liste =[1,2,3,4,5,6]

for rakam in liste: #  for döngüsü listenin içindekileri yazdırdı 
    print(rakam) 

isim="sevim"
for harf in isim: # harfleri yazdırdı
    print(harf)

demet = (1,2,3,4)
for i in demet :
    print(i)

for i in range (1,10): # 1den 10 a kadar yazdırdı 10 dahıl degıl
     print(i)

for i in range (1,17,2) : # 1 başlangıç 17 nereye kadar olduğu 2 şer ritmik sayma
    print(i)

sonuc =1
for i in range (0,10): # döngü 10 kere tekrarlandı 2 ile carpıldı
    sonuc *= 2
    print(sonuc)

liste1=["a","b","c"] # sayı ile harfleri eşleştirecek
liste2=[1,2,3]
for harf in liste1:
    for rakam in liste2:
        print(harf,rakam) 

liste=[1,2,3,4,5,6,7,8,9]
for i in liste:
    if i ==3:
        print("3 ü atladık")
        continue # atla demek 3ü atladı 4ten devam etti
    print(i)     

for i in liste:
    if i ==3:
        print("3 ü atladık")
        break # 3 ü yazmadı devamını kesti 
    print(i) 

liste=range(100)

for i in liste:
    if i %3 != 0: # sadece 3 e bölünen sayıları yazdır
      continue
    if i ==81:# 81 e kadar 3´erli yazdı 81 'i yazmadı 
        break
    print(i) 

x= 2
while x < 10:
    print(x)
    x += 1 
    print("x =" ,x) 

x=2
y=3

while x * y < 1000:
    print (x,y)
    x += 2
    y += 2


i = 1
while True:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    if i == 1000:
        break

