# flask web framework
from flask import Flask,render_template, request

# DB modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base,User

# flask basic authentication
from flask_httpauth import HTTPBasicAuth

#DB configuration
engine = create_engine('sqlite:///catalogBDSetup.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

# Basic Auth configuration
auth = HTTPBasicAuth()

# create flask app
app = Flask(__name__)


# app routes
@app.route('/')
def main_page():
    return render_template('base.html')

@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print(request.form['username_or_email'])
    return render_template('/auth/login.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
