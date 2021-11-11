from langdetect import detect
from textblob import TextBlob
# class CheckEnglish():
    
#     def __init__(self, wordsToCheck):

#         self.wordsToCheck = wordsToCheck

def checkForEnglish(wordsToCheck, sensitivity=5):


    wordsToCheck = wordsToCheck.lower()

    with open('englishWords.txt') as word_file:
        valid_words = set(word_file.read().split())

    realWordList = []
    for word in wordsToCheck.split():
        if word in valid_words:
            if len(word) > sensitivity:
                realWordList.append(word)
    
    return realWordList

def checkForLanguage(wordsToCheck):
    if len(wordsToCheck) > 100:
        return detect(wordsToCheck)
    else:
        return TextBlob(wordsToCheck).detect_language()
        
