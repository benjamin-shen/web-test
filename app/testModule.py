# module for administerTest.py

def update_csv(name,testChoice,questionNumber,score): # update students csv file
    # read csv file
    source = open("client/students/"+testChoice,'rU')
    csv = source.read()
    source.close()
    # change values
    firstComma = csv.find(name) + len(name)
    secondComma = csv[firstComma+1:].find(",") + firstComma + 1
    newline = csv[secondComma+1:].find("\n") + secondComma + 1
    # write to csv file
    dest = open("client/students/"+testChoice,'w')
    dest.write(csv[:firstComma+1] + str(questionNumber) + "," + str(score) + csv[newline:])
    dest.close()

def handleCompletion(name,score,questionNumber):
    source = open("templates/congrats.html",'rU')
    html = source.read()
    source.close()

    html = html.replace("score_placeholder",str(score)+"/"+str(questionNumber))
    html = html.replace("name_placeholder",name)
    return html
