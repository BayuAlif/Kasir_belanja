
jenis = int(input("masukkan jumlah jenis jenis barang yang di beli: "))


def main(harga, jumlah):

    
    return harga * jumlah

#buat list agar lebih mudah
mylist = []

for i in range (0, jenis):
    #diberi i+1 karena kita inginnn barang dimulai dari 1 jadi 0+1 = 1
    print("Barang", i+1) 
    nama = str(input("Masukkan nama barang: "))
    harga = int(input("Masukkan harga barang : Rp. "))
    jumlah = int(input("Masukkan jumlah barang : "))
    total = main(harga,jumlah)

    #Masukkan data ke list dengan append
    mylist.append([nama,harga,jumlah,total])

print("\nDaftar belanja:")

#buat variabel untuk nomor angka otomatis dan total keseluruhan barang yang dibeli
Number = 1
g_total = 0

for x in mylist:

    print(f"{Number}. {x[0]} - {x[2]} unit x Rp. {x[1]} = Rp. {x[3]}")
    Number += 1
    g_total += x[3]


print(f"\nTotal biaya belanja: Rp. {g_total}")

#buat condition dimana jika total belanja lebih dari 100000 maka akan ada discount 10% dan di python _ dianggap gak ada (khusus int)
if g_total > 100_000:

    #gunakan -= untuk pengurangan biayaya setelah mendapatkan discount 10%
    g_total -= g_total * 0.1

    print(f"\nTotal harga setelah mendapatkan discount Rp. {int(g_total)}")