def mySezar():
    alp = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    metin = input("metin giriniz: ")
    sifrelenmismetin = ""

    for harf in metin.upper():
        harf = alp[alp.find((harf)) + 3] if (alp.find((harf)) + 3)<30 else alp[(27 - (alp.find(harf) )+ 3)]
        sifrelenmismetin = sifrelenmismetin + harf
        
    print("girilen metin: ", metin)
    print("şifrelenmiş metin: ", sifrelenmismetin)

mySezar()