"""
1 - veri isimli bir klasör oluşturun
2 - zip dsosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini
    tek bir csv dosyasında birleştirin
    volume olmasın
4 - bu kayıtların tamamını sqlite veritabanına bir tablo
    oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""
import os
import zipfile
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()


parite = "AVAXUSDT"  # input("Parite Giriniz :")
begin_date = "2022-02-03"  #  input("Başlangıç Tarihi :")
finish_date = "2022-02-04"  # input("Bitiş Tarihi :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+begin_date+"' " \
        "AND '"+finish_date+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
conclusion = cursor.fetchall()
liste_a = []
liste_b = []
for mum in conclusion:
    #print(mum)
    #print(mum[1])
    liste_b.append(mum[6])
    liste_a.append(mum[2])

plt.plot(liste_a, liste_b)
plt.show()
bag.close()