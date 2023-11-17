# data user
user = {
    'username' : "yosua",
    'password' : "123456",
    'saldo' : 500.000,
    'status' : "biasa"
}

# database produk
display_produk = {
    1 : {"nama" : "Christmas Tree", "harga" : 400.000, "stok" : 50},
    2 : {"nama" : "Hiasan Pohon", "harga" : 75.000, "stok" : 70},
    3 : {"nama" : "Topi Santa", "harga" : 50.000, "stok" : 100},
    4 : {"nama" : "Kaos Natal", "harga" : 60.000, "stok" : 150},
    5 : {"nama" : "Hadiah Natal", "harga" : 50.000, "stok" : 80}
}

# database voucer
voucer = "G0DBL3SSY0U"



def registrasi_member ():
    pin = input("masukan pin anda:")

    if pin == user['password'] :
        user['status'] = "VIP"
        print("selamat akun anda sekarang VIP")
            


def tampil_produk() :
    print("Daftar produk:")
    for id_display_produk, info_display_produk in display_produk.items():
        print(f"{id_display_produk}. {info_display_produk['nama']} - Rp {info_display_produk['harga']} - Stok {info_display_produk['stok']:,}")


def topup_emoney():
    pin = input("masukan password untuk melakukan top-up:")
    jumlah = int(input("masukan jumlah top-up:"))

    jumlah_topup = user['saldo'] + jumlah
    print("Top-up berhasil")


def transaksi(status):
    tampil_produk()
    pin = input("masukan pin anda untuk melakukan transasksi:")
    id_produk = int(input("masukan ID produk yang ingin di beli: "))
    jumlah_produk = int(input("masukan jumlah produk yang akan di beli: "))
    total_harga = jumlah_produk * display_produk[id_produk]["harga"]

    if pin in user and user['status'] == "VIP" :
        total_harga *= 0.7
    print(f"total harga belanjaan anda : Rp {total_harga:,}")

    kode_voucer = input("masukan kode voucer (jika ada):")

    if kode_voucer == voucer:
        total_harga *= 0.9
        print(f"total harga belanjaan anda setelah diskon dengan voucer : Rp {total_harga:,}")
    else:
        print(f"total harga belanjaan anda : Rp {total_harga:,}")

    pin = input("masukan password anda untuk melakukan pembayaran:")

    if pin in user and user['saldo'] >= total_harga:
        user['saldo'] - total_harga
        print("pembayaran berhasil!")
    else:
        print("saldo e-money anda tidak mencukupi. silahkan top-up saldo anda")
        topup_emoney()

 

def main():
    print("silahkan lakukan login dengan memasukan password anda terlebih dahulu")
    pin = input("Masukan password Anda:")
    if pin == user['password']:
        print("Login berhasil")
        while True:
            print("========== BLESSED STORE  ==========")
            print("welcome", user['username'])
            print("1. Registrasi akun")
            print("2. Tampilkan produk")
            print("3. Top-up e-money")
            print("4. Transaksi")
            print("5. Keluar")

            pilihan_user = input("masukan pilihan anda:")

            if pilihan_user == "1":
                registrasi_member()
            elif pilihan_user == "2":
                tampil_produk()
            elif pilihan_user == "3" :
                topup_emoney()
            elif pilihan_user == "4" :
                transaksi('status')
            elif pilihan_user == "5":
                print("Terima kasih telah menggunakan program kami. God bless you!!!!")
                break
            else:
                print("pilihan tidak valid. Silahkan pilih ulang")
 
    else: 
        print("password yang anda masukan salah. silakan coba lagi")
 
 

main()