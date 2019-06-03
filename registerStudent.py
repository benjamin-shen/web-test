#! /usr/bin/python
import cgitb
cgitb.enable()
print 'content-type: text/html\n'

# interprets submitted data
import cgi
fromQS = cgi.FieldStorage()

student = fromQS["registerName"].value
password = fromQS["registerPassword"].value
# print student, password

# check validity of student name
valid = not "," in student
import csvToDict
studentDatabase = csvToDict.csvToDict('/home/students/2018/benjamin.shen/accounts.csv')
for name in studentDatabase:
    valid = valid and not name == student

# adapted from 2016.05.25's Do Now
def addAccount(username,password):
    dest = open('/home/students/2018/benjamin.shen/accounts.csv', 'a', 0)
    newAccount = '\n' + username + ',' + password
    dest.write(newAccount)
    dest.close()
    
    import loginModule
    for testChoice in loginModule.testChoices():
        dest = open('/home/students/2018/benjamin.shen/public_html/project/students/'+testChoice, 'a', 0)
        newAccount = username + ',1,0\n'
        dest.write(newAccount)
        dest.close()

# read template
source = open('./templates/after_login.html','rU') # need the same template
html = source.read()
source.close()
body = """

<p align="right">
<b><a href="login.py" style="text-decorations:none; color:inherit;">Log out</a></b>
</p>
"""

# update body
if valid:
    import hashlib
    addAccount(student,hashlib.sha256(password).hexdigest())
    body += '<div align="center"><h1> <u>student_placeholder</u> is now registered </h1>\n<h2>password: <u>' + password + '</u></h2></div>'
    html = html.replace("title_placeholder","Student Registered")
else:
    body += '<div align="center"><h1> "student_placeholder" is an invalid name </h1></div>'
    html = html.replace("title_placeholder","Failed Registration")
body = body.replace("student_placeholder",student)

# produce html
html = html.replace("body_template",body)
print html