import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "falih": {"password": "043", "role": "user"}
}

films = {
    "1": {"judul": "G30S/ISO", "studio": "Studio 1", "harga": 50000, "seat": 75},
    "2": {"judul": "Herul 1990", "studio": "Studio 2", "harga": 50000, "seat": 70},
    "3": {"judul": "Finding Falih", "studio": "Studio 3", "harga": 35000, "seat": 100}
}

riwayat = {}
id_baru = 4
id_riwayat = 1
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

            if input_user == "" and input_pass == "":
                print("Username dan Password tidak boleh kosong!")
            elif input_user == "":
                print("Username tidak boleh kosong!")
            elif input_pass == "":
                print("Password tidak boleh kosong!")
            elif input_user not in users:
                print("Username salah!")
            elif users[input_user]["password"] != input_pass:
                print("Password salah!")
            else:
                aktif = input_user
                role = users[input_user]["role"]
                break
            input("Tekan Enter untuk melanjutkan...")

        elif opsi == "2":
            username_baru = input("Masukkan Username baru   : ").strip()
            password_baru = input("Masukkan Password baru   : ").strip()

            if username_baru == "" and password_baru == "":
                print("Username dan Password tidak boleh kosong!")
            elif username_baru == "":
                print("Username tidak boleh kosong!")
            elif password_baru == "":
                print("Password tidak boleh kosong!")
            elif username_baru in users:
                print("Username sudah digunakan, Silahkan gunakan username lain!")
            else:
                users[username_baru] = {"password": password_baru, "role": "user"}
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
            if not films:
                print("Film Tidak Tersedia!")
            else:
                for id_f, f in films.items():
                    print("ID:", id_f, "|", f["judul"], "|", f["studio"], "| Rp", f["harga"], "| Seat:", f["seat"])
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
                films[str(id_baru)] = {
                    "judul": judul_baru,
                    "studio": studio_baru,
                    "harga": int(harga_baru),
                    "seat": int(seat_baru)
                }
                id_baru += 1
                print("Film Berhasil Ditambahkan!")
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "admin" and menu == "3":
            id_film = input("ID Film : ").strip()

            if id_film not in films:
                print("ID Film Tidak Ditemukan!")
            else:
                judul_baru = input("Judul Baru  : ").strip()
                harga_baru = input("Harga Baru  : ").strip()
                berubah = False

                if judul_baru != "":
                    films[id_film]["judul"] = judul_baru
                    berubah = True

                if harga_baru != "":
                    if harga_baru.isdecimal() and int(harga_baru) > 0:
                        films[id_film]["harga"] = int(harga_baru)
                        berubah = True
                    else:
                        print("Harga tidak valid, harga tidak diubah!")

                if berubah:
                    print("Film Berhasil Diubah!")
                else:
                    print("Tidak ada data yang diubah.")
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "admin" and menu == "4":
            id_film = input("ID Film : ").strip()

            if id_film in films:
                del films[id_film]
                print("Film Berhasil Dihapus!")
            else:
                print("Film Tidak Ditemukan!")
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "admin" and menu == "5":
            if not riwayat:
                print("Belum ada pembelian.")
            else:
                for r in riwayat.values():
                    print(r["user"], "|", r["judul"], "|", r["jumlah"], "tiket | Rp", r["total"])
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "admin" and menu == "6":
            print("Log Out berhasil.")
            input("Tekan Enter untuk Melanjutkan...")
            break

        elif role == "user" and menu == "2":
            i = input("ID Film : ").strip()
            jml = input("Jumlah Tiket : ").strip()

            if i not in films:
                print("Film tidak ditemukan!")
            elif not jml.isdecimal() or int(jml) <= 0:
                print("Jumlah harus angka positif!")
            elif int(jml) > films[i]["seat"]:
                print("Kursi tidak cukup! Sisa:", films[i]["seat"])
            else:
                target = films[i]
                total = int(jml) * target["harga"]
                target["seat"] -= int(jml)
                riwayat[str(id_riwayat)] = {
                    "user": aktif,
                    "judul": target["judul"],
                    "jumlah": int(jml),
                    "total": total
                }
                id_riwayat += 1
                print("Berhasil! Total: Rp", total)
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "user" and menu == "3":
            ada = False
            for r in riwayat.values():
                if r["user"] == aktif:
                    print(r["judul"], "|", r["jumlah"], "tiket | Rp", r["total"])
                    ada = True
            if not ada:
                print("Belum ada pembelian")
            input("Tekan Enter untuk Melanjutkan...")

        elif role == "user" and menu == "4":
            print("Log Out berhasil.")
            input("Tekan Enter untuk Melanjutkan...")
            break

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk Melanjutkan...")
