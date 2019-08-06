#! /usr/bin/python
import cgitb
cgitb.enable()
print 'content-type: text/html\n'

# interprets submitted data
import cgi
fromQS = cgi.FieldStorage()
# for name in fromQS:
#     print name, fromQS[name]

# reads and converts csv file into dictionary
import csvToDict
# for passwords
import hashlib

if "student" in fromQS: # if student logs in
    accounts = csvToDict.csvToDict('./data/accounts.csv')
    # adapted from hw54 (login page)
    name = fromQS['studentName'].value
    try:
        password = fromQS['studentPassword'].value
        encrypted = hashlib.sha256(password).hexdigest()
        success = accounts[name]['password'] == encrypted
        if success:
            title = "Welcome student!"
        else:
            title = "Invalid Password"
    except:
        title = "Missing Password"
elif "name" in fromQS: # if student finishes a test and wants to take another one
    accounts = csvToDict.csvToDict('./data/accounts.csv')
    name = fromQS['name'].value
    title = "Welcome student!"
else: # if "teacher" in fromQS, if teacher logs in
    accounts = csvToDict.csvToDict('./data/teachers.csv')
    name = fromQS['teacherName'].value
    try:
        password = fromQS['teacherPassword'].value
        encrypted = hashlib.sha256(password).hexdigest()
        success = accounts[name]['password'] == encrypted
        if success:
            title = "Welcome teacher!"
        else:
            title = "Invalid Password"
    except:
        title = "Missing Password"


# read html template
source = open("./templates/after_login.html",'rU')
template = source.read()
source.close()
html = template.replace("title_placeholder",title)

# update html

if title == "Invalid Password":
    body = '<h2> Wrong password. Please try again. </h2> <a href="login.py"> Retry </a>'
    html = html.replace("body_template", body)
elif title == "Missing Password":
    body = '<h2> Please enter a password. </h2> <a href="login.py"> Retry </a>'
    html = html.replace("body_template", body)
else: # if successful login
    import loginModule
    if title == "Welcome student!":
        source = open("./templates/studentLogin.html",'rU')
        body = source.read()
        source.close()
        html = html.replace("body_template",body)
        html = html.replace("name_placeholder",name)
        inputs = '<h1> Please select a test. </h1>' + loginModule.htmlChoices(loginModule.testChoices())
        html = html.replace("inputs_placeholder",inputs)
    else: # if title == "Welcome teacher!"
        source = open("./templates/teacherLogin.html",'rU')
        body = source.read()
        source.close()
        html = html.replace("body_template",body)
        inputs = '''<p align="right">
<b><a href="login.py" style="text-decorations:none; color:inherit;">Log out</a></b>
</p>'''
        if name == "View Scores":
            html = html.replace("action_placeholder","teacherStats.py")
            inputs += '\n<h1> What scores do you want to view? </h1>\n' + loginModule.htmlChoices(loginModule.testChoices())
        elif name == "Register a Student":
            html = html.replace("action_placeholder","registerStudent.py")
            inputs += '\n<h1> Who do you want to register? </h1>\n' + loginModule.formNamePassword()
        elif name == "Add Test":
            html = html.replace("action_placeholder","createTest.py")
            inputs += '\n<h1> Please create the test form. </h1>\n' + loginModule.testGeneralInfo()
        # add more options
        html = html.replace("inputs_placeholder",inputs)

# produce html
print html
