from PyDictionary import PyDictionary
dictionary = PyDictionary()

def get_meaning(word):
    meaning = dictionary.meaning(word)
    if meaning:
        result = ""
        for key, values in meaning.items():
            result += f"{key}: {', '.join(values[:2])}\n"
        return result
    else:
        return "Sorry, I could not find the meaning."

def get_synonym(word):
    synonyms = dictionary.synonym(word)
    if synonyms:
        return f"Synonyms of {word}: {', '.join(synonyms[:5])}"
    else:
        return "Sorry, I could not find synonyms."

def get_antonym(word):
    antonyms = dictionary.antonym(word)
    if antonyms:
        return f"Antonyms of {word}: {', '.join(antonyms[:5])}"
    else:
        return "Sorry, I could not find antonyms."
