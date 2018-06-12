import json

from difflib import get_close_matches


def LoadDictionary():

    # Load the json from the file object
    data = json.load(open('data.json'))

    return data

# Definitions will be returned as a dictionary with 'word' as the key to a list of definitions
# Return the dictionary of definitions and boolean of whether the exact word was found
def GetDefinitions(word, data):
    
    definitions = {}
    word_found = False

    # Find the definition for the word, else tell the user the word was not found
    if(word in data):
        definitions[word] = data[word]
        word_found = True
    # Maybe the word is a proper name or place such as Delhi
    elif(word.title() in data):
        definitions[word.title()] = data[word.title()]
        word_found = True
    # Maybe the word is an acronym such as USA
    elif(word.upper() in data):
        definitions[word.upper()] = data[word.upper()]
        word_found = True
    else:
        # We didn't find the word. Get a list of close matches and we'll display all of them
        # get_close_matches uses SequenceMatcher to determine a similarity percentage
        close_matches = get_close_matches(word, data.keys(), len(data), cutoff=0.85)

        # If no close matches were found, inform the user
        for match in close_matches:
            definitions[match] = data[match]

    return definitions,word_found

# Display the definition:
# Print the word followed by a number list of definitions
def DisplayDefinitions(word, definitions, word_found):

    if(not word_found and len(definitions) == 0):
        print("Word not found: '{0}' was not found in the dictionary".format(word))
    else:

        if(not word_found):
            print("'{0}' was not found.  Here are similar word(s):".format(word))

        for key,value in definitions.items():

            # Display the word
            print("{0}: ".format(key))

            for i in range(len(value)):
                # Precede each definition with a definition number
                print("{0}. {1}".format(i+1, value[i]))


if __name__ == "__main__":

    word_found = False

    # Load the dictionary of words and definitions
    data = LoadDictionary()
    print("data.json contains {0} words.".format(len(data)))

    # Obtain the word from the user
    word = input('Enter a word to get the definition: ').lower()

    # Obtain the definition and boolean of whether the exact word was found
    definitions,word_found = GetDefinitions(word, data)

    # Display the definitions for the word
    DisplayDefinitions(word, definitions, word_found)
