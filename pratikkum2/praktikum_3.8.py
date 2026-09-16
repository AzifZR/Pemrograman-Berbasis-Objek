class SaldoTidakMencukupiError(Exception):
    pass

class NominalTidakValidError(Exception):
    pass

def atm():
    saldo = 500000
    print("--- ATM Sederhana ---")
    print(f"Saldo awal: Rp{saldo}")
    
    try:
        nominal_input = input("Masukkan nominal tarik tunai: ")
        
        try:
            nominal = int(nominal_input)
        except ValueError:
            raise ValueError("Nominal yang dimasukkan bukan angka.")
            
        if nominal <= 0:
            raise NominalTidakValidError("Nominal kurang dari atau sama dengan 0.")
            
        if nominal > saldo:
            raise SaldoTidakMencukupiError("Saldo tidak mencukupi.")
            
        saldo -= nominal
        print(f"Tarik tunai berhasil. Sisa saldo: Rp{saldo}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except NominalTidakValidError as e:
        print(f"Error: {e}")
    except SaldoTidakMencukupiError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error tak terduga: {e}")
        
if __name__ == "__main__":
    atm()
