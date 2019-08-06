from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_dir(path):
    return path

if __name__ == '__main__':
   app.run(debug = True)
