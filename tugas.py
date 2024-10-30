#list utama: kendaraan
kendaraan = ["mio", "motor", "200cc", "hitam", "roda 2"]

#mencetak isi list kendaraan
print(kendaraan)

#menambahkan value atau nilai diujung list (pakai append())

#proses append 1 (harga kendaraan)
kendaraan.append("20.000.000")

#proses append 2 (tipe kendaraan)
kendaraan.append("matic")

#cetak nilai kendaraan setelah perubahan
print(kendaraan)

#sisipkan nilai untuk tipe kendaraan
kendaraan.insert (2, "yamaha")

#cetak hasil list akhirnya
print (kendaraan)



pilihan = int(input("""pilih nomer pilihan:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas lingkaran
"""))

                   
match pilihan:
    case 1:
        print("menghitung luas persegi")
        s = int(input("masukan nilai sisi: "))
        luas_persegi = s * s
        print(f"luas persegi dengan sisi (s) adalah (luas persegi)")
    case 2:
       print("menghitung luas lingkaran")
       pi = 3.14
       r = int(input("masukan nilai jari jari"))
       luaslingkaran = pi * r**2
       print(f"luas lingkaran dengan jari jari{r} adalah {luaslingkaran}")
    case 3:
        print("menghitung luas segitiga")
        alas = int(input("masukan nilai alas: "))
        tinggi = int(input("masukan nilai tinggi: "))
        luassegitiga = 1/2 *alas *tinggi
        print(f"luas segitiga dengan alas {alas} dan tinggi adalah {luassegitiga}")
    case _:
        print("input tidak valid")         