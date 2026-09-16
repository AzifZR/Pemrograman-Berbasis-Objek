try:
    list=[1, 2, 3]
    print(list[3])
except IndexError:
    print("Ada kesalahan indeks")
except LookupError:
    print("Ada kesalahan lookup")
except Exception:
    print("Ada kesalahan base")
print("<< End Program >>")
