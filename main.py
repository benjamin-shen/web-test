from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    file = open("index.html", "r")
    return file.read()

@app.route('/login.py')
def index():
    import login
    return login.result()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_dir(path):
    return path

if __name__ == '__main__':
   app.run(debug = True)
