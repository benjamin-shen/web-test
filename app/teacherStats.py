#! /usr/bin/python
# import cgitb
# cgitb.enable()
# print('content-type: text/html\n')

# interpret data
# import cgi
# fromQS = cgi.FieldStorage()
from flask import request

from app import csvToDict, testModule, statModule

def result():
    fromQS = request.form
    testChoice = fromQS['testChoice']

    # dealing with resetting data
    def reset(name):
        testModule.update_csv(name,testChoice,1,0)
    for name in fromQS:
        if name == "reset":
            if isinstance(fromQS[name],list):
                position = 0
                while position < len(fromQS[name]):
                    # print fromQS[name][position].value
                    reset(fromQS[name][position])
                    position += 1
            else:
                # print fromQS[name].value
                reset(fromQS[name])

    csvDict = csvToDict.csvToDict('client/students/'+testChoice)
    csvList = csvDict.keys()
    csvList = sorted(csvList)
    # print csvList

    # successful teacher login
    def success(testChoice):
        def fraction(name):
            if questionNumber != 0: # for users that didn't take the test
                return csvDict[name]["score"] + "/" + str(int(csvDict[name]["questionNumber"])-1)
            else:
                return " - "
        def percent(name):
            if questionNumber != 0: # for users that didn't take the test
                return str(int(int(csvDict[name]["score"])/float(questionNumber) *100))
            else:
                return " - "
        def redify():
            # determine if end of test
            testCsv = csvToDict.csvToDict("client/tests/"+testChoice)
            notEndOfTest = questionNumber < len(testCsv)
            if notEndOfTest:
                return ' style="color:red";'
            return ""

        # create table
        table = ""
        for name in csvList[1:]: # to splice out empty string
            questionNumber = (int(csvDict[name]["questionNumber"])-1)
            table += '''  <tr''' + redify() + '''>
        <td align="center">
          ''' + name + '''
        </td>
        <td align="center">
          ''' + fraction(name) + '''
        </td>
        <td align="center">
          ''' + percent(name) + '''
        </td>
        <td align="center">
          <input type="checkbox" name="reset" value="''' + name + '''">
        </td>
      </tr>\n'''

        # produce html
        return table

    # read template
    source = open("templates/teacherStats.html",'rU')
    template = source.read()
    source.close()

    # change and produce html
    html = template.replace("table_placeholder",success(testChoice))
    html = html.replace("testChoice_value",testChoice)

    scorePercents = []
    del csvDict[""]
    for name in csvDict:
        # from redify function above
        totalNumberQ = len(csvToDict.csvToDict("client/tests/"+testChoice))
        if int(csvDict[name]["questionNumber"])-1 == totalNumberQ: # if completed test
            scorePercents.append(int(int(csvDict[name]["score"])/float(totalNumberQ) *100))

    mean = str(statModule.mean(scorePercents))
    median = str(statModule.median(scorePercents))
    mode = str(statModule.mode(scorePercents))
    maxValue = str(statModule.customMax(scorePercents))
    minValue = str(statModule.customMin(scorePercents))

    html = html.replace("mean_placeholder", mean)
    html = html.replace("median_placeholder", median)
    html = html.replace("mode_placeholder", mode)
    html = html.replace("max_placeholder", maxValue)
    html = html.replace("min_placeholder", minValue)

    # print(html)
    return html
