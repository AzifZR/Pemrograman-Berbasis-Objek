# Menangani Eksepsi Dasar
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print(f"Hasil: {hasil}")
except ValueError:
    print("Error: Harus memasukkan angka yang valid!")
except ZeroDivisionError:
    print("Error: Tidak bisa dibagi dengan nol!")
