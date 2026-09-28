Şirket	Fiyat
ASELSAN	100
THYAO	250
TUPRS	180

import matplotlib.pyplot as plt

şirketler = ["ASELSAN", "THYAO", "TUPRS"]
fiyatlar = [100, 250, 180]

plt.bar(şirketler, fiyatlar) # çubuk grafiği gösterir
plt.plot(şirketler, fiyatlar)# çizgi graf. gösterir
plt.show()

#import matplotlib.pyplot as plt → Matplotlib'i kullanıma açıyoruz.
#şirketler → grafiğin isimleri
#fiyatlar → grafiğin değerleri
#plt.bar() → çubuk grafik oluştur
#plt.show() → grafiği ekranda göster
#plt.plot() → çizgi grafik

plt.plot(gunler, fiyat)

plt.title("Hisse Fiyatı")
plt.xlabel("Gün")
plt.ylabel("Fiyat")

plt.show()
#plt.title() → grafiğin başlığı
#plt.xlabel() → X ekseninin adı
#plt.ylabel() → Y ekseninin adı

 















