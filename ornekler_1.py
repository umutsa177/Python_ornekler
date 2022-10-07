from re import L


print("Selam")

print("Selam")
print("Naber")

print("Selam")

if 4 > 1:
 print("Selam")
print("Merhaba")

if 1 > 4:
      print("4")
      print("1")

q = 13
w = None
e = 45.6
r = -61262768768
v = "qwerty"
p = 'fed'
print("q :", type(q))
print("w :", type(w))
print("e :", type(e))
print("r :", type(r))
print("v:", type(v))
print("p :", type(p))
print(r)
y = False
print(w)
print(q, w, e, r, y)
print(q, w, e, r)
r = 12
print(q, w, )
print(" aynı satır")

print(q); print(w); print(e)

q, w, e = 2, 4, 6
print(q, w, e)

c = "asdf"
v = 'qewr'
z = 'a'

print(c, v, z)

k = [1, 2 , 3 , 4 ,5]
h = {q : "agrgag", r:"wasd"}
m = (0, 1, 4, 8)

print("k :", type(k))
print("h :", type(h))
print("m :", type(m))

# "#" bu ifade tek satırlık yorum yapar.

"""
bir den
fazla
yo
rum
satırı
böyle
yapılır.....
"""

'''
bir
den
fazla açıklama satırı işte böyledir.
'''

b = '''asd
sdfgr
sdfgt
sdfgh
'''
print(b)

a = 13
print(type(a))
a = float(13)
print(type(a))
a = str(13)
print(type(a))
class a:
    b = 45

d = a
print(type(a))
print(type(d))
print(d.b)
print(type(d.b))

b = 6
B = 11
print(b, " : ", B)

aze = 55
def ber():
    aze = 17
    print(aze)

ber()
print(aze)


def c():
    global aze
    aze = 10
    print(aze)

c()
print(aze)

a = 5435142357982756574783873867586276
b = 6597541754587681904869168756826*68
print(a*b)

from random import randrange

rastgele_Sayi = randrange(5, 40)
# 5 den 40 ye kadar rastgele sayı üretir

print(rastgele_Sayi)

a = "asdrwyyht"
b = """adsfwgttrwgw
asdfwggw
adsfgrwrg"""
print(a, b)
print(a[0])
print(a[1])
print(b[3])

print("a nın uzuluğu :", len(a))
print("b nin uzuluğu :", len(b))

a = "Balmumu"

if a == "Balmumu":
    print("a balmumuna eşit")

if "bal" in a:
    print("a da bal var")

print("Balmumu".upper())
print("Balmumu".capitalize())

e = 53
d = 105
f = 156
print("a = {} - b = {} - c = {}".format(e, d, f))

a = 'Balikesir\'in tepeleri'
print(a)

a = 'Balikesir\\in tepeleri'
print(a)

print(105 > 552)
print(102 < 533)

a = 1023 > 534
print(a)

print(33 + 4)
print(33 - 4)
print(33 * 4)
print(33 / 4)

print(99 % 6)
print(99 // 6)
print(33 ** 3)

aw = [1, 2, 3, 4, 5, 6]
br= [False, 0.54, -9879545454, None, [1, "ad", 84.45435643545]]

print(aw)
print(br)
print(br[0])
print(br[4][1])

tr = "turkey"
print(tr[1:3])

br[4][1] = [6324, 9964, 6.53243, "zasasthgthtr"]
print(br[4][1])
print(br[4][1][2])

w = [1, 6, 3, 5]
w.append(53)
print(w)

w.pop()
print(w)

w.append(5)
w.remove(6)
print(w)

w.insert(3, 45)
print(w)

print(w.pop())
print(w)

w.clear()
print(w)

listem = ["Armut", "Ayva", "Limon","Şeftali"]

listem.sort()
print(listem)

listem.reverse()
print(listem)

def fonksiyon(n):
  return abs(n - 55)

sayi_listem = [100, 50, 65, 82, 23]
sayi_listem.sort(key=fonksiyon)
print(sayi_listem)

####################################

sayi_listesi = [3, 5, 10, -8, 9, 15, 33, 45, 76, 7657]
w = sayi_listesi
print(w)

sayi_listesi.sort()
print(w)

##############################
sayi_listesi = [34, 53, 105, -84, 92, 151]
a = sayi_listesi.copy()
print(a)

sayi_listesi.sort()
print(a)

degisitirilemezler = ("armut", "hurma", "cilek")
print(degisitirilemezler)

print(degisitirilemezler[1])

sozluk = {
  "marka": "Ford",
  "model": "Fiesta",
  "yil": 2005
}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

sozluk["renk"] = "mavi"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "beyaz"
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])

