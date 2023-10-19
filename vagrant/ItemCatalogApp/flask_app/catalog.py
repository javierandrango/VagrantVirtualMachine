# flask web framework
from flask import Flask,render_template, request, redirect,url_for,\
                    jsonify,g,current_app,abort
from flask import session as temp_session

#security
from flask_cors import CORS

# DB modules
from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
from db_setup import Base,User

# DB exceptions modules
from sqlalchemy.orm import exc

# flask basic,token authentication
from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth

# verify hashed password
import bcrypt

# oauth2 providers
from auth import Providers
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

#DB configuration
engine = create_engine('sqlite:///../catalogDBSetup.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

# Login Auth configuration
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')

# create flask app 
app = Flask(__name__, 
            template_folder = '../frontend/templates/', 
            static_folder = '../frontend/static/')

# import oauth configuration from auth.py
app.config.from_object(Providers)

# Enable CORS if making cross-origin requests in all routes
CORS(app)

# app routes
# ----------------------------------------------------------------------------
# main page
@app.route('/')
def main_page():
    if 'username' not in temp_session:
        return render_template('base.html')
    else:
        return render_template('active_account_base.html',
                               username=temp_session.get('username'),
                               picture=temp_session.get('picture'),
                               email=temp_session.get('email'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# login: render template
@app.route('/login/')
def login():
    return render_template('/auth/login.html')

# login: username or email verification
@app.route('/login/verify_username_or_email/', methods=['POST'])
def username_or_email():
    username = None
    message = ""
    if request.method == 'POST':
        username_or_email = request.json.get('username_or_email')
        username,salt = verify_username(username_or_email)
        #print('DB username:', username)
        # empty imput or wrong username
        if not(username_or_email) or not(username):
            #flash("Sorry, we could not find your account.")
            message = "Sorry, we could not find your account."
    return jsonify({'username': username, 'salt': salt, 'message':message})


# login: password verification
@basic_auth.verify_password
def pswd_verification(username,pswd_hash):
    try:
        user = session.query(User).filter(and_(User.username==username,User.password_hash==pswd_hash)).one()
    except exc.NoResultFound:
        user = None
    if(user):
        g.user = user
        return True
    return False


# login: status code handling for bad credentials
@basic_auth.error_handler
@token_auth.error_handler
def unauthorized():
    '''
    # this code prevent browser default login prompt to open when status 
    # code 401(flask default status code response) is send with header 
    # WW-Authenticate = 'Basic realm="Authentication Required"'
    response = jsonify(message="Unauthorized")
    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'xBasic realm="Authentication Required"'
    return response
    '''
    #change the original status code to prevent browser defautl login prompt to open
    response = jsonify(message="Unauthorized. This is a protected resource")
    response.status_code = 400
    return response


# login: granted access after password verification to generate an access token
@app.route('/login/verify_pswd/', methods=['POST'])
@basic_auth.login_required
def get_access_token():
    message = ''
    token = ''
    status_code = 200
    if request.method == 'POST':
        if (g.user is not None):
            token = g.user.generate_auth_token()
            message = 'authenticated user'
        #print('access token: ',token)
        return jsonify({'token':token,'message':message}), status_code


# login: verify access token 
@token_auth.verify_token
def verify_acess_token(token):
    user_id = User.verify_auth_token(token)
    if (not user_id):
        return False   
    g.user = session.query(User).filter_by(id=user_id).first()     
    return True


# login: granted access after access token verification (for test purposes)
'''
@app.route('/login/protected_resource/', methods=['GET'])
@token_auth.login_required
def get_resource():
    if request.method == 'GET':
        #print(g.user.username)
        temp_session['username'] = g.user.username
    return jsonify({'protected_resource': 'hello '+g.user.username}), 200
'''

# login: required user data to update active account header
@app.route('/login/user_info/', methods=['GET'])
@token_auth.login_required
def user_info():
    if request.method == 'GET':
        temp_session['username'] = g.user.username
        temp_session['picture'] = g.user.picture 
        temp_session['email'] = g.user.email        
    return jsonify({'username':g.user.username}),200

# login: send flash messages to client
'''
@app.route('/login/flash_msgs', methods=['GET','POST'])
def get_flash_msgs():
    flash_msgs = dict(session['_flashes']) 
    return jsonify(flash_msgs)
'''
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# logout
@app.route('/logout/')
def logout():
    temp_session.clear()
    return redirect(url_for('main_page'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# login with google: response 
@app.route('/login/callback/google',methods=['POST'])
def oauth2_google():
    if request.method =='POST':
        '''
        # show all request content that has application/x-www-form-urlencoded format
        for key, value in request.form.items():
                print('Field: {}, Value: {}'.format(key,value))
        '''
        #print('credential:',request.form.get('credential'))
        #print('cookies:',request.cookies)

        # Verify the Cross-Site Request Forgery (CSRF) token
        csrf_token_cookie = request.cookies.get('g_csrf_token')
        #print('csrf_token_cookie',csrf_token_cookie)
        if not csrf_token_cookie:
            abort(400,'No CSRF token in Cookie.')
        csrf_token_body = request.form.get('g_csrf_token')
        #print('csrf_token_body',csrf_token_body)
        if not csrf_token_body:
            abort(400,'No CSRF token in post body.')
        if csrf_token_cookie != csrf_token_body:
            abort(400,'Failed to verify double submit cookie.')
        
        # validate ID token 
        credential = request.form.get('credential')
        provider_data = current_app.config['OAUTH2_PROVIDERS'].get('google')
        client_id = provider_data['client_id']
        try:
            idinfo = id_token.verify_oauth2_token(credential,google_requests.Request(),client_id)
            temp_session['username'] = idinfo['name']
            temp_session['email'] = idinfo['email']
            temp_session['picture'] = idinfo['picture']
        except ValueError:
            abort(400,'Failed to authenticate user')
        
        # save google user in database if not exist
        google_user = session.query(User).filter_by(email=idinfo['email']).first()
        if (google_user is None):
            new_user = User(username=idinfo['name'],
                            email=idinfo['email'],
                            picture=idinfo['picture'])
            session.add(new_user)
            session.commit()

    return redirect(url_for('main_page'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# signup: render template
@app.route('/signup/')
def signup():
    return render_template('/auth/signup.html')

# sign up: verify if user and email already exist
@app.route('/signup/verify-new-user/', methods=['POST'])
def check_new_user():
    email_msg = ''
    if request.method == 'POST':
        #print('request email:',request.json.get('email'))
        user_exist = check_new_user(request.json.get('email'))
    if (user_exist is not None):
        email_msg = 'email already exist'
    return jsonify({'email_msg':email_msg}),200

# sign up: save new user information
@app.route('/signup/newuser', methods=['POST'])
def new_user():
    if request.method == 'POST':
        completed_form = request.json.get('completed_form')
        user_data = request.get_json()
        #print("form status:", completed_form)
        #print("new user data:",user_data)
        if (completed_form == False):
            new_user = User()
            if 'new_username' in user_data:
                new_user.username = user_data['new_username']
            if 'new_email' in user_data:
                new_user.email = user_data['new_email']
            if 'new_picture' in user_data:
                new_user.username = user_data['new_picture']
            if 'new_password_hash' in user_data:
                new_user.username = user_data['new_password_hash']
            if 'new_password_salt' in user_data:
                new_user.username = user_data['new_password_salt']
            session.add(new_user)
            return jsonify({'form status':'INcomplete'}),200
        elif(completed_form == True):
            session.commit()
            return jsonify({'form status':'complete'}),200
         
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# user functions
def verify_username(username_or_email):
    try:
        # query by username or email
        this_user = session.query(User).filter(or_(User.username==username_or_email,
                                                   User.email==username_or_email)).one()
        username = this_user.username
        salt = this_user.password_salt
    except exc.NoResultFound:
        username = None
        salt = None
    return username,salt

# verify if email already exist or used by other user
def check_new_user(email):
    try:
        this_user = session.query(User).filter_by(email=email).one()
    except exc.NoResultFound:
        this_user = None
    return this_user

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# to run app in comand line
# SSL/TLS encryptation for development and testing: adhoc
# secret_key temporarily used for flask message (CHANGE KEY)
if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0', port=8000, ssl_context='adhoc') 
# ----------------------------------------------------------------------------