#! /usr/bin/python
import cgitb
cgitb.enable()
print 'content-type: text/html\n'

# organize received data
import cgi
fromQS = cgi.FieldStorage()
name = fromQS['name'].value
questionList = []
for field in sorted(fromQS):
    # print field
    if field != 'name':
        questionList.append(fromQS[field])
# print questionList

def create(questionList):
    testContent = 'number,question,a,b,c,d,correctAnswer\n'
    field = 0
    while field < len(questionList):
        testContent += str((field + 6)/6) + ","
        testContent += questionList[field].value + ","
        testContent += questionList[field+1].value + ","
        testContent += questionList[field+2].value + ","
        testContent += questionList[field+3].value + ","
        testContent += questionList[field+4].value + ","
        testContent += questionList[field+5].value + "\n"
        field += 6
    # write questions into test file
    dest = open('./tests/'+name,'w',0)
    dest.write(testContent[:len(testContent)-1])
    dest.close()

    studentContent = 'student,questionNumber,score\n'
    import csvToDict
    studentDatabase = csvToDict.csvToDict('./data/accounts.csv')
    for student in studentDatabase:
        studentContent += student + ",1,0\n"
    dest = open('./students/'+name,'w',0)
    dest.write(studentContent)
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

questionString = ""
for miniFS in questionList:
    questionString += miniFS.value
if not "," in questionString:
    create(questionList)
    body += '<div align="center"><h1> New test (' + name + ') created </h1>\n</div>'
    html = html.replace("title_placeholder","Test Created")
else:
    body += '<div align="center"><h1> There is a comma in your input; <br> press the back key </h1></div>'
    html = html.replace("title_placeholder","Invalid Input")

# produce html
html = html.replace("body_template",body)
print html
