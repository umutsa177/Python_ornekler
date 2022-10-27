import csv

with open("metin_2.txt", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row["species"])

baslik = ["nem", "basınc", "sıcaklık"]
veri = [[23.4, 43.4, 10], [32.1, 58, 3]]

with open("veri.csv", "w", encoding="UTF8", newline="") as e:
    writer = csv.writer(e)
    writer.writerow(baslik)
    writer.writerows(veri)

