try:
    with open("sample.txt", mode="r") as file:
        print(file.read())
except Exception as e:
    print(e)
print("<< End Program >>")
