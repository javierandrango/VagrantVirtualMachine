import os
from dotenv import load_dotenv
load_dotenv()
class Providers(object):
    OAUTH2_PROVIDERS={
    # Google OAuth 2.0 documentation:
    # https://developers.google.com/identity/protocols/oauth2/web-server#httprest
    'google': {
        'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
        'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        'admin_client_id': os.environ.get('ADMIN_GOOGLE_CLIENT_ID'),
        'admin_client_secret': os.environ.get('ADMIN_GOOGLE_CLIENT_SECRET'),
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'token_url': 'https://accounts.google.com/o/oauth2/token',
        'userinfo': {
            'url_info': 'https://openidconnect.googleapis.com/v1/userinfo',
            'email': lambda json: json['email'],
        },
        'scopes': ['https://www.googleapis.com/auth/userinfo.profile','https://www.googleapis.com/auth/userinfo.email'],
    },

    # add more Oauth2 providers below:
}