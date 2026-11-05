import os
from colorama import init, Fore
import data

init(autoreset=True)


def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def jeda(kata="Melanjutkan"):
    input(Fore.YELLOW + "Tekan Enter untuk " + kata + "...")

def tampil_header_awal():
    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "KASIR BIOSKOP PALING BAGUS".center(70))
    print(Fore.CYAN + "=" * 70)

def tampil_header_menu():
    print(Fore.YELLOW + "||===== MENU UTAMA =====||".center(70))
    print("User:", Fore.GREEN + data.aktif, "| Role:", Fore.CYAN + data.role)
