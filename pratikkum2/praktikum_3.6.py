# ValueError, TypeError
try:
    angka = int("Bukan Angka")
except ValueError as e:
    print(f"Error Nilai: {e}")

try:
    hasil = "Angka: " + 10
except TypeError as e:
    print(f"Error Tipe: {e}")
