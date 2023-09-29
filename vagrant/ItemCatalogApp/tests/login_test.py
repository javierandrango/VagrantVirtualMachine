# make requests
from httplib2 import Http
import json
import sys

# encode data
import base64


#first user credentials:
username = 'javier'
hash = '$2a$10$e/kHhQ3bNuDono.BlbSb/.I95SnVD69PkfOIQbvrg58DTS.InHBem'

print ("Running Endpoint Tester....\n")
address = str(input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:8000':   "))
if address == '':
    address = 'https://localhost:8000'


# TEST 1: try to get token with INVALID credentials
try:
    url = address + '/login/verify_pswd/'
    # only for test purposes disable ssl certified
    h = Http(disable_ssl_certificate_validation=True)
    invalid_hash = hash+'.234s$'
    credentials = username+':'+invalid_hash
    credentials64 = base64.b64encode(credentials.encode('utf-8')).decode()
    data={}
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Basic '+ credentials64,
    }
    resp, content = h.request(url,'POST',body=data,headers=headers)
    if resp['status'] =='200':
        raise Exception('Security Flaw: able to log in with INVALID credentials') 
except Exception as err:
    print('TEST 1 FAILED!')
    print(err.args)
    sys.exit()
else:
    print('TEST 1 PASS: Check against INVALID credentials')


# TEST 2: try to get token with VALID credentials
try:
    url = address + '/login/verify_pswd/'
    # only for test purposes disable ssl certified
    h = Http(disable_ssl_certificate_validation=True)
    credentials = username+':'+hash
    credentials64 = base64.b64encode(credentials.encode('utf-8')).decode()
    data={}
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Basic '+ credentials64,
    }
    resp, content = h.request(url,'POST',body=data,headers=headers)
    if resp['status'] !='200':
        raise Exception('Unable to get token with VALID credentials') 
    token = json.loads(str(content,'UTF-8'))['token']
    #print('token: ',token)
except Exception as err:
    print('TEST 2 FAILED!')
    print(err.args)
    sys.exit()
else:
    print('TEST 2 PASS: App checks token with VALID credentials')



# TEST 3: try to read protected resource with INVALID TOKEN
try:
    url = address + '/login/protected_resource'
    # only for test purposes disable ssl certified
    h = Http(disable_ssl_certificate_validation=True)
    invalid_token = token+'wedfr5'
    headers = {"Authorization": "Bearer "+invalid_token}
    resp, content = h.request(url,'GET',headers=headers)
    if resp['status'] =='200':
        raise Exception('Security Flaw: able to log in with INVALID token') 
except Exception as err:
    print('TEST 3 FAILED!')
    print(err.args)
    sys.exit()
else:
    print('TEST 3 PASS: Check against INVALID token')


# TEST 4: try to read protected resource with VALID TOKEN
try:
    url = address + '/login/protected_resource'
    # only for test purposes disable ssl certified
    h = Http(disable_ssl_certificate_validation=True)
    headers = {"Authorization": "Bearer "+token}
    resp, content = h.request(url,'GET',headers=headers)
    if resp['status'] !='200':
        raise Exception('Unable to access protected API resource with valid token')
    print("protected resource:", json.loads(str(content,'UTF-8'))['protected resource']) 
except Exception as err:
    print('TEST 4 FAILED!')
    print(err.args)
    sys.exit()
else:
    print('TEST 4 PASS: login-in user can view protected resource')
