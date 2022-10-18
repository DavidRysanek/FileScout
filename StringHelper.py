def filterStringsWithMinLength(strings, minLength):
    filteredStrings = [x for x in strings if len(x) >= minLength]
    return filteredStrings


def findLongestString(strings):
    maxLength = 0
    longestString = ""
    
    for s in strings:
        if (len(s) > maxLength):
            maxLength = len(s)
            longestString = s

    return longestString