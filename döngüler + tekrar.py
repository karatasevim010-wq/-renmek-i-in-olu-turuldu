print("Mini Alistirma: Not Ortalamasi")

ad = input("Adini gir: ")

vize_str = input("Vize notunu gir (0-100): ")
while not vize_str.isdigit() or int(vize_str) < 0 or int(vize_str) > 100:
    print("Hata: 0 ile 100 arasinda bir sayi gir.")
    vize_str = input("Vize notunu tekrar gir (0-100): ")
vize = int(vize_str)

final_str = input("Final notunu gir (0-100): ")
while not final_str.isdigit() or int(final_str) < 0 or int(final_str) > 100:
    print("Hata: 0 ile 100 arasinda bir sayi gir.")
    final_str = input("Final notunu tekrar gir (0-100): ")
final = int(final_str)

ortalama = vize * 0.4 + final * 0.6

print(f"{ad}, ortalaman: {ortalama}")

if ortalama >= 50:
    print("Sonuc: Gectin")
else:
    print("Sonuc: Kaldin")
