#! /usr/bin/python
import cgitb
cgitb.enable()
print 'content-type: text/html\n'

# interprets submitted data
import cgi
fromQS = cgi.FieldStorage()

name = fromQS["testName"].value
# print name
name = name.replace(" ","_")

# see if the filename is valid
valid = True
for character in name:
    ascii = ord(character)
    valid = valid and (ord('0')<=ascii<=ord('9') or ord('A')<=ascii<=ord('Z') or ord('a')<=ascii<=ord('z') or ascii==ord('-') or ascii==ord('_'))
name += ".csv"
import loginModule
# print loginModule.testChoices()
if name in loginModule.testChoices():
    valid = False

# read template
source = open('./templates/after_login.html','rU') # need the same template
html = source.read()
source.close()
body = """
<p align="right">
<b><a href="login.py" style="text-decorations:none; color:inherit;">Log out</a></b>
</p>
"""

def testForm(quantity):
    question = 1
    html = '<table align="center"><tr><td>\n<form action="testCreated.py" method="POST">\n<input type="hidden" name="name" value="name_placeholder">'
    while question <= quantity:
        html += '''
    Question ''' + str(question) + ''': <input type="text" name="''' + str(question) + '''" required> <br>
    Choice A: <input type="text" name="''' + str(question) + '''A" required> <br>
    Choice B: <input type="text" name="''' + str(question) + '''B" required> <br>
    Choice C: <input type="text" name="''' + str(question) + '''C" required> <br>
    Choice D: <input type="text" name="''' + str(question) + '''D" required> <br>
    Correct Answer: <select name="''' + str(question) + '''answer" size="1"> 
        <option> a </option>
        <option> b </option>
        <option> c </option>
        <option> d </option>
      </select> <br> <br> \n'''
    
        question += 1
    html += '<div align="center"><input type="submit" value="Create Test"></div></form></td></tr></table>'
    return html

# update body
if valid:
    quantity = int(fromQS["numberQuestions"].value)
    body += '<div align="center"><h1> Test Location: name_placeholder </h1>\n</div>' + testForm(quantity)
    html = html.replace("title_placeholder","Test Form")
else:
    body += '<div align="center"><h1> "name_placeholder" is an invalid test name </h1></div>'
    html = html.replace("title_placeholder","Invalid Name")

# produce html
body = body.replace("name_placeholder",name)
html = html.replace("body_template",body)
print html