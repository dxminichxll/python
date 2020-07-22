def cipher(text):
    cipher_text = []
    cipher2 = [char for char in "abcdefghijklmnopqrstuvwxyz\n ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    cipher1 = [char for char in "yzabcdefghijklmnopqrstuvwx\n YZABCDEFGHIJKLMNOPQRSTUVWX"]
    for char in text:
        cipher_letter = cipher1[cipher2.index(char)]
        cipher_text.append(cipher_letter)
    return "".join(cipher_text)

with open('text.txt','r') as file:
    print(cipher(file.read()))
