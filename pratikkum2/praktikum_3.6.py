try:
    bill=9
    bil2=0
    x=bill/bil2
except FloatingPointError:
    print("Ada kesalahan")
except ZeroDivisionError:
    print("Ada kesalahan pembagian nol")
except ArithmeticError:
    print("Ada kesalahan aritmatika")
print("<< End Program >>")
