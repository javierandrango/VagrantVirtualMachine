# Prerequisites
1. Hashing password
    ```bash
    pip3 install passlib --user
    ```
2. HTTP authentication for Flask routes
    ```bash
    pip3 install Flask-HTTPAuth==4.4.0 --user
    ```
3. Safely pass data to untrusted environments and back (encode token)
    ```bash
    pip3 install itsdangerous --user
    ```
4. handling Cross Origin Resource Sharing (CORS) security mechanism that restricts resources being fetched from a different origin
    ```bash
    pip3 install flask-cors==3.0.10 --user
    ```
5. To use ad-hoc certified inside flask with CORS we need the cryptography module
Previously I deleted this module and re-installed again is a little tricky 
    ```bash
    sudo apt install python3-dev build-essential gcc 
    sudo apt install libssl-dev libffi-dev
    sudo pip3 install cryptography==3.2.1 
    ```
6. Update database (migrate changes in data base):
    ```bash
    pip3 install alembic==1.4.3 --user
    ```
7. Make requests for test endpoints
    ```bash
    pip3 install httplib2 --user
    ```
8. Hash password 
    ```bash
    pip3 install bcrypt --user
    ```
9. Google authentication library
    ```bash
    pip3 install google-auth --user
    ```

# Usage
1. Add a user to test the login process

    ```bash
    cd ItemCatalogApp/tests/
    python3 single_user.py
    ```