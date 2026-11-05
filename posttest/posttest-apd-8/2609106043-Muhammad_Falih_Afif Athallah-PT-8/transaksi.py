from prettytable import PrettyTable
from colorama import Fore
import data
from film import ambil_film


def riwayat_kosong():
    return len(data.riwayat) == 0

def hitung_total(harga, jumlah):
    return harga * jumlah

def tampil_semua_riwayat():
    if riwayat_kosong():
        print(Fore.YELLOW + "Belum ada pembelian.")
    else:
        table = PrettyTable()
        table.field_names = ["User", "Judul", "Jumlah", "Total"]
        for r in data.riwayat:
            table.add_row([r[0], r[1], str(r[2]) + " tiket", "Rp " + str(r[3])])
        print(table)

def tampil_riwayat_saya():
    pembelian = False
    table = PrettyTable()
    table.field_names = ["Judul", "Jumlah", "Total"]
    for r in data.riwayat:
        if r[0] == data.aktif:
            table.add_row([r[1], str(r[2]) + " tiket", "Rp " + str(r[3])])
            pembelian = True
    if not pembelian:
        print(Fore.YELLOW + "Belum ada pembelian")
    else:
        print(table)

def beli_tiket():
    i = input("ID Film : ").strip()
    jml = input("Jumlah Tiket : ").strip()
    try:
        target = ambil_film(i)
        if not jml.isdecimal() or int(jml) <= 0:
            raise ValueError("Jumlah harus angka positif!")
        if int(jml) > target[4]:
            raise ValueError("Kursi tidak cukup! Sisa: " + str(target[4]))
    except KeyError:
        print(Fore.RED + "Film tidak ditemukan!")
    except ValueError as e:
        print(Fore.RED + str(e))
    else:
        total = hitung_total(target[3], int(jml))
        target[4] -= int(jml)
        data.riwayat.append([data.aktif, target[1], int(jml), total])
        print(Fore.GREEN + "Berhasil! Total: Rp " + str(total))
