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


def ambil_id_baru():
    global id_baru
    hasil = id_baru
    id_baru += 1
    return hasil
