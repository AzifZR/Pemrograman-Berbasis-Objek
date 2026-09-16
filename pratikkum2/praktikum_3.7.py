# AttributeError, ImportError
try:
    import math
    print(math.a)
except AttributeError as e:
    print(f"Error Atribut: {e}")

try:
    from time import datetime
except ImportError as e:
    print(f"Error Import: {e}")
