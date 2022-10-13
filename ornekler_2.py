"""
1- Klavyeden girilen 5 tane sayıyı bir listeye atarak bunların 
karelerinden 20 çıktığında ortaya çıkan sonuca göre sıralayan 
ve listeyi buna göre yazdıran programı yazınız.
"""

from ast import While
from cmath import sqrt
from tokenize import triple_quoted

q = []

def siralama(n):
  return n*n - 20

for i in range(0, 5):
    q.append(eval(input()))


q.sort(key=siralama)
print(q)

##############################################

q = 3
x = 6
a = -5

if x > a:
    print("x, a'dan büyüktür")

if a < 0: print("a, 0'dan küçüktür")

if a > 0: print("wfhefaeofjşm"); print("fregreg"); w= 12

##############################################

z = 45

if z > 34:
    print("z, 34'ten büyüktür")
elif z == 45:
    print("z 45 e esittir")
else:
    print("z 45 e eşit değildir.")

""""""""""""""""""""""""""""""""""""""""""""""""""""""

f = 0 
v = 6
print("f ve v  farklı") if f != v else print("f ile v aynı")

e = 5
u = 10
m = -7

if a < 10 or u < 10:
    print("a yada u 10 dan küçük")

if a == 10 or u == 10:
    print("a 10 a eşit ve u 10 a eşit")

t = 4 
if t is 4:
    print("t 4 e eşit")

if t is not 4:
    print("t 4 e eşit değil")

#############################################

s = 7 
p = 12
if s < 8:
    if p > 10:
        print("MERHABA")

""""""""""""""""""""""""""""""""""""""""""

ö = 4

if ö > 3:
    pass
print("nfekfaslkjfla")

ğ = 18
while ğ < 25:
    ğ += 1
    if ğ == 20:
        continue
    if ğ == 25:
        break
    print(ğ)

else:
    print("ğ artık daha büyük")


""""""""""""""""""""""""""""""""""""""""""

for x in range(3,12):
    print(x)

for i in range(0, 10, 3):
    print(i)

for ş in range(20, 8, -3):
    print(ş)

listem = ["adds", True, 3.4, 7, ["freg", "gsrgsfg", "nwynsj"]]

for n in listem:
    print(n)

for ü in listem[4]:
    print(ü)

for p in range(0, 4):
    print(p)

for ç, eleman in enumerate(listem):
    print(ç+1, ". eleman : ", sep="")

##########################################################

def write():
    print("I am writing.")

write()

def numandmultiply(c,d):
    return c + d, c * d

num, multiply = numandmultiply(4,7)
print(numandmultiply(4,7))
print(num, multiply)

def all_num(*a):
    total = 0
    for value in a:
        total += a
    return total

print(all_num(3, 5, 7, 78, 2, 1, -345))


def topla(*toplanacak, fazlalık=0):
    total = 0
    for value in toplanacak:
        total += value + fazlalık
    return total

print(topla(3, 5, 7, 78, 2, 1,fazlalık= -345))

###########################################################

def br_işlem(**birim):
    print("ad : ", type(birim))
    print("ad : " + birim["ad"])
    print("yıl : ", birim["yıl"])
    print("tipi : ", birim["tip"])

br_işlem(ad="qew",yıl="2003",tip="asdw")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lambda_fonk = lambda v : v + 15 

print(lambda_fonk(7))

toplam= lambda c, d: c+ d

print(toplam(5,98))

def my_fuction(x):
    return lambda x: x * n


katını_al = my_fuction(3)
print(katını_al(5))

katını_al = my_fuction(5)
print(katını_al(5))

