user_input = "falih"
pass_input = "043"

kalimantan_gambut = 0
kalimantan_mineral = 0
sumatera_gambut = 0
sumatera_mineral = 0    

print("=" * 45)
print("   REKAPITULASI TITIK API - BPBD & MANGGALA AGNI")
print("=" * 45)


while True:
    username = input("Masukkan username : ").lower().strip()
    password = input("Masukkan password : ")

    if username == user_input and password == pass_input:
        print("\nLogin berhasil!")
        break
    elif username == "" and password == "":
        print("Username dan password tidak boleh kosong, Silakan coba lagi")
    elif username == "":
        print("Username tidak boleh kosong., Silakan coba lagi")
    elif password == "":
        print("Password tidak boleh kosong., Silakan coba lagi")
    elif username != user_input and password != pass_input:
        print("Username dan password salah, Silakan coba lagi")
    elif password != pass_input:
        print("Password salah, Silakan coba lagi.")
    elif username != user_input:
        print("Username salah, Silakan coba lagi.")

ulang = "y"
while ulang == "y":
    print("\nTambah Data Kebakaran Hutan dan Lahan")

    pulau = ""
    while pulau != "kalimantan" and pulau != "sumatera":
        pulau = input("Masukkan nama pulau ( Kalimantan/Sumatera ): ").lower().strip()
        if pulau == "":
            print("Pulau tidak boleh kosong, Silakan coba lagi")
        elif pulau != "kalimantan" and pulau != "sumatera":
            print("Pulau tidak valid, Silakan coba lagi")

    lahan = ""
    if pulau == "kalimantan":
        while lahan != "gambut" and lahan != "mineral":
            lahan = input("Masukkan jenis lahan ( Gambut/Mineral ): ").lower().strip()
            if lahan == "":
                print("Jenis lahan tidak boleh kosong, Silakan coba lagi")
            elif lahan != "gambut" and lahan != "mineral":
                print("Jenis lahan tidak valid Silakan coba lagi")
    elif pulau == "sumatera":
        while lahan != "gambut" and lahan != "mineral":
            lahan = input("Masukkan jenis lahan ( Gambut/Mineral ): ").lower().strip()
            if lahan == "":
                print("Jenis lahan tidak boleh kosong, Silakan coba lagi")
            elif lahan != "gambut" and lahan != "mineral":
                print("Jenis lahan tidak valid, Silakan coba lagi")

    hotspot = 0
    while hotspot <= 0:
        h_input = input("Masukkan jumlah Titik Api ( Hotspot ) : ")
        if h_input == "":
            print("Jumlah Titik Api tidak boleh kosong, Silakan coba lagi")
        elif not h_input.isdigit() or int(h_input) <= 0:
            print("Jumlah Titik Api harus berupa angka positif, Silakan coba lagi")
        else:
            hotspot = int(h_input)


    luas = hotspot * 5
    if pulau == "kalimantan":
        if lahan == "gambut":
            kalimantan_gambut += luas
        elif lahan == "mineral":
            kalimantan_mineral += luas
    elif pulau == "sumatera":
        if lahan == "gambut":
            sumatera_gambut += luas
        elif lahan == "mineral":
            sumatera_mineral += luas


    ulang = ""
    while ulang != "y" and ulang != "t":
        ulang = input("Apakah ingin memasukkan data lagi? ( Y/T ): ").lower().strip()
        if ulang == "":
            print("Input tidak boleh kosong, Silakan coba lagi")
        elif ulang != "y" and ulang != "t":
            print("Input tidak valid, Silakan coba lagi")

total = kalimantan_gambut + kalimantan_mineral + sumatera_gambut + sumatera_mineral
print("\n" + "=" * 45)
print("   RINGKASAN TOTAL LUAS LAHAN TERBAKAR")
print("=" * 45)
print("Kalimantan - Gambut  :", kalimantan_gambut, "Hektare")
print("Kalimantan - Mineral :", kalimantan_mineral, "Hektare")
print("Sumatera - Gambut    :", sumatera_gambut, "Hektare")
print("Sumatera - Mineral   :", sumatera_mineral, "Hektare")
print("-" * 45)
print("TOTAL KESELURUHAN    :", total, "Hektare")
print("=" * 45)
