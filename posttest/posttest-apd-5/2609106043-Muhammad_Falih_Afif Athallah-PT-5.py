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

while True:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("KASIR BIOSKOP PALING BAGUS".center(70))
        print("=" * 70)
        print("1. Login\n2. Register\n3. Exit")
        opsi = input("Pilih : ").strip()

        if opsi == "1":
            input_user = input("Masukkan Username   : ").strip()
            input_pass = input("Masukkan Password   : ").strip()
            berhasil = False
            user_ada = False
            pass_ada = False
            for akun in user:
                if akun[0] == input_user:
                    user_ada = True
                if akun[1] == input_pass:
                    pass_ada = True
                if akun[0] == input_user and akun[1] == input_pass:
                    aktif, role, berhasil = akun[0], akun[2], True

            if berhasil:
                break
            elif input_user == "" and input_pass == "":
                print("Username dan Password tidak boleh kosong!")
            elif input_user == "":
                print("Username tidak boleh kosong!")
            elif input_pass == "":
                print("Password tidak boleh kosong!")
            elif not user_ada and not pass_ada:
                print("Username dan Password salah!")
            elif not user_ada:
                print("Username salah!")
            else:
                print("Password salah!")
            input("Tekan Enter untuk melanjutkan...")

        elif opsi == "2":
            username_baru = input("Masukkan Username baru   : ").strip()
            password_baru = input("Masukkan Password baru   : ").strip()
            user_ada = False
            for akun in user:
                if akun[0] == username_baru:
                    user_ada = True
                    break

            if username_baru == "" and password_baru == "":
                print("Username dan Password tidak boleh kosong!")
            elif username_baru == "":
                print("Username tidak boleh kosong!")
            elif password_baru == "":
                print("Password tidak boleh kosong!")
            elif user_ada:
                print("Username sudah digunakan, Silahkan gunakan username lain!")
            else:
                user.append([username_baru, password_baru, "user"])
                print("Register berhasil!")
            input("Tekan Enter untuk melanjutkan...")

        elif opsi == "3":
            print("Terima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print("Opsi tidak valid, Harus Berupa Angka")
            input("Tekan Enter untuk melanjutkan...")
            
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("||===== MENU UTAMA =====||".center(70))
        print("User:", aktif, "| Role:", role)

        if role == "admin":
            print("1. Daftar Film\n2. Tambah Film\n3. Ubah Film\n4. Hapus Film\n5. Semua Riwayat\n6. Log Out")
        else:
            print("1. Daftar Film\n2. Beli Tiket\n3. Riwayat Saya\n4. Log Out")
        menu = input("Pilih : ").strip()

        if menu == "1":
            for f in film:
                print("ID:", f[0], "|", f[1], "|", f[2], "| Rp", f[3], "| Seat:", f[4])
            if len(film) == 0:
                print("Film Tidak Tersedia!")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "admin" and menu == "2":
            judul_baru = input("Judul  : ").strip()
            studio_baru = input("Studio : ").strip()
            harga_baru = input("Harga  : ").strip()
            seat_baru = input("Seat   : ").strip()
            if judul_baru == "" or studio_baru == "" or not harga_baru.isdecimal() or not seat_baru.isdecimal():
                print("Semua harus diisi, Harga dan Seat harus berupa Angka!!!")
            elif int(harga_baru) <= 0 or int(seat_baru) <= 0:
                print("Harga dan seat harus lebih dari 0!")
            else:
                film.append([id_baru, judul_baru, studio_baru, int(harga_baru), int(seat_baru)])
                id_baru += 1
                print("Film Berhasil Ditambahkan!")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "admin" and menu == "3":
            id_film = input("ID Film : ").strip()
            berhasil = False
            for f in film:
                if id_film.isdecimal() and f[0] == int(id_film):
                    berhasil = True
                    judul_baru = input("Judul Baru  : ").strip()
                    harga_baru = input("Harga Baru  : ").strip()
                    berubah = False
                    if judul_baru != "":
                        f[1] = judul_baru
                        berubah = True
                    if harga_baru != "":
                        if harga_baru.isdecimal() and int(harga_baru) > 0:
                            f[3] = int(harga_baru)
                            berubah = True
                        else:
                            print("Harga tidak valid, harga tidak diubah!")
                    if berubah:
                        print("Film Berhasil Diubah!")
                    else:
                        print("Tidak ada data yang diubah.")
                    break
            if not berhasil:
                print("ID Film Tidak Ditemukan!")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "admin" and menu == "4":
            id_film = input("ID Film : ").strip()
            berhasil = False
            for f in film:
                if id_film.isdecimal() and f[0] == int(id_film):
                    film.remove(f)
                    berhasil = True
                    print("Film Berhasil Dihapus!")
                    break
            if not berhasil:
                print("Film Tidak Ditemukan!")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "admin" and menu == "5":
            for r in riwayat:
                print(r[0], "|", r[1], "|", r[2], "tiket | Rp", r[3])
            if len(riwayat) == 0:
                print("Belum ada pembelian.")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "admin" and menu == "6":
            print("Log Out berhasil.")
            input("Tekan Enter untuk Melanjutkan...")
            break

        elif role == "user" and menu == "2":
            i = input("ID Film : ").strip()
            jml = input("Jumlah Tiket : ").strip()
            target = None
            for f in film:
                if i.isdecimal() and f[0] == int(i):
                    target = f
            if target is None:
                print("Film tidak ditemukan!")
            elif not jml.isdecimal() or int(jml) <= 0:
                print("Jumlah harus angka positif!")
            elif int(jml) > target[4]:
                print("Kursi tidak cukup! Sisa:", target[4])
            else:
                total = int(jml) * target[3]
                target[4] -= int(jml)
                riwayat.append([aktif, target[1], int(jml), total])
                print("Berhasil! Total: Rp", total)
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "user" and menu == "3":
            pembelian = False
            for r in riwayat:
                if r[0] == aktif:
                    print(r[1], "|", r[2], "tiket | Rp", r[3])
                    pembelian = True
            if not pembelian:
                print("Belum ada pembelian")
            input("Tekan Enter untuk Melanjutkan...")
        elif role == "user" and menu == "4":
            print("Log Out berhasil.")
            input("Tekan Enter untuk Melanjutkan...")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk Melanjutkan...")