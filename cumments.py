import pandas
import random

#create data object from json
df = pandas.read_json('comments.json', lines=True)


def parseCumment(df):
    '''
    Input is a pandas json object, generates a list of words from a random set of 50 comments
    '''
    counter = 0 
    wordList = []

    while counter < 50:

        cumment = df.text[random.randint(0,len(df))]
        splitValue = cumment.split()
        for word in splitValue:
            #handle weird ass unicode characters
            try:
                word.encode('ascii')
                wordList.append(word)
            except UnicodeEncodeError: 
                pass
        counter += 1 

    return wordList

out = parseCumment(df)

newSentence = []
counter = 0 
while counter < 15:
    newWord = out[random.randint(0,len(out))]
    newSentence.append(newWord)
    counter += 1

print(' '.join(newSentence))
