# kendi fonksiyon denemelerin (düzeltilmiş)
# çalıştır:  python3 fonksiyon_deneme.py

def selamla_isim(isim):
    print("Merhaba", isim)


selamla_isim("Sevim")  # fonksiyonu çağırıyoruz


def carp(a, b):
    return a * b  # return ile fonksiyonun sonucunu döndürüyoruz


sonuc = carp(5, 3)  # çağrı fonksiyonun DIŞINDA olmalı
print(sonuc)


def topla(sayi1, sayi2):  # birden fazla parametre virgülle yazılır
    return sayi1 + sayi2


sonuc = topla(5, 8)
print(sonuc)


# input + fonksiyon birlikte
sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("İkinci sayı: "))

sonuc = topla(sayi1, sayi2)
print(sonuc)


def kontrol(sayi):  # fonksiyon + if/else
    if sayi > 10:
        return "Büyük"
    else:
        return "Küçük"


sonuc = kontrol(7)
print(sonuc)


# sözlük ayrı konu; karışmasın diye burada kısa örnek
sirket = {
    "isim": "ASELSAN",
    "fiyat": 85,
    "sektor": "Savunma",
}
print(sirket["fiyat"])
