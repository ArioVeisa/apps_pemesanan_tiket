import csv
import pandas as pd

data_ketersedian_tiket = pd.read_csv('pemesanan.csv')



with open('pemesanan.csv', 'a', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',')

# Inisialisasi dataTiket sebagai list kosong
dataTiket = []

hargaTiket = {
    'Surabaya - Yogyakarta': 60000,
    'Surabaya - Malang': 40000,
    'Surabaya - Jakarta': 100000
}

def cekTiket():
    cekPelanggan = input('Masukkan Nama anda: ').lower()
    for tiket in dataTiket:
        if cekPelanggan == tiket[0]:
            print('Tiket anda terdaftar')
            return
    print('Tiket anda tidak terdaftar. Mohon pesan tiket terlebih dahulu.')

def bubble_sort(data, key=lambda x: x):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(data[j]) > key(data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]

def laporan():
    print('\n=== Laporan Tiket ===')
    
    # Menggunakan bubble_sort untuk mengurutkan dataTiket berdasarkan nama pelanggan
    bubble_sort(dataTiket, key=lambda x: x[0].lower())

    for tiket in dataTiket:
        print(f"Nama Pelanggan: {tiket[0]}")
        print(f"Jumlah Tiket: {tiket[1]}")
        print(f"Tujuan: {tiket[2]}")
        print(f"Harga: Rp. {tiket[3] * tiket[1]}")
        print(f"Metode Pembayaran : {tiket[4]}")
        print('-' * 30)

def pembayaran():
    print()
    print(' === Metode Pembayaran === ')
    print('1. Cash')
    print('2. Transfer')
    print()
    
    metodePembayaran = input('Pilih metode pembayaran (1/2): ')

    if metodePembayaran == '1':
        print('Pembayaran anda berhasil dan tiket anda berhasil dipesan ')
        metodePembayaran = 'Cash'

    elif metodePembayaran == '2':
        print('\nPilihlah Metode transfer dibawah ini')
        print('1. BCA')
        print('2. Mandiri')
        print('3. BNI')
        print('4. BRI')

        bank = input(' Masukan pilihan bank anda (1/2/3/4): ')

        if bank in ('1', '2', '3', '4'):
            if bank == '1' :
                metodePembayaran = 'BCA'
            if bank == '2' :
                metodePembayaran = 'Mandiri'
            if bank == '3' :
                metodePembayaran = 'BNI'
            if bank == '4' :
                metodePembayaran = 'BRI'
                
            print('Pembayaran anda berhasil dan tiket anda berhasil dipesan ')
        else:
            print("Pilihan metode pembayaran tidak valid!")
            return None
    else:
        print('Pilihan metode pembayaran tidak valid. Pembayaran tidak dapat diproses.')
        return None

    return metodePembayaran

def pesan_tiket():
    namaPelanggan = input("Masukan nama pelanggan: ").lower()
    jumlahTiket = int(input("Berapa tiket yang akan dipesan (Batas : 4 Kursi dalam 1 Kali transaksi): "))
    if jumlahTiket > 4:
        print('=== Penumpang hanya bisa memesan 4 tiket dalam 1 kali transaksi ===')
        return
    
    print("\nDaftar Tujuan:")
    for i, (tujuan, harga) in enumerate(hargaTiket.items(), start=1):
        print(f"{i}. {tujuan} - Rp. {harga}")

    

    # Pilih tujuan berdasarkan choice
    pilihTujuan = int(input("Pilih Tujuan (1/2/3): "))
    
    print('\n')
    # Menghitung total jumlah tiket untuk tujuan Surabaya - Malang
    total_tiket_surabaya_malang = data_ketersedian_tiket[data_ketersedian_tiket['Tujuan'] == 'Surabaya - Malang']['Jumlah Tiket'].sum()

    # Menghitung total jumlah tiket untuk tujuan Surabaya - Yogyakarta
    total_tiket_surabaya_yogyakarta = data_ketersedian_tiket[data_ketersedian_tiket['Tujuan'] == 'Surabaya - Yogyakarta']['Jumlah Tiket'].sum()

    # Menghitung total jumlah tiket untuk tujuan Surabaya - Jakarta
    total_tiket_surabaya_jakarta = data_ketersedian_tiket[data_ketersedian_tiket['Tujuan'] == 'Surabaya - Jakarta']['Jumlah Tiket'].sum()

    # Validasi dan print hasil
    if pilihTujuan == 1:
        if total_tiket_surabaya_yogyakarta >= 120:
            print("Tiket (Surabaya - Yogyakarta) Sudah habis di pesan")
            
    if pilihTujuan == 2:            
        if total_tiket_surabaya_malang >= 150:
            print("Tiket (Surabaya - Malang) Sudah habis di pesan")
            return
    if pilihTujuan == 3:  
        if total_tiket_surabaya_jakarta >= 200:
            print("Tiket (Surabaya - Jakarta) Sudah habis di pesan")
            
    print('\n')
    
    

    if pilihTujuan not in range(1, len(hargaTiket) + 1):
        print("Pilihan tujuan tidak valid.")
        return
    
    tujuan = list(hargaTiket.keys())[pilihTujuan - 1]
    harga = hargaTiket[tujuan]

    # Menyimpan data tiket
    metodePembayaran = pembayaran()

    if metodePembayaran is None:
        return

    # Menambahkan data tiket dengan urutan yang diinginkan
    dataTiket.append([namaPelanggan, jumlahTiket, tujuan, harga, metodePembayaran])

    print(f"\nTiket berhasil dibuat. Tujuan: {tujuan}, Harga: Rp. {harga * jumlahTiket}")
    
 # Menyimpan data tiket ke file CSV
    with open('pemesanan.csv', 'a', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',')
            # Menambahkan header jika file CSV masih kosong
        if csv_file.tell() == 0:
            header = ['Nama Pelanggan', 'Jumlah Tiket', 'Tujuan', 'Harga', 'Metode Pembayaran']
            data_writer.writerow(header)
            
        for tiket in dataTiket:
            data_writer.writerow(tiket)

# Menu
while True:
    print('\n=== Selamat datang di stasiun Surabaya ===')
    print('1. Pesan Tiket')
    print('2. Cek Status Tiket')
    print('3. Laporan Stasiun')
    print('4. Logout')

    choice = int(input('Silakan masukkan pilihan anda: '))

    if choice == 1:
        pesan_tiket()
    elif choice == 2:
        cekTiket()
    elif choice == 3:
        laporan()
    elif choice == 4:
        print('=== Terimakasih Selamat Jalan ===')
        
        break
       
    else:
        print("Pilihan tidak ada. Silakan coba lagi.")
