# IndexError, KeyError
try:
    data_list = [1, 2, 3]
    print(data_list[5])
except IndexError as e:
    print(f"Error Indeks: {e}")

try:
    data_dict = {"nama": "Budi"}
    print(data_dict["umur"])
except KeyError as e:
    print(f"Error Kunci: {e}")
