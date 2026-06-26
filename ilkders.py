mesaj = "Merhaba"
mesaj2 = "Dünya"
 
mesaj = mesaj.upper()
print( mesaj)
mesaj=mesaj.lower()
print(mesaj)
mesaj = mesaj.capitalize()
print(mesaj)
print(mesaj.startswith("me"))
print(mesaj.endswith("a"))
print (len(mesaj + mesaj2))
print ("Merhaba" * 10)

isim = "Serhat"
yas = "22"
print ("{} , {} yaşındadır".format(isim,yas))

isim="Serhat"
mesaj="seni seviyorum"
print("{} {} dedi...".format(isim,mesaj))

print(f" {isim} {mesaj} dedi")

#  upper = büyültme 
# lower= küçültme
# capitalize = baş harf büyültme
#len= harf toplamak 
#startswith= metnin hangi harfle basladıgını kontrol etmek 
# endswith=   ""           ""     bıttıgını        "
# "


