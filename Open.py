#Open parametresi deneme
f = open('yun.txt')
#print(f)
#print(f.read())
"""
>>> f = open("yun.txt")
>>> f.read()
'Yeni stajyer ogrenci\nDop yazÄ±lÄ±m\nAraÅŸtÄ±rma\n\n'
>>> f.read
<built-in method read of _io.TextIOWrapper object at 0x000001A0A9DCA0C0>
>>> f.read()
''
>>> f.seek(0)
0
>>> f.read()
'Yeni stajyer ogrenci\nDop yazilim\nArastÄ±rma'
>>> f.seek(5)
5
>>> f.read()
'stajyer ogrenci\nDop yazilim\nArastirma\nYeni satir'
>>>
>>> 
>>> 
>>> f.seek(0)
0
>>> f.readline()
'Yeni stajyer ogrenci\n'
>>> f.seek(0)
0
>>> f.readlines()
['Yeni stajyer ogrenci\n', 'Dop yazilim\n', 'Arastirma\n', 'Yeni satir']
>>> satirlar = f.readlines()
>>> satirlar
[]
>>> satirlar(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> satirlar = f.readlines()
>>> satirlar
[]
>>> f.seek(0)
0
>>> satir = f.readlines()
>>> satir
['Yeni stajyer ogrenci\n', 'Dop yazilim\n', 'Arastirma\n', 'Yeni satir']
>>> satir(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> satir[0]
'Yeni stajyer ogrenci\n'
>>> satir[1]
'Dop yazilim\n'
>>> f.closed
False
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x000001A0A9DCA0C0>
>>> f.close()
>>> f.closed
True
>>>
"""

