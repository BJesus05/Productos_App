db = "db.csv"
with open(db , "r") as archivo:
    next(archivo, None)
    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split(",")

        nombre = lista [0]
        nombre1 = lista[1]
        nombre2 = lista[2]
        nombre3 = lista[3]
        nombre4 = lista[4]
        nombre5 = lista[5]
        nombre6 = lista[6]
        nombre7 = lista[7]
        nombre8 = lista[8]
        nombre9 = lista[9]
        nombre10 = lista[10]
        nombre11 = lista[11]

        print(f"{nombre},{nombre1},{nombre2},{nombre3}, {nombre4},{nombre5},{nombre6},{nombre7},{nombre8},{nombre69}, {nombre10},")