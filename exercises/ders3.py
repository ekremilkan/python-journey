ne_kadar = float(input("Urun ne kadar? "))

if ne_kadar >= 500:
    print("Buyuk harcama!")
elif ne_kadar == 0 or ne_kadar < 0:
    print("Gecersiz tutar")
elif ne_kadar < 100:
    print("Kucuk harcama.")
else:
    print("Orta harcama.")
