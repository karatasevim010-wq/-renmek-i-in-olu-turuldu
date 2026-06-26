kisi= {"isim":"serhat", "yas":22, "cinsiyet":"m","hobiler":[" kv ", " pc"," yazılım "]}
print(kisi)
print(kisi["isim"])
print(kisi["yas"])
print(kisi["hobiler"])

print(kisi)
kisi["isim"]="sevim"#isim değiştirmek 

print(kisi)
kisi.update({"isim":"sevim","yas":19}) # birden fazla değişir 
print(kisi)

print(kisi)
kisi["id"]=12345 #listeye herhangi birşey eklemek 
print(kisi)
del kisi["id"] # listeden herhangi birşey silmek
print(kisi)

for x in kisi:# anahtarları yazdırdı
 print(x)

for x in kisi: #değerleri yazdırdık
 print(kisi[x]) 

print(kisi.keys()) # sadece anahtarlar yazdırılır 

print(kisi.values()) # sadece değerleri alır 
print(kisi.items()) # anahtar + değer

for k in kisi.items(): # anahtar+ değer alt alta yazdırır
 print(k) 

print(kisi["id"]) #id sözlükte yok hata verir
print(kisi.get("id"))# id sözlükte yok hata vermez


