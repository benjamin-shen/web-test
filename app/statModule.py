# module for statistics

def mean(list):
    if len(list) == 0:
    
        return "none"
    return sum(list) / float(len(list))
    
# print mean([1,2])
# print mean([1,2,3])
# print mean([])

def median(list):
    if len(list) == 0:
        return "none"
    
    list.sort()
    if len(list) % 2 == 0:
        x = (len(list) / 2) - 1
        y = len(list) / 2
        c = [list[x], list[y]]
        return mean(c)
    else:
        a = len(list) / 2 # floor
        return list[a]
        
# print median([1,2])
# print median([1,2,3,3])
# print median([])

def mode(list):
    if len(list) == 0:
        return "none"
    
    numberFreq = {}
    for number in list: # [3,4,4,4,5,5,5]
        if not number in numberFreq:
            numberFreq[number] = 0
        numberFreq[number] += 1
    # numberFreq = [3:1,4:3,5:3]
    
    frequencies = numberFreq.values() # [1,3,3]
    mostFrequent = max(frequencies) # 3
    if mostFrequent == 1:
        return "none"
    
    modeList = []
    for key in numberFreq:
        if numberFreq[key] == mostFrequent:
            modeList.append(key)
    
    finalString = ""
    for number in sorted(modeList):
        finalString += str(number) + ", "
    
    return finalString[:len(finalString)-2] # to get rid of final ", "
    
# print mode([1,2,3])
# print mode([1,1,2])
# print mode([1,1,2,2])
# print mode([])

def customMax(list):
    if len(list) == 0:
        return "none"
    return max(list)

def customMin(list):
    if len(list) == 0:
        return "none"
    return min(list)