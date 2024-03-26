import random
import string

alphabet = list(string.printable)
cipher_alphabet = alphabet.copy()
random.shuffle(cipher_alphabet)

def encode():
    text = str(input("Bir metin giriniz: "))
    cipher_text = []
    
    for letter in text:
        cipher_text.append(cipher_alphabet[alphabet.index(letter)])
        
    cipher_text = "".join(cipher_text)
    print("girdiğiniz metin: {}".format(text))
    print("şifrelenmiş metin: {}".format(cipher_text)) 


def decode():
    cipher_text = str(input("Bir şifre giriniz: "))
    text = []
    for letter in cipher_text:
        text.append(alphabet[cipher_alphabet.index(letter)])

    text = "".join(text)
    print("girdiğiniz şifre: {}".format(cipher_text))
    print("çözülmüş metin: {}".format(text))