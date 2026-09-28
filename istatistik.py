# ortalama 
getiri = [5, 10, 15]

ortalama = sum(getiri) / len(getiri)

print(ortalama)
#pandasta ise 
tablo["Getiri"].mean()

# medyan 
import numpy as np

getiri = [3, 5, 7, 9, 100]

np.median(getiri)

# st. sapma (verilerin ne kadar dalgalandığını verir)
getiri = [2, 5, 8, 10, 20]

np.std(getiri)

#korelasyon (-1,+1   +1 e ne kadar yakınsa o kadar güçlü aralarında ilişki vardır )
import pandas as pd

dolar = [10, 11, 12, 13, 14]
altin = [690, 755, 820, 885, 950]

tablo = pd.DataFrame({
    "Dolar": dolar,
    "Altin": altin
})

korelasyon = tablo["Dolar"].corr(tablo["Altin"])

print(korelasyon) 



#p-value 0,1 arasında 0 a ne kadar yakınsa o kadar güçlü p<0.05
from scipy.stats import pearsonr

korelasyon, p_value = pearsonr(
    tablo["Dolar"],
    tablo["Altın"]
)

print(korelasyon)
print(p_value) 

"""p = 0.01 ✅ anlamlı kabul edilir
p = 0.03 ✅ anlamlı kabul edilir
p = 0.05 → kullanılan kurala bağlı
p = 0.20 ❌ anlamlı kabul edilmez
p = 0.80 ❌ anlamlı kabul edilmez"""

# varyans ne kadar dağıldığını ölçer 
getiri = [10, 10, 10, 10, 10]

varyans = np.var(getiri)

print(varyans)  # çıktı 0 olur değerler yakın 

# aykırı değer 
import pandas as pd

# Veri seti
veri = pd.Series([5, 6, 5, 7, 6, 100, 4, 8])

# IQR hesapla
Q1 = veri.quantile(0.25)
Q3 = veri.quantile(0.75)
IQR = Q3 - Q1

# Sınırları hesapla
alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

# Aykırı değerleri bul
aykiri = veri[(veri < alt_sinir) | (veri > ust_sinir)]

# Aykırı değerleri çıkar
temiz_veri = veri[(veri >= alt_sinir) & (veri <= ust_sinir)]

print("Aykırı değerler:")
print(aykiri)

print("\nTemiz veri:")
print(temiz_veri)








