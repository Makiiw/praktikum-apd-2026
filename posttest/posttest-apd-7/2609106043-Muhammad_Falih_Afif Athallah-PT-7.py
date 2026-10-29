import os

user = [["admin", "admin123", "admin"], ["falih", "043", "user"]]
film = [
    [1, "G30S/ISO", "Studio 1", 50000, 75],
    [2, "Herul 1990", "Studio 2", 50000, 70],
    [3, "Finding Falih", "Studio 3", 35000, 100]
]
riwayat = []
id_baru = 4
aktif = ""
role = ""


def film_kosong():
    return len(film) == 0

def riwayat_kosong():
    return len(riwayat) == 0

def ambil_id_baru():
    global id_baru
    hasil = id_baru
    id_baru += 1
    return hasil

def hitung_total(harga, jumlah):
    return harga * jumlah

def cek_login(nama, sandi):
    user_ada = False
    pass_ada = False
    for akun in user:
        if akun[0] == nama:
            user_ada = True
        if akun[1] == sandi:
            pass_ada = True
        if akun[0] == nama and akun[1] == sandi:
            return akun
    if nama == "" and sandi == "":
        raise ValueError("Username dan Password tidak boleh kosong!")
    elif nama == "":
        raise ValueError("Username tidak boleh kosong!")
    elif sandi == "":
        raise ValueError("Password tidak boleh kosong!")
    elif not user_ada and not pass_ada:
        raise ValueError("Username dan Password salah!")
    elif not user_ada:
        raise ValueError("Username salah!")
    raise ValueError("Password salah!")

def cari_film(id_film, i=0):
    if i == len(film):
        return None
    if film[i][0] == id_film:
        return film[i]
    return cari_film(id_film, i + 1)

def ambil_film(teks_id):
    if not teks_id.isdecimal():
        raise KeyError(teks_id)
    hasil = cari_film(int(teks_id))
    if hasil is None:
        raise KeyError(teks_id)
    return hasil

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def jeda(kata="Melanjutkan"):
    input("Tekan Enter untuk " + kata + "...")

def tampil_header_awal():
    print("=" * 70)
    print("KASIR BIOSKOP PALING BAGUS".center(70))
    print("=" * 70)

def tampil_header_menu():
    print("||===== MENU UTAMA =====||".center(70))
    print("User:", aktif, "| Role:", role)

def tampil_daftar_film():
    for f in film:
        print("ID:", f[0], "|", f[1], "|", f[2], "| Rp", f[3], "| Seat:", f[4])
    if film_kosong():
        print("Film Tidak Tersedia!")

def tampil_semua_riwayat():
    for r in riwayat:
        print(r[0], "|", r[1], "|", r[2], "tiket | Rp", r[3])
    if riwayat_kosong():
        print("Belum ada pembelian.")

def tampil_riwayat_saya():
    pembelian = False
    for r in riwayat:
        if r[0] == aktif:
            print(r[1], "|", r[2], "tiket | Rp", r[3])
            pembelian = True
    if not pembelian:
        print("Belum ada pembelian")

def register():
    username_baru = input("Masukkan Username baru   : ").strip()
    password_baru = input("Masukkan Password baru   : ").strip()
    user_ada = False
    for akun in user:
        if akun[0] == username_baru:
            user_ada = True
            break
    try:
        if username_baru == "" and password_baru == "":
            raise ValueError("Username dan Password tidak boleh kosong!")
        elif username_baru == "":
            raise ValueError("Username tidak boleh kosong!")
        elif password_baru == "":
            raise ValueError("Password tidak boleh kosong!")
        elif user_ada:
            raise ValueError("Username sudah digunakan, Silahkan gunakan username lain!")
    except ValueError as e:
        print(e)
    else:
        user.append([username_baru, password_baru, "user"])
        print("Register berhasil!")

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
        print(e)
    else:
        film.append([ambil_id_baru(), judul_baru, studio_baru, int(harga_baru), int(seat_baru)])
        print("Film Berhasil Ditambahkan!")

def ubah_film():
    id_film = input("ID Film : ").strip()
    try:
        f = ambil_film(id_film)
    except KeyError:
        print("ID Film Tidak Ditemukan!")
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
                print(e)
        if berubah:
            print("Film Berhasil Diubah!")
        else:
            print("Tidak ada data yang diubah.")

def hapus_film():
    id_film = input("ID Film : ").strip()
    try:
        film.remove(ambil_film(id_film))
    except KeyError:
        print("Film Tidak Ditemukan!")
    else:
        print("Film Berhasil Dihapus!")

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
        print("Film tidak ditemukan!")
    except ValueError as e:
        print(e)
    else:
        total = hitung_total(target[3], int(jml))
        target[4] -= int(jml)
        riwayat.append([aktif, target[1], int(jml), total])
        print("Berhasil! Total: Rp", total)

def halaman_awal():
    global aktif, role
    while True:
        bersihkan_layar()
        tampil_header_awal()
        print("1. Login\n2. Register\n3. Exit")
        opsi = input("Pilih : ").strip()

        if opsi == "1":
            input_user = input("Masukkan Username   : ").strip()
            input_pass = input("Masukkan Password   : ").strip()
            try:
                akun = cek_login(input_user, input_pass)
            except ValueError as e:
                print(e)
                jeda("melanjutkan")
            else:
                aktif, role = akun[0], akun[2]
                return
        elif opsi == "2":
            register()
            jeda("melanjutkan")
        elif opsi == "3":
            print("Terima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print("Opsi tidak valid, Harus Berupa Angka")
            jeda("melanjutkan")

def halaman_menu():
    while True:
        bersihkan_layar()
        tampil_header_menu()

        if role == "admin":
            print("1. Daftar Film\n2. Tambah Film\n3. Ubah Film\n4. Hapus Film\n5. Semua Riwayat\n6. Log Out")
        else:
            print("1. Daftar Film\n2. Beli Tiket\n3. Riwayat Saya\n4. Log Out")
        menu = input("Pilih : ").strip()

        if menu == "1":
            tampil_daftar_film()
        elif role == "admin" and menu == "2":
            tambah_film()
        elif role == "admin" and menu == "3":
            ubah_film()
        elif role == "admin" and menu == "4":
            hapus_film()
        elif role == "admin" and menu == "5":
            tampil_semua_riwayat()
        elif (role == "admin" and menu == "6") or (role == "user" and menu == "4"):
            print("Log Out berhasil.")
            jeda()
            return
        elif role == "user" and menu == "2":
            beli_tiket()
        elif role == "user" and menu == "3":
            tampil_riwayat_saya()
        else:
            print("Pilihan tidak valid!")
        jeda()

def main():
    while True:
        halaman_awal()
        halaman_menu()

try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan.")
