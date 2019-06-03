# from Benjamin Shen's hw53-hw55 (csvToDict)

def getStringsOfLines(fileName):
    source = open(fileName,'rU')
    fileContents = source.read()
    source.close()
    return fileContents.split('\n')
def dictify(listOfStringsOfLines):
    listOfHeadings = listOfStringsOfLines.pop(0).split(',')
    finalDict = {}
    for line in listOfStringsOfLines:
        lineList = line.split(',')
        subDict = {}
        position = 1
        while position < len(lineList):
            subDict[listOfHeadings[position]] = lineList[position]
            position += 1
        finalDict[lineList[0]] = subDict
    return finalDict
def csvToDict(CSVfile):
    return dictify(getStringsOfLines(CSVfile))