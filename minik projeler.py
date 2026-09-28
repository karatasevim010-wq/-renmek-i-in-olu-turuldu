sifre = "1234"
hak = 3
while hak > 0:
    giris = input("Şifreyi gir: ")
    if giris == sifre:
        print("giriş başarılı")
        break
    else:
        hak -= 1
        print(f"yanlış şifre, {hak} hakkınız kaldı.")
else:
    print("Hakkınız bitti.")

import random

sayi = random.randint(1, 50)
hak = 7
deneme = 0
while hak > 0:
    tahmin = int(input("1-50 arası tahmin et: "))
    deneme += 1
    if tahmin == sayi:
        print(f"tebrikler! {deneme} denemede buldun")
        break
    elif abs(tahmin - sayi) <= 2:
        hak -= 1
        print(f"çok yaklaştın! kalan hak: {hak}")
    else:
        hak -= 1
        print(f"yanlış tahmin, {hak} hakkınız kaldı.")
else:
    print("Hakkınız bitti.")

sayi = int(input("sayi gir: "))
if sayi == 0:
    print("sıfır")
elif sayi % 2 == 0:
    print("çift")
else:
    print("tek")

# Proje 1: Hava Durumu Önerisi
sicaklik = float(input("hava sıcaklığını girin: "))
if sicaklik > 30:
    print("çok sıcak")
elif sicaklik > 20:
    print("hava güzel")
elif sicaklik > 10:
    print("serin hava")
else:
    print("soğuk hava")

# Proje 2: Not Sistemi
puan = int(input("sınav puanı girin (0-100): "))
if puan >= 90:
    print("harf notu: A")
elif puan >= 80:
    print("harf notu: B")
elif puan >= 70:
    print("harf notu: C")
elif puan >= 60:
    print("harf notu: D")
else:
    print("harf notu: F")

# yaş kategorisi belirleme
yas = int(input("yaşinizi girin: "))
if yas < 0:
    print("geçersiz yaş")
elif yas < 13:
    print("çocuk")
elif yas < 20:
    print("genç")
elif yas < 65:
    print("yetişkin")
else:
    print("yasli")

# Proje 5: Günlük Aktivite Önerisi
hava = input("Hava durumu nasıl? (güneşli, yağmurlu, karlı): ").lower()
if hava == "güneşli":
    print("Piknik yapabilirsin!")
elif hava == "yağmurlu":
    print("Evde film izle.")
elif hava == "karlı":
    print("Kardan adam yap!")
else:
    print("Hava durumunu anlayamadım, ama dışarı çık!")
