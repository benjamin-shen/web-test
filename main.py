from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    file = open("templates/index.html", "r")
    return file.read()

@app.route('/documentation')
def documentation():
    file = open("documentation.html", "r")
    return file.read()

@app.route('/login')
def login():
    from app import login
    return login.result()

@app.route('/validation', methods=['GET','POST'])
def after_login():
    from app import after_login
    return after_login.result()

if __name__ == '__main__':
   app.run(debug = True)
