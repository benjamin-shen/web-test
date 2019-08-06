#! /usr/bin/python
import cgitb
cgitb.enable()
print('content-type: text/html\n')

import testModule

# read html template
source = open('../templates/administerTest.html','rU')
html = source.read()
source.close()

# interprets hidden submitted data
import cgi
fromQS = cgi.FieldStorage()
# print fromQS
name = fromQS['name'].value
testChoice = fromQS['testChoice'].value

import csvToDict
# create personalized dictionary
allStudents = csvToDict.csvToDict("../students/"+testChoice)
# print allStudents
studentDict = allStudents[name]
# print studentDict
questionNumber = int(studentDict['questionNumber'])
# print questionNumber

# get test details
testCsv = csvToDict.csvToDict("../tests/"+testChoice)
# print testCsv

# for received answer
score = int(studentDict['score'])
continuation = "answer" in fromQS # if continuation of the recursive program, could've tested for any hidden input sent later
if continuation and questionNumber < len(testCsv)+1:
    lastQuestion = fromQS['lastQuestion'].value
    # see if question is new
    if lastQuestion == testCsv[str(questionNumber)]['question']:
        # validate answer
        if fromQS['answer'].value == testCsv[str(questionNumber)]['correctAnswer']:
            score += 1
        # update question number
        questionNumber += 1
        # update csv file
        testModule.update_csv(name,testChoice,questionNumber,score)

if questionNumber < len(testCsv)+1:
    # get question details
    questionDetails = testCsv[str(questionNumber)]
    # update html
    html = html.replace("question_placeholder",questionDetails['question'])
    html = html.replace("a_placeholder",questionDetails['a'])
    html = html.replace("b_placeholder",questionDetails['b'])
    html = html.replace("c_placeholder",questionDetails['c'])
    html = html.replace("d_placeholder",questionDetails['d'])
    html = html.replace("lastQuestion_placeholder",questionDetails['question'])
    html = html.replace("number_placeholder",str(questionNumber))
    html = html.replace("name_placeholder",name)
    html = html.replace("testChoice_placeholder",testChoice)
    # produce html
    print(html)
else:
    print(testModule.handleCompletion(name,score,questionNumber-1))
