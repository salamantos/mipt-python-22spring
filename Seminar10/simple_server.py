from flask import Flask


# the main Flask application object
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return {'data': 'hello!'}


# this makes your Flask application start
# will start at http://127.0.0.1:5000/
if __name__ == "__main__":
    app.run(debug=True)
