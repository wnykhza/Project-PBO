import user
import sqlite3


class Owner(user.User):

    def __init__(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        super().__init__(username, password, nama, gender, alamat, telepon, tanggalMasuk)