# Raise Exception (Melemparkan eksepsi buatan sendiri)
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    print(f"Umur anda adalah {umur}")

try:
    cek_umur(-5)
except ValueError as e:
    print(f"Terjadi kesalahan: {e}")
