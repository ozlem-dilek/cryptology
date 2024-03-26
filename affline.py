def affline():
    alp = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    #(ax+b)%n
    a = int(input("ax+b için a değerini giriniz: "))
    b = int(input("ax+b için b değerini giriniz: "))
    n = len(alp)

    metin = input("şifrelenecek metini giriniz: ")
    sifrelenmismetin = ""

    for harf in metin.upper():
        x = alp.index(harf)
        yeniHarf = alp[int((a*x+b)%n)]
        sifrelenmismetin = sifrelenmismetin + yeniHarf

    print("şifrelenmiş metin: ", sifrelenmismetin)


affline()