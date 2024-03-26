def bloklara_ayir(metin, blok_uzunlugu=4):
    bloklar = [metin[i:i+blok_uzunlugu] for i in range(0, len(metin), blok_uzunlugu)]
    return bloklar


def encode():
    text = str(input("bir metin giriniz: "))
    key = int(input("bir anahtar giriniz: "))
    
    if not key.is_integer:
        raise "Key için bir sayı bloğu girmelisiniz!"

    key = str(key)

    if len(str(key)) > len(text):
        raise "Key uzunluğu metin uzunluğundan az olmalıdır!"
    if len(str(key)) < 2:
        raise "Şifreleme yapılabilmesi için key uzunluğu en az 2 olmalıdır!"

    if len(text)%len(key) != 0:
        kalan = len(text)%len(str(key))
        eklenecek = len(str(key))-kalan
        text = text + '\x0c'*eklenecek
    

    cipher_text = []
    blocks = bloklara_ayir(text, len(str(key)))

    for word in blocks:
        for i in range(len(key)):
            cipher_text.append(((word[int(key[i])-1])))


    cipher_text = "".join(cipher_text)

    print("girdiğiniz metin:{}".format(text))
    print("şifrelenmiş metin:{}".format(cipher_text))



