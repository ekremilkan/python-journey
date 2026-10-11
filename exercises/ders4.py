while True:
    girdi = input("1) Selam ver, 2) Iki sayiyi topla, 3) Cikis, Secimin nedir? ")
    if girdi == "1":
        print("Selam Ekrem!")
    elif girdi == "2":
        sayi1 = int(input("ilk sayiyi gir. "))
        sayi2 = int(input("ikinci sayiyi gir. "))
        print(f"Girdigin sayilarin toplami {sayi1 + sayi2}")
    elif girdi == "3":
        print("Gorusuruz!")
        break
    else: 
        print("Gecersiz secim, tekrar dene.")
