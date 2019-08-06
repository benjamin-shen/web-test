from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    file = open("index.html", "r")
    return file.read()

app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods = ['GET'])

if __name__ == '__main__':
   app.run(debug = True)
