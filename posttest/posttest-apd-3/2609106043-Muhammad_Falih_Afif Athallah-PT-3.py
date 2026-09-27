print("=" * 50)
print("SELAMAT DATANG DI STREAMING MUSIC ANGKASA".center(50))
print("=" * 50)

nama_pengguna = "Falih"
nim_pengguna = "43"
biaya_langganan = 1500000

username = input("Masukkan Nama Pengguna : ")
nim = input("Masukkan NIM Pengguna    : ")

if username == nama_pengguna and nim == nim_pengguna:
    print("\n" + "-" * 50)
    print(f"Login berhasil! Selamat datang, Muhammad Falih Afif Athallah!")
    print("-" * 50)

    print("\n" + "=" * 50)
    print("PILIHAN PAKET LANGGANAN ANGKASA".center(50))
    print("=" * 50)
    print(f"{'1. Paket Orbit':<20}{'Admin 1%':<12}Akses dasar lagu-lagu populer")
    print(f"{'2. Paket Nebula':<20}{'Admin 3%':<12}Akses lagu premium + playlist kustom")
    print(f"{'3. Paket Galaxy':<20}{'Admin 5%':<12}Akses premium + playlist + mode offline")
    print(f"{'4. Paket Supernova':<20}{'Admin 7%':<12}Akses semua fitur + konten eksklusif artis")
    print("=" * 50)

    pilihan_paket = input("Masukkan pilihan paket (1-4) : ")

    if pilihan_paket == "1":
        nama_paket = "Orbit"
        akses = "Akses dasar ke lagu-lagu populer"
        admin = 0.01
        status = True
    elif pilihan_paket == "2":
        nama_paket = "Nebula"
        akses = "Akses lagu premium dan playlist custom"
        admin = 0.03
        status = True
    elif pilihan_paket == "3":
        nama_paket = "Galaxy"
        akses = "Akses lagu premium, playlist custom, dan mode offline"
        admin = 0.05
        status = True
    elif pilihan_paket == "4":
        nama_paket = "Supernova"
        akses = "Akses semua fitur, playlist custom, mode offline, dan konten eksklusif artis"
        admin = 0.07
        status = True
    else:
        print("\nPilihan tidak tersedia!")
        status = False

    if status:
        biaya_admin = biaya_langganan * admin
        total_bayar = biaya_langganan + biaya_admin

        print("\n" + "=" * 50)
        print("DETAIL PEMBAYARAN - PAKET", nama_paket.upper())
        print("=" * 50)
        print(f"{'Biaya Langganan':<25}: Rp{biaya_langganan:,.0f}".replace(",", "."))
        print(f"{'Biaya Admin (' + str(int(admin*100)) + '%)':<25}: Rp{biaya_admin:,.0f}".replace(",", "."))
        print("-" * 50)
        print(f"{'TOTAL BAYAR':<25}: Rp{total_bayar:,.0f}".replace(",", "."))
        print("=" * 50)
        print("Fitur yang kamu dapatkan".center(50))
        print(("► " + akses))
        print("=" * 50)

else:
    print("\n" + "!" * 50)
    print("Login gagal! Nama atau NIM tidak sesuai dengan data")
    print("Program dihentikan")
    print("!" * 50)