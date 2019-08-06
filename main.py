from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    file = open("index.html", "r")
    return file.read()

if __name__ == '__main__':
   app.run(debug = True)
