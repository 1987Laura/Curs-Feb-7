with open("ethereum.txt", "r") as file_reader:
    continut = file_reader.read()
    print(continut)
    linii = continut.split("\n")
    print(linii)

    linii = [float(i) for i in linii]
    print(linii)

    media = sum(linii) / len(linii)
    print("media =", media )
