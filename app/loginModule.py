# this module is broken

# module to handle student logins

def testChoices():
    import urllib
    html =  urllib.urlopen("static/tests").read() # html code for tests directory
    # print html
    # isolate dynamic part of webpage
    lenStart = 1 + len("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /~benjamin.shen/project/tests</title>
 </head>
 <body>
<h1>Index of /~benjamin.shen/project/tests</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/~benjamin.shen/project/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>""")
    lenEnd = len(html) - len("""
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.7 (Ubuntu) Server at homer.stuy.edu Port 80</address>
</body></html>""") - 1
    html = html[lenStart:lenEnd]

    # split by row
    csvList = html.split("<tr>")[1:] # spliced to get rid of empty string (element 0)
    # print len(csvList)
    # '<td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="chem.csv">chem.csv</a></td><td align="right">2016-06-09 15:46  </td><td align="right">418 </td><td>&nbsp;</td></tr>\n'

    # listing csv file names
    testList = []
    rowNumber = 0
    while rowNumber < len(csvList):
        start = csvList[rowNumber].find("href=") + 6
        end = csvList[rowNumber][start+1:].find('"') + start + 1
        testList.append(csvList[rowNumber][start:end])
        rowNumber += 1
        # print "done"
    # print testList

    return testList

def htmlChoices(testList):
    inputs = '<table align="center"> <tr><td>\n'
    for file in testList:
        name = file[:len(file)-4] # everything before .csv
        inputs += '<input type="radio" name="testChoice" value="' + file + '" required> ' + name + ' <br><br>\n'
    inputs += '<br> <input type="submit" value="Choose test">\n<tr><td> </table>'
    return inputs

def formNamePassword():
    inputs = '''<table align="center"><tr><td>
Student name: <input type="text" name="registerName" required> <br><br>
Student password: <input type="password" name="registerPassword" required> <br><br>
<div style="text-align:center"><input type="submit" value="Register"></div>
</table>'''
    return inputs

def testGeneralInfo():
    inputs = '''<table align="center"><tr><td align="center">
Test name: <b>(a-z,A-Z,0-9,-,_)</b> <br>
<input type="text" name="testName" required></div><br><br>
Number of questions: <br>
<input type="number" name="numberQuestions" min="1" required> <br><br>
<input type="submit" value="Create Form">
</table>'''
    return inputs
