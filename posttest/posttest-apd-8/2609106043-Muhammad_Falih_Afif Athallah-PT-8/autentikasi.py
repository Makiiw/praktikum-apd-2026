import pwinput
from colorama import Fore
import data


def cek_login(nama, sandi):
    user_ada = False
    pass_ada = False
    for akun in data.user:
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

def register():
    username_baru = input("Masukkan Username baru   : ").strip()
    password_baru = pwinput.pwinput("Masukkan Password baru   : ").strip()
    user_ada = False
    for akun in data.user:
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
        print(Fore.RED + str(e))
    else:
        data.user.append([username_baru, password_baru, "user"])
        print(Fore.GREEN + "Register berhasil!")
