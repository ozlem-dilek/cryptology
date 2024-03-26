def kaydirmali():
    alp = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    metin = input("metin giriniz: ")
    sayi = int(input("sayi: "))
    while sayi > 28:
        sayi = sayi-28
        
    sifrelenmismetin = ""

    for harf in metin.upper():
        yeniAlp = alp[sayi:] + alp[:sayi]
        harf = yeniAlp[alp.find(harf)] if (alp.find(harf) + sayi) < 29 else yeniAlp[(27 - (alp.find(harf)+ sayi))]
        sifrelenmismetin = sifrelenmismetin + harf
        
    print("girilen metin: ", metin)
    print("şifrelenmiş metin: ", sifrelenmismetin)

kaydirmali()