import math
import os

# Skenario A: OverflowError > ArithmeticError > Exception
print("--- Skenario A ---")
try:
    # Memaksa OverflowError (misalnya hasil terlalu besar untuk float)
    hasil = math.exp(1000)
    print(hasil)
except OverflowError as e:
    print(f"Ditangkap oleh OverflowError: {e}")
except ArithmeticError as e:
    print(f"Ditangkap oleh ArithmeticError: {e}")
except Exception as e:
    print(f"Ditangkap oleh base Exception: {e}")

print("\n--- Skenario B ---")
# Skenario B: FileExistsError > OSError > Exception
try:
    # Membuat file yang sudah ada
    nama_file = "test_file.txt"
    with open(nama_file, 'w') as f:
        f.write("Halo")
    
    # Mencoba membuat eksklusif file yang sama (akan trigger FileExistsError)
    with open(nama_file, 'x') as f:
        f.write("Ditolak")
except FileExistsError as e:
    print(f"Ditangkap oleh FileExistsError: {e}")
except OSError as e:
    print(f"Ditangkap oleh OSError: {e}")
except Exception as e:
    print(f"Ditangkap oleh base Exception: {e}")
finally:
    # Bersihkan file
    if os.path.exists(nama_file):
        os.remove(nama_file)
