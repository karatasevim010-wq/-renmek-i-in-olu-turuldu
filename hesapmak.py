# Basit hesap makinesi

def hesapla(sayi1, sayi2, islem):
    if islem == '+':
        return sayi1 + sayi2
    elif islem == '-':
        return sayi1 - sayi2
    elif islem == '*':
        return sayi1 * sayi2
    elif islem == '/':
        if sayi2 == 0:
            return "Hata: Sıfıra bölme yapılamaz!"
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem!"

# Kullanıcıdan veri al
print("Basit Hesap Makinesi")
sayi1 = float(input("Birinci sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı girin: "))

# Hesapla ve sonucu göster
sonuc = hesapla(sayi1, sayi2, islem)
print("Sonuç:", sonuc)
