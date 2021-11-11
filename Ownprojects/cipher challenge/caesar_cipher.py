from checkWords import checkForEnglish
# message = 'GZQQX' #encrypted message
# message = """SLVVC, XSLNJW OPV CPYV TMLEK, E OPVUPX CPY SLH WQTNX XEMT STVT EN XST LVGSLTPKPUEWXW LNH EX ALW UPPH XP IT VTMENHTH XSLX EX GLN KTLH WPMTASTVT."""
# message = """GZQQX, H ZL ANQDC, ZMC H ZL QDZKKX MNS RTQD VGX H GZUD ADDM DWHKDC SN SGD ZQBGZDNKNFHRSR. CHC H CN RNLDSGHMF SN TORDS RNLDNMD?"""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('ciphertext.txt', 'r', encoding="utf8") as f:
    message = f.read()

message = message.upper()

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
    
    if checkForEnglish(translated):
        print('Key #%s: %s' % (key, translated))

    
