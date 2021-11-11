from checkWords import checkForEnglish, checkForLanguage
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('ciphertext.txt', 'r') as f:
    ciphertext = f.read()

for key in range(len(LETTERS)):
    translated = ''
    for symbol in ciphertext:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        
        else:
            translated = translated + symbol
    
    if checkForEnglish(translated):
        if checkForLanguage(translated):
            print('Key #%s: %s' % (key, translated))