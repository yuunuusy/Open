# 1- "Samsung s5, Samsung s6, Samsung s7, Samsung s8" elamanlarına sahip bir liste oluşturunuz.

telefonlar = "Samsung s5", "Samsung s6", "Samsung s7", "Samsung s8"

#print(Telefonlar)

# 2- Liste kaç elamanlıdır

sonuc = len(telefonlar)

#3- Listenin ilk ve son elemanı nedir?

sonuc = telefonlar[-1]
sonuc = telefonlar[0]

# 4- "Samsung s5" değerini "Samsung s9" değeri ile değiştirin

#telefonlar[0] = "Samsung s9"
sonuc = telefonlar

# "Samsung s6" listenin bir elemanı mıdır?

if "Samsung s6" in telefonlar:
    print("evet")

# 6- Listenin -3 indeksindeki değer nedir?

sonuc= telefonlar[-3]

#7- Listenin ilk 2 elemanını alın.

sonuc = telefonlar[0:2]

#8- Listenin son 2 elemanı yerine "Samsung s9" ve "Samsung s10" değerlerini ekleyin.

#telefonlar[-2] = ["Samsung s9","Samsung s10"]
sonuc = telefonlar

# 9- Listenin üzerine "Iphohe X" ve "Iphone XR" değerlerini ekleyin
#sonuc = telefonlar + ["Iphone X", "Iphone XR"]

#10- Listenin son elemanını silin
del telefonlar [-1]
sonuc = telefonlar







































print(sonuc)