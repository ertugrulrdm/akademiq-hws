faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz"))
print(type(vade))
print(vade + 12)

print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = input("İsminizi giriniz: ")
metin = "Merhaba {name}".format(name=isim)
print(metin)

metin = f"Hoşgeldiniz {1+1}"
print(metin)


dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)



for i in range(5,11):
    print(i)

for i in range(0,51,10):
    print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

for i in range(3):
    print(krediler[i])

i = 0
while i < 10:
    print("x")
    i += 1

while True:
    print("X")
    break

i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1
    print(i)
    if krediler[i] == "Konut Kredisi":
        break



fiyat = 100
indirim = 20

def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Ertugrul")

def calculateAndReturn(fiyat,indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(fonk1)
print(fonk2)
# print(f"159.satır: {fonk1 + 100}")
print(f"160.satır: {fonk2+100}")

###