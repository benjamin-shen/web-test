from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    import login
    return login.result()

if __name__ == '__main__':
   app.run(debug = True)
