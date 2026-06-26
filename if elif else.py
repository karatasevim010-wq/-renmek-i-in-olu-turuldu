if False: # false yanlış olduğu için komutu yazmadı true olsaydı komutu olduğu gibi yazardi 
    print("koşul doğru")
    print("halen if bloğunun içindeyiz")

a = 6
b = 6
if a == b: 
  print("a = b")
else:
  print("a!=b")


renk="siyah"
if renk=="beyaz":
 print("beyaz")
elif renk=="sari":
 print("sari")
elif renk=="mavi":
 print("mavi")
else:
 print("hiçbiri")

a=5
b=8
c=10
if a > b or c < a or b >a: # or yerıne and kullanılsaydı iki koşulundadoğru olması gerekıyor
 print("koşul doğru")
else:
 print("koşul yanlış")
  
liste=[1,2,3,4,5,6,7,8,9]
a= 4 and 10 #  ,

isim ="sevim"
a="S"
if a in isim: #listenin içinde 4 var mı 
 print("listede var")
else:
 print("listede yok")
 # if a yerine if not yazsaydık üstekı degıl alttakı else çalışırdı
  
a=8
b=10
if not a == b : # normalde a b ye eşit değil ama not geldığı için doğru sayılıyor
  print("koşul doğru")
else:
  print("koşul yanlış") 

a ="python"
b="pytho"
b+="n"
print(a)
print(b) 

if a  is  b: # is anahtarında hafızada aynı nesne olmalı is yerine ==konsaydı  = olan çalışırdı 
    print("a=b")
else:
    print("a!=b")
    