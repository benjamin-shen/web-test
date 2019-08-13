#! /usr/bin/python
# import cgitb
# cgitb.enable()
# print('content-type: text/html\n')

# interprets submitted data
# import cgi
# fromQS = cgi.FieldStorage(environ="post")
from flask import request

# reads and converts csv file into dictionary
from app import csvToDict

# for successful login
from app import loginModule

def result():
    fromQS = request.form
    if "student" in fromQS and fromQS['student'] != "": # if student logs in
        accounts = csvToDict.csvToDict('client/data/accounts.csv')
        # adapted from hw54 (login page)
        name = fromQS['studentName']
        try:
            password = fromQS['studentPassword']
            success = accounts[name]['password'] == password
            if success:
                title = "Welcome student!"
            elif password == "":
                title = "Missing Password"
            else:
                title = "Invalid Password"
        except:
            title = "Error"
    elif "name" in fromQS and fromQS['name'] != "": # if student finishes a test and wants to take another one
        accounts = csvToDict.csvToDict('client/data/accounts.csv')
        name = fromQS['name']
        title = "Welcome student!"
    else: # if "teacher" in fromQS, if teacher logs in
        accounts = csvToDict.csvToDict('client/data/teachers.csv')
        action = fromQS['teacherAction']
        try:
            password = fromQS['teacherPassword']
            success = accounts[action]['password'] == password
            if success:
                title = "Welcome teacher!"
            elif password == "":
                title = "Missing Password"
            else:
                title = "Invalid Password"
        except:
            title = "Error"


    # read html template
    source = open("templates/after_login.html",'rU')
    template = source.read()
    source.close()
    html = template.replace("title_placeholder",title)

    # update html

    if title == "Missing Password":
        body = '<h2> Please enter a password. </h2> <a href="login"> Retry </a>'
        html = html.replace("body_template", body)
    elif title == "Invalid Password":
        body = '<h2> Wrong password. Please try again. </h2> <a href="login"> Retry </a>'
        html = html.replace("body_template", body)
    elif title == "Error":
        body = '<h2> Error. Please try again. </h2> <a href="login"> Retry </a>'
        html = html.replace("body_template", body)
    else: # if successful login
        if title == "Welcome student!":
            source = open("templates/studentLogin.html",'rU')
            body = source.read()
            source.close()
            html = html.replace("body_template",body)
            html = html.replace("name_placeholder",name)
            inputs = '<h1> Please select a test. </h1>' + loginModule.htmlChoices(loginModule.testChoices())
            html = html.replace("inputs_placeholder",inputs)
        else: # if title == "Welcome teacher!"
            source = open("templates/teacherLogin.html",'rU')
            body = source.read()
            source.close()
            html = html.replace("body_template",body)
            inputs = '''<p align="right">
    <b><a href="login" style="text-decorations:none; color:inherit;">Log out</a></b>
    </p>'''
            if action == "View Scores":
                html = html.replace("action_placeholder","teacherStats")
                inputs += '\n<h1> What scores do you want to view? </h1>\n' + loginModule.htmlChoices(loginModule.testChoices())
            elif action == "Register a Student":
                html = html.replace("action_placeholder","registerStudent")
                inputs += '\n<h1> Who do you want to register? </h1>\n' + loginModule.formNamePassword()
            elif action == "Add Test":
                html = html.replace("action_placeholder","createTest")
                inputs += '\n<h1> Please create the test form. </h1>\n' + loginModule.testGeneralInfo()
            # add more options
            html = html.replace("inputs_placeholder",inputs)

    # produce html
    # print(html)
    return html
