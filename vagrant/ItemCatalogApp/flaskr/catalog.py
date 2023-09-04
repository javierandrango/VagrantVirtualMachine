# flask web framework
from flask import Flask

# create flask app
app = Flask(__name__)


# app routes
@app.route('/')
def main_page():
    return "main_page"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
