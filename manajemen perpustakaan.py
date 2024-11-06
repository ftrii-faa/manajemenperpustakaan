# Struktur data untuk menyimpan daftar buku dan transaksi peminjaman
class Buku:
    def _init_(self, id_buku, judul, pengarang):
        self.id_buku = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.dipinjam = False

    def _str_(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"ID Buku: {self.id_buku}, Judul: {self.judul}, Pengarang: {self.pengarang}, Status: {status}"

# Kelas perpustakaan untuk mengelola buku dan transaksi
class Perpustakaan:
    def _init_(self):
        self.daftar_buku = []
        self.daftar_transaksi = []

    def tambah_buku(self, id_buku, judul, pengarang):
        buku = Buku(id_buku, judul, pengarang)
        self.daftar_buku.append(buku)
        print("Buku berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for buku in self.daftar_buku:
                print(buku)

    def cari_buku(self, judul):
        found = False
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                print("Buku ditemukan:")
                print(buku)
                found = True
                break
        if not found:
            print("Buku tidak ditemukan.")

    def pinjam_buku(self, id_buku, nama_peminjam):
        for buku in self.daftar_buku:
            if buku.id_buku == id_buku:
                if not buku.dipinjam:
                    buku.dipinjam = True
                    self.daftar_transaksi.append({"id_buku": id_buku, "nama_peminjam": nama_peminjam})
                    print("Buku berhasil dipinjam.")
                else:
                    print("Buku sedang dipinjam.")
                return
        print("ID Buku tidak ditemukan.")

    def kembalikan_buku(self, id_buku):
        for buku in self.daftar_buku:
            if buku.id_buku == id_buku:
                if buku.dipinjam:
                    buku.dipinjam = False
                    print("Buku berhasil dikembalikan.")
                else:
                    print("Buku tidak sedang dipinjam.")
                return
        print("ID Buku tidak ditemukan.")

# Fungsi utama untuk menjalankan aplikasi perpustakaan
def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\nSistem Informasi Perpustakaan")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Cari Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            id_buku = input("Masukkan ID Buku: ")
            judul = input("Masukkan Judul Buku: ")
            pengarang = input("Masukkan Pengarang: ")
            perpustakaan.tambah_buku(id_buku, judul, pengarang)
        elif pilihan == '2':
            perpustakaan.tampilkan_buku()
        elif pilihan == '3':
            judul = input("Masukkan Judul Buku yang dicari: ")
            perpustakaan.cari_buku(judul)
        elif pilihan == '4':
            id_buku = input("Masukkan ID Buku yang ingin dipinjam: ")
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            perpustakaan.pinjam_buku(id_buku, nama_peminjam)
        elif pilihan == '5':
            id_buku = input("Masukkan ID Buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(id_buku)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem informasi perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()