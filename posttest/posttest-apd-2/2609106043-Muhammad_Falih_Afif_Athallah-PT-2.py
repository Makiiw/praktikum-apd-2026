makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000
biaya_aplikasi = 5000
nim = 43
kurs_euro = 20456

total_harga = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6

total_bayar = total_harga + biaya_aplikasi

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

rata_rata = total_bayar / len(harga_makanan)

bolean = nim != rata_rata

total_euro = total_bayar / kurs_euro

print("harga makanan 1 : Rp", makanan_1)
print("harga makanan 2 : Rp", makanan_2)
print("harga makanan 3 : Rp", makanan_3)
print("harga makanan 4 : Rp", makanan_4)
print("harga makanan 5 : Rp", makanan_5)
print("harga makanan 6 : Rp", makanan_6)
print("Biaya Aplikasi : Rp", biaya_aplikasi)
print("nim : ", nim)
print("Kurs Euro saat ini : Rp", kurs_euro, " = 1 €")

print("Total Harga : Rp", total_harga)
print("Total Bayar : Rp", total_bayar)
print(f"Rata-rata Harga Makanan : Rp{rata_rata:.2f}")
print("bolean : ", bolean)
print(f"Total Euro : {total_euro:.2f} €")
print("Harga Makanan : ", (harga_makanan[-6:]))
