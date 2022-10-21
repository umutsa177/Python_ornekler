"""
Soru 1
Kendisine gönderilen sayılardan sadece palindrom olanları toplayan, diğerlerini de bu toplamdan çıkaran  ve geri döndüren fonkisyonu yaz.
palindrom = 909 , 888, 121 ...
"""

def palindrom(*dram):
    total = fark = 0
    for sayı in dram:
        if str(sayı) == str(sayı)[::-1]:
            total += sayı
        else:
            total -= sayı
    return total - fark

print(palindrom(10, 101, 55, 40, 9001))

""""""""""""""""""""""""""""""""""""""""""""

class sınıf:
    e = 5
    d = "qwew"
    f = [2, 4, 6]

    def write(self):
        k = 120
        print(k, self.k)

    def write2(self,y):
        self.write()
        print(y)

nesne = sınıf()
nesne.write()
nesne.write2("fwefreq")   # self i görmezden geliyoruz.


obje = sınıf()
print(obje.e)
obje.e = 989
print(obje.e)

def Palamut():{print("asdsefd")}

Palamut()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class qwerty:
    yazı = ""
    def __init__(self, b):
        self.yazı = b

    def __del__(self):
        print("sil")

    def __str__(self):
        return "yazdırılan : " + self.yazı

nesneee = qwerty("Ali")
print(nesneee.metin)

qw = qwerty("CIVA")
print(qw)

""""""""""""""""""""""""""""""""

def num(c, d):
    return c + d

def multiply(c , d):
    return c * d


w = 4
s = "wefı"
r = [0, 5 ,6]
""""""""""""""""""""""""""""""""""""""""""""""""""""""
import ast
from cmath import e
import ornekler_2 as orn

from ornekler_2 import num

print(orn.num(5, 7))
print(orn.e)

print(num(1, 5))

print(orn.e)

#####################################################

a = "wer"
try:
    h = 9 + a
except:
    print("int and string")

#############################

from termcolor2 import termcolor

print(qw("hi").red.on_white.blink.underline.dark)

""""""""""""""""""""""""""""""""""""""""""""""""

dosya = open("metin.txt", "v")

for satır in dosya:
    print(satır[:-1])

gerg = open("metin.txt", "r")
print("villages", file=gerg)

gerg.close()

