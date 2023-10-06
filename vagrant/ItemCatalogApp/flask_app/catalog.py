# flask web framework
from flask import Flask,render_template, request, redirect,url_for,flash,\
                    jsonify,g,abort
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

# Enable CORS if making cross-origin requests in all routes
CORS(app)


# app routes
# main page
@app.route('/')
def main_page():
    return render_template('base.html')

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
@app.route('/login/protected_resource/', methods=['GET'])
@token_auth.login_required
def get_resource():
    if request.method == 'GET':
        #print(g.user.username)
        temp_session['username'] = g.user.username
    return jsonify({'protected_resource': 'hello '+g.user.username}), 200

# login: required user data to show in frotend
@app.route('/login/user_info/', methods=['GET'])
@token_auth.login_required
def user_info():
    if request.method == 'GET':
        temp_session['username'] = g.user.username
        temp_session['picture'] = g.user.picture
        temp_session['email'] = g.user.email            
    return jsonify({'username':temp_session.get('username'),
                    'picture':temp_session.get('picture'),
                    'email':temp_session.get('email')})


# login: send flash messages to client
@app.route('/login/flash_msgs', methods=['GET','POST'])
def get_flash_msgs():
    flash_msgs = dict(session['_flashes']) 
    return jsonify(flash_msgs)


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


# to run app in comand line
# SSL/TLS encryptation for development and testing: adhoc
# secret_key temporarily used for flask message (CHANGE KEY)
if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0', port=8000, ssl_context='adhoc') 
