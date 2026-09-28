import random


def sifre_oyunu():
    print("\n--- Şifre Oyunu ---")
    sifre = "1234"
    hak = 3
    while hak > 0:
        giris = input("Şifreyi gir: ")
        if giris == sifre:
            print("Giriş başarılı!")
            return
        hak -= 1
        if hak > 0:
            print(f"Yanlış şifre, {hak} hakkınız kaldı.")
    print("Hakkınız bitti.")


def sayi_tahmin():
    print("\n--- Sayı Tahmin Oyunu ---")
    sayi = random.randint(1, 50)
    hak = 7
    deneme = 0

    while hak > 0:
        try:
            tahmin = int(input("1-50 arası tahmin et: "))
        except ValueError:
            print("Lütfen bir sayı gir.")
            continue

        deneme += 1
        if tahmin == sayi:
            print(f"Tebrikler! {deneme} denemede buldun.")
            return
        elif abs(tahmin - sayi) <= 2:
            hak -= 1
            print(f"Çok yaklaştın! Kalan hak: {hak}")
        else:
            hak -= 1
            print(f"Yanlış tahmin. Kalan hak: {hak}")

    print(f"Hakkınız bitti. Doğru sayı: {sayi}")


def cift_tek():
    print("\n--- Çift / Tek Kontrolü ---")
    try:
        sayi = int(input("Sayı gir: "))
    except ValueError:
        print("Geçersiz sayı.")
        return

    if sayi == 0:
        print("Sıfır")
    elif sayi % 2 == 0:
        print("Çift")
    else:
        print("Tek")


def hava_durumu():
    print("\n--- Hava Durumu Önerisi ---")
    try:
        sicaklik = float(input("Hava sıcaklığını girin (°C): "))
    except ValueError:
        print("Geçersiz sıcaklık.")
        return

    if sicaklik > 30:
        print("Çok sıcak — bol su iç, gölgede kal.")
    elif sicaklik > 20:
        print("Hava güzel — dışarı çıkabilirsin.")
    elif sicaklik > 10:
        print("Serin hava — hafif bir ceket al.")
    else:
        print("Soğuk hava — kalın giyin.")


def not_sistemi():
    print("\n--- Not Sistemi ---")
    try:
        puan = int(input("Sınav puanı girin (0-100): "))
    except ValueError:
        print("Geçersiz puan.")
        return

    if puan < 0 or puan > 100:
        print("Puan 0 ile 100 arasında olmalı.")
        return

    if puan >= 90:
        print("Harf notu: A")
    elif puan >= 80:
        print("Harf notu: B")
    elif puan >= 70:
        print("Harf notu: C")
    elif puan >= 60:
        print("Harf notu: D")
    else:
        print("Harf notu: F")


def yas_kategorisi():
    print("\n--- Yaş Kategorisi ---")
    try:
        yas = int(input("Yaşınızı girin: "))
    except ValueError:
        print("Geçersiz yaş.")
        return

    if yas < 0:
        print("Geçersiz yaş")
    elif yas < 13:
        print("Çocuk")
    elif yas < 20:
        print("Genç")
    elif yas < 65:
        print("Yetişkin")
    else:
        print("Yaşlı")


def aktivite_onerisi():
    print("\n--- Günlük Aktivite Önerisi ---")
    hava = input("Hava durumu nasıl? (güneşli, yağmurlu, karlı): ").lower().strip()

    if hava == "güneşli":
        print("Piknik yapabilirsin!")
    elif hava == "yağmurlu":
        print("Evde film izle.")
    elif hava == "karlı":
        print("Kardan adam yap!")
    else:
        print("Hava durumunu anlayamadım, ama dışarı çık!")


def hesap_makinesi():
    print("\n--- Hesap Makinesi ---")
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        islem = input("İşlem seçin (+, -, *, /): ").strip()
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Geçersiz sayı.")
        return

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            print("Hata: Sıfıra bölme yapılamaz!")
            return
        sonuc = sayi1 / sayi2
    else:
        print("Geçersiz işlem!")
        return

    print(f"Sonuç: {sonuc}")


def not_ortalamasi():
    print("\n--- Not Ortalaması ---")
    ad = input("Adını gir: ").strip() or "Öğrenci"

    vize_str = input("Vize notunu gir (0-100): ")
    while not vize_str.isdigit() or int(vize_str) < 0 or int(vize_str) > 100:
        print("Hata: 0 ile 100 arasında bir sayı gir.")
        vize_str = input("Vize notunu tekrar gir (0-100): ")
    vize = int(vize_str)

    final_str = input("Final notunu gir (0-100): ")
    while not final_str.isdigit() or int(final_str) < 0 or int(final_str) > 100:
        print("Hata: 0 ile 100 arasında bir sayı gir.")
        final_str = input("Final notunu tekrar gir (0-100): ")
    final = int(final_str)

    ortalama = vize * 0.4 + final * 0.6
    print(f"{ad}, ortalaman: {ortalama:.1f}")

    if ortalama >= 50:
        print("Sonuç: Geçtin")
    else:
        print("Sonuç: Kaldın")


def menu_goster():
    print("\n" + "=" * 35)
    print("   Python Mini Uygulama")
    print("=" * 35)
    print("1.  Şifre oyunu")
    print("2.  Sayı tahmin oyunu")
    print("3.  Çift / tek kontrolü")
    print("4.  Hava durumu önerisi")
    print("5.  Not sistemi")
    print("6.  Yaş kategorisi")
    print("7.  Aktivite önerisi")
    print("8.  Hesap makinesi")
    print("9.  Not ortalaması")
    print("0.  Çıkış")
    print("=" * 35)


def main():
    islemler = {
        "1": sifre_oyunu,
        "2": sayi_tahmin,
        "3": cift_tek,
        "4": hava_durumu,
        "5": not_sistemi,
        "6": yas_kategorisi,
        "7": aktivite_onerisi,
        "8": hesap_makinesi,
        "9": not_ortalamasi,
    }

    print("Hoş geldin! Mini projelerin tek uygulamada.")

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim == "0":
            print("Görüşürüz!")
            break

        islem = islemler.get(secim)
        if islem:
            islem()
        else:
            print("Geçersiz seçim, tekrar dene.")


if __name__ == "__main__":
    main()
