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

print("makanan_1 : Rp" + str(makanan_1))
print("makanan_2 : Rp" + str(makanan_2))
print("makanan_3 : Rp" + str(makanan_3))
print("makanan_4 : Rp" + str(makanan_4))
print("makanan_5 : Rp" + str(makanan_5))
print("makanan_6 : Rp" + str(makanan_6))
print("Biaya Aplikasi : Rp" + str(biaya_aplikasi))
print("Total Harga : Rp" + str(total_harga))
print("Total Bayar : Rp" + str(total_bayar))
print("nim : ", nim)
print("Kurs Euro saat ini : Rp" + str(kurs_euro) + " = 1 €")
print("bolean : ", bolean)
print(f"Rata-rata Harga Makanan : Rp{rata_rata:.2f}")
print(f"Total Euro : {total_euro:.2f} €")
print("Harga Makanan : ", (harga_makanan[-6:]))