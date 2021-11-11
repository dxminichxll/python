# message = 'GZQQX' #encrypted message
from langdetect import detect
from checkWords import checkForEnglish
# message = """SLVVC, XSLNJW OPV CPYV TMLEK, E OPVUPX CPY SLH WQTNX XEMT STVT EN XST LVGSLTPKPUEWXW LNH EX ALW UPPH XP IT VTMENHTH XSLX EX GLN KTLH WPMTASTVT."""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translatedList = []

with open('ciphertext.txt', 'r', encoding="utf8") as f:
    message = f.read()


for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        
        else:
            translated = translated + symbol
    
    # print('Key #%s: %s' % (key, translated))

    translatedList.append(translated)

for translated in translatedList:
    for key in range(len(LETTERS)):
        translated2 = ''
        for symbol in translated:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated2 = translated2 + LETTERS[num]
            
            else:
                translated2 = translated2 + symbol
        # print(detect(translated2))
        if checkForEnglish(translated2):
            with open('checkForEnglish.txt', 'a') as f:
                f.write('First key: #%s Second Key #%s: %s' % (translatedList.index(translatedList[translatedList.index(translated)]), key, translated2))
            
            print('First key: #%s Second Key #%s: %s' % (translatedList.index(translatedList[translatedList.index(translated)]), key, translated2))
