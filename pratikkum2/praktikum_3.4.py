# Custom Exception
class SaldoKurangError(Exception):
    pass

def tarik_tunai(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoKurangError("Saldo Anda tidak mencukupi untuk penarikan ini.")
    return saldo - jumlah

try:
    sisa = tarik_tunai(100000, 150000)
    print(f"Penarikan berhasil. Sisa saldo: {sisa}")
except SaldoKurangError as e:
    print(f"Gagal: {e}")
