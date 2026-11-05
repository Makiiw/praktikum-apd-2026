from prettytable import PrettyTable
from colorama import Fore
import data


def film_kosong():
    return len(data.film) == 0

def cari_film(id_film, i=0):
    if i == len(data.film):
        return None
    if data.film[i][0] == id_film:
        return data.film[i]
    return cari_film(id_film, i + 1)

def ambil_film(teks_id):
    if not teks_id.isdecimal():
        raise KeyError(teks_id)
    hasil = cari_film(int(teks_id))
    if hasil is None:
        raise KeyError(teks_id)
    return hasil

def tampil_daftar_film():
    if film_kosong():
        print(Fore.YELLOW + "Film Tidak Tersedia!")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Judul", "Studio", "Harga", "Seat"]
        for f in data.film:
            table.add_row([f[0], f[1], f[2], "Rp " + str(f[3]), f[4]])
        print(table)

def tambah_film():
    judul_baru = input("Judul  : ").strip()
    studio_baru = input("Studio : ").strip()
    harga_baru = input("Harga  : ").strip()
    seat_baru = input("Seat   : ").strip()
    try:
        if judul_baru == "" or studio_baru == "" or not harga_baru.isdecimal() or not seat_baru.isdecimal():
            raise ValueError("Semua harus diisi, Harga dan Seat harus berupa Angka!!!")
        if int(harga_baru) <= 0 or int(seat_baru) <= 0:
            raise ValueError("Harga dan seat harus lebih dari 0!")
    except ValueError as e:
        print(Fore.RED + str(e))
    else:
        data.film.append([data.ambil_id_baru(), judul_baru, studio_baru, int(harga_baru), int(seat_baru)])
        print(Fore.GREEN + "Film Berhasil Ditambahkan!")

def ubah_film():
    id_film = input("ID Film : ").strip()
    try:
        f = ambil_film(id_film)
    except KeyError:
        print(Fore.RED + "ID Film Tidak Ditemukan!")
    else:
        judul_baru = input("Judul Baru  : ").strip()
        harga_baru = input("Harga Baru  : ").strip()
        berubah = False
        if judul_baru != "":
            f[1] = judul_baru
            berubah = True
        if harga_baru != "":
            try:
                if not harga_baru.isdecimal() or int(harga_baru) <= 0:
                    raise ValueError("Harga tidak valid, harga tidak diubah!")
                f[3] = int(harga_baru)
                berubah = True
            except ValueError as e:
                print(Fore.RED + str(e))
        if berubah:
            print(Fore.GREEN + "Film Berhasil Diubah!")
        else:
            print(Fore.YELLOW + "Tidak ada data yang diubah.")

def hapus_film():
    id_film = input("ID Film : ").strip()
    try:
        data.film.remove(ambil_film(id_film))
    except KeyError:
        print(Fore.RED + "Film Tidak Ditemukan!")
    else:
        print(Fore.GREEN + "Film Berhasil Dihapus!")
