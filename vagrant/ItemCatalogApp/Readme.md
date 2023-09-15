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

# Usage
1. Add a user to test the login process

    ```bash
    cd ItemCatalogApp/tests/

    python3 single_user.py
    ```