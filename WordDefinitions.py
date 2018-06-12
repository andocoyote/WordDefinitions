import json

from difflib import SequenceMatcher


def LoadDictionary():

    # Load the json from the file object
    data = json.load(open('data.json'))

    return data


def GetDefinition(word, data):
    
    definition = None

    # Find the definition for the word, else tell the user the word was not found
    if(word in data):
        definition = data[word]
    else:
        definition = list(["'{0}' was not found in the dictionary".format(word)])

    return definition


if __name__ == "__main__":

    # Load the dictionary of words and definitions
    data = LoadDictionary()
    print("data.json contains {0} words.".format(len(data)))

    # Obtain the word from the user
    word = input('Enter a word to get the definition: ').lower()
    definition = GetDefinition(word, data)

    # Display the definition
    for i in range(len(definition)):

        # If there are multiple definitions, precede each one with a definition number
        if(len(definition) > 1):
            print("{0}. ".format(i+1), end='')

        print("{0}".format(definition[i]))
