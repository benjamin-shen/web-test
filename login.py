#! /usr/bin/python
import cgitb
cgitb.enable()
print 'content-type: text/html\n'

# read html template
source = open("./templates/login.html",'rU')
template = source.read()
source.close()
# assign to loginPage
loginPage = template
# print loginPage

# write html for options in select tag from csv file
def createOptions(filename,placeholder,webpage):
    csv = open(filename,'rU')
    lines = csv.read().split('\n')
    csv.close()
    # retrieve account names
    accountNames = []
    for line in lines[1:]:
        field = line.split(',')
        accountNames.append(field[0])
    accountNames.sort()
    # replace placeholder
    options_placeholder = ""
    for name in accountNames:
        options_placeholder += "<option> " + name + " </option>  "
    webpage = webpage.replace(placeholder,options_placeholder)
    return webpage

loginPage = createOptions("./data/accounts.csv",'student_options',loginPage)
loginPage = createOptions("./data/teachers.csv",'teacher_options',loginPage)

# produce html
print loginPage
