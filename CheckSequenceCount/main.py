with open("data/t_petrophila_oriC.txt","r+") as file:
    ori = file.read()

print file.closed

print ori



def patternCount(text, word):
    #check how many times a word has occurred in a text.
    # Return the number of count for the pattern
    count = 0
    for i in range(0,len(text)-len(word )+1):
        #print text[i:i+len(word)-1]
        if word == text[i:i+len(word)]:
            count +=1
    return count

def countK(text,k):
    #find the count of all patterns for a specific k.
    # Return a dictionary of all pattern with its count
    count = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        count[text[i:i+k]] = patternCount(text, pattern)
    return count

def findMaxK(text,k):
    #find the max count for a specific k
    #return the max-count pattern and its count
    patterns = countK(text, k)
    key = max(patterns, key=patterns.get)
    value = patterns[key]
    return key, value

def findAllCount(text):
    #find the count for all k
    #return the a list of max count for all k
    count = {}
    for i in range(len(text)):
        mostK = findMaxK(text, i)
        key = mostK[0]
        value = mostK[1]
        count[key] = value
    return count

def printList(list):
    for i in list:
        print len(i), list[i]


printList(findAllCount(ori))


