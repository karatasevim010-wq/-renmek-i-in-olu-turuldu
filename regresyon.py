import pandas as pd

tablo = pd.DataFrame({
    "Dolar": [30, 32, 34, 36, 38],
    "Altin": [2000, 2100, 2250, 2400, 2500]
}) 

import statsmodels.api as sm 
X = tablo["Dolar"]
Y = tablo["Altin"]
X = sm.add_constant(X) # denklemdeki değeri hesaplar 
model = sm.OLS(Y, X).fit()#pyt. veriye bakıp en uygun regresyon doğrusunu bulur 
print(model.summary()) # sonuçlar gösterilir 

# R**2 NEDİR?
#“Modelimiz, Y'deki değişimin ne kadarını açıklayabiliyor?”
# R**2 = 0.90 ise Modeldeki Dolar değişkeni, Altın'daki değişimin yaklaşık %90'ını açıklıyor.
#      0<R**2>1    R**2 yüksek dye model kesin doğru diyemeyiz 
| Dolar | Altın |
|---:|---:|
| 10 | 690 |
| 11 | 755 |

dolar1 = 10
altin1 = 690

dolar2 = 11
altin2 = 755

# b katsayısını bul
b = (altin2 - altin1) / (dolar2 - dolar1)

# const'ı bul
const = altin1 - b * dolar1

print("b =", b)
print("const =", const)

# R**2 YE ÖRNEK
import statsmodels.api as sm

dolar = [10, 11, 12, 13, 14]
altin = [690, 755, 820, 885, 950]

X = sm.add_constant(dolar)

model = sm.OLS(altin, X).fit()

R2 = model.rsquared

print("R² =", R2)

model.rsquared # "Bu regresyon modelinin R² değerini ver." demek

import statsmodels.api as sm

dolar = [10, 11, 12, 13, 14]
altin = [690, 755, 820, 885, 950]

X = sm.add_constant(dolar) # dolar değişkenine constı ekle 

model = sm.OLS(altin, X).fit() # 2 veri arasındaki regresyon modelini kur 

print("b =", model.params[1])
print("const =", model.params[0])
print("R² =", model.rsquared)
print("p-value =", model.pvalues[1]) 0pşs
# tek seferde hepsini bulduruyor 









