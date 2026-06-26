# liste nedir nasıl oluşturulur?
# liste nasıl yazdırılır?
# len fonk. nedir?
# liste elemanlarına nasıl erişilebilir?
# liste nasıl parçalanır?


renkler=["siyah","beyaz","sarı","mavi","yeşil"]

print(renkler)
print(len(renkler))
print (renkler[0])
print (renkler [1:4])
print(renkler[1:])
print(renkler[0:])
print(renkler[::2])
print (renkler[::5])

#append metodu = listeye yeni eleman eklemek
#insert metodu= elemanı nereye eklemek 
#remove metodu=listeden eleman silmek
#extend metodu =listeye birden fazla eleman eklemek 
#pop metodu= en son elemanı siler 
#reverse metodu = listeyi tersine döndürür
#sort metodu= listeyi  alfabetik sıralıyor 
#sorted  metodu =liste bozulmadan sıralamak

renkler = ["siyah", "beyaz" , "sari" , "mavi", "yeşil"]

rint(renkler)

renkler.insert(2,"Gri")

print(renkler)

renkler.append("gri")

renkler.remove("sari")

print(renkler)

renkler2=("turuncu" , "pembe")
renkler.extend(renkler2)
print(renkler)

silinen=renkler.pop()
print(renkler)
print(silinen)


print(renkler)
renkler.reverse()
print(renkler)

print(renkler)
renkler.sort()
renkler.reverse() # sıralamayı tersten yapar.
renkler.sort(reverse=True) # sıralamayı tersten yapar.
print(renkler)

print(renkler)
liste2=sorted(renkler)
print(liste2)
print(renkler)

# min,max ve in kullanımı
#sum kullanımı = toplar
#for döngüsü ile liste yazdırmak
#enumerate= listeyi numaralandırır
#listeyi stringe çevirmek ve joiin metodu
#stringi listeye çevirmek ve split metodu

renkler=["siyah","beyaz","sari","mavi","yeşil"]


sayilar=[1,2,39,4,3,7,8]

print(min(renkler))

print(max(sayilar))

print(sum(sayilar))

for renk in renkler:
    print (renk)

for sayi in sayilar:
    print(sayi)

print(list(enumerate(renkler)))
print(list(enumerate(renkler,start=1)))

print("siyah"in renkler) # listede siyah renk var mı

stringrenkler="-".join(renkler)
print(type(stringrenkler)) # liste stringe döndü
print(stringrenkler)

renkler2 = stringrenkler.split("-")
print(renkler2)


# tuple(demet) nedir? = listenin benzeri 
#farkı demete herhangi bir eleman ekleyip çıkaramazsınız 114.satır örnek



demet=("sari","mavi","yeşil","kirmizi","siyah")

print(len(demet)) #kaç eleman olduğunu gösterir
print(demet)      #listeyi olduğu gibi yazdırır 
for renk in demet: #altına 'print(renk)' yazarsan renkleri teker teker yazar
  demet[2]="pembe" 

# küme nedir ve nasıl tanımlanır?
# kümeleri yazdırma
# kümelerle eleman ekleme - silme ?
# remove ve discard metotlarının farkı 

kume={"sari","mavi","yeşil","kirmizi","siyah"}
print(type(kume)) 
print(len(kume)) 
print(kume)
for renk in kume :  # kümeyi alta alta dizdi 
    print(renk) 

print(kume)

kume.add("pembe") # kümeye pembe eklendi
print(kume)
#add yerine remove yazsaydık istediğin rengi silerdik
# discard  da siler ancak kümede o eleman yoksa hata vermeden kodu çalıştırır 

#kümelerde kesişim ve birleşim
#kümelerde fark işlemi 
#in anahtar kelimesi 


kume1={"sari","mavi","yeşil","kirmizi","siyah"}
kume2={"sari","mavi","yeşil","beyaz","gri"}

print(kume1.difference(kume2))
#intersection ortak yazdırma
#union 'u kullanırsan birleştirirsin
#difference farklı olanı bulur 

print ("sari" in kume1)
#1.kümede sari rengi var mı
print("beyaz" in kume1.union(kume2))
#kumelerın birleşiminde beyaz var mı

bosliste1=[]
bosliste2=list()

bosdemet1=()
bosdemet2=tuple()

boskume1= set()

python=set("python")
print(python)
# set elemanlara parçalar ve bir kumede birleştirir
