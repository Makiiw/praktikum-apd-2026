import pwinput
from colorama import init, Fore
import data
from tampilan import bersihkan_layar, jeda, tampil_header_awal, tampil_header_menu
from autentikasi import cek_login, register
from film import tampil_daftar_film, tambah_film, ubah_film, hapus_film
from transaksi import tampil_semua_riwayat, tampil_riwayat_saya, beli_tiket

init(autoreset=True)


def halaman_awal():
    while True:
        bersihkan_layar()
        tampil_header_awal()
        print("1. Login\n2. Register\n3. Exit")
        opsi = input("Pilih : ").strip()

        if opsi == "1":
            input_user = input("Masukkan Username   : ").strip()
            input_pass = pwinput.pwinput("Masukkan Password   : ").strip()
            try:
                akun = cek_login(input_user, input_pass)
            except ValueError as e:
                print(Fore.RED + str(e))
                jeda("melanjutkan")
            else:
                data.aktif, data.role = akun[0], akun[2]
                return
        elif opsi == "2":
            register()
            jeda("melanjutkan")
        elif opsi == "3":
            print(Fore.CYAN + "Terima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print(Fore.RED + "Opsi tidak valid, Harus Berupa Angka")
            jeda("melanjutkan")

def halaman_menu():
    while True:
        bersihkan_layar()
        tampil_header_menu()

        if data.role == "admin":
            print("1. Daftar Film\n2. Tambah Film\n3. Ubah Film\n4. Hapus Film\n5. Semua Riwayat\n6. Log Out")
        else:
            print("1. Daftar Film\n2. Beli Tiket\n3. Riwayat Saya\n4. Log Out")
        menu = input("Pilih : ").strip()

        if menu == "1":
            tampil_daftar_film()
        elif data.role == "admin" and menu == "2":
            tambah_film()
        elif data.role == "admin" and menu == "3":
            ubah_film()
        elif data.role == "admin" and menu == "4":
            hapus_film()
        elif data.role == "admin" and menu == "5":
            tampil_semua_riwayat()
        elif (data.role == "admin" and menu == "6") or (data.role == "user" and menu == "4"):
            print(Fore.GREEN + "Log Out berhasil.")
            jeda()
            return
        elif data.role == "user" and menu == "2":
            beli_tiket()
        elif data.role == "user" and menu == "3":
            tampil_riwayat_saya()
        else:
            print(Fore.RED + "Pilihan tidak valid!")
        jeda()

def main():
    while True:
        halaman_awal()
        halaman_menu()

try:
    main()
except (KeyboardInterrupt, EOFError):
    print(Fore.YELLOW + "\nProgram dihentikan.")
