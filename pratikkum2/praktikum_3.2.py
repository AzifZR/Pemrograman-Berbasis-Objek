# Eksepsi dengan blok finally dan else
try:
    file = open("data.txt", "r")
    konten = file.read()
except FileNotFoundError:
    print("Error: File data.txt tidak ditemukan!")
else:
    print("Berhasil membaca file:")
    print(konten)
finally:
    print("Selesai mencoba mengakses file.")
