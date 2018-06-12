import json

from difflib import SequenceMatcher
from difflib import get_close_matches


def LoadDictionary():

    # Load the json from the file object
    data = json.load(open('data.json'))

    return data

# Definitions will be returned as a dictionary with 'word' as the key to a list of definitions
def GetDefinitions(word, data):
    
    definitions = {}

    # Find the definition for the word, else tell the user the word was not found
    if(word in data):
        definitions[word] = data[word]
    else:
        # We didn't find the word. Get a list of close matches and we'll display all of them
        # get_close_matches uses SequenceMatcher to determine a similarity percentage
        close_matches = get_close_matches(word, data.keys(), len(data), cutoff=0.85)

        # If no close matches were found, inform the user
        if(len(close_matches) == 0):
            definitions["Word not found"] = list(["'{0}' was not found in the dictionary".format(word)])
        else:
            for match in close_matches:
                definitions[match] = data[match]

    return definitions

# Display the definition:
# Print the word followed by a number list of definitions
def DisplayDefinitions(definitions):

    for key,value in definitions.items():

        print("{0}: ".format(key))

        for i in range(len(value)):
        # If there are multiple definitions, precede each one with a definition number
            if(len(value) > 1):
                print("{0}. ".format(i+1), end='')

            print("{0}".format(value[i]))


if __name__ == "__main__":

    # Load the dictionary of words and definitions
    data = LoadDictionary()
    print("data.json contains {0} words.".format(len(data)))

    # Obtain the word from the user
    word = input('Enter a word to get the definition: ').lower()
    definitions = GetDefinitions(word, data)

    # Display the definitions
    DisplayDefinitions(definitions)
