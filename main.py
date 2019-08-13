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

@app.route('/validation', methods=['POST'])
def after_login():
    from app import after_login
    return after_login.result()

@app.route('/test', methods=['POST'])
def administerTest():
    from app import administerTest
    return administerTest.result()

@app.route('/createTest', methods=['POST'])
def createTest():
    from app import createTest
    return createTest.result()

@app.route('/testCreated', methods=['POST'])
def testCreated():
    from app import testCreated
    return testCreated.result()

@app.route('/registerStudent', methods=['POST'])
def registerStudent():
    from app import registerStudent
    return registerStudent.result()

@app.route('/teacherStats', methods=['POST'])
def teacherStats():
    from app import teacherStats
    return teacherStats.result()

if __name__ == '__main__':
   app.run(debug = True)
