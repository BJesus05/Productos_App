import csv
db = 'basedato.csv'

#Funcion para obtener un mensaje
def intro(message):
    return int(input(message))

#Funcion para leer el archivo
def leerArchivo():
    with open(db, 'r') as archivo_csv:
        # Crear  lector CSV
        reader = csv.reader(archivo_csv)
        file = list(reader)
    return file

#Funcion para grear separadores en el registro
def mostraRegistroFormatiado(filas, index):
    regsitroFormateado = '|'
    separador = regsitroFormateado
    for i, fila in enumerate(filas, start=0):
        regsitroFormateado += filas[i].center(20) + '|'
        separador += '--------------------' + '|'
    if index == 0:
        regsitroFormateado = separador + '\n' + regsitroFormateado + '\n' + separador
    else:
         regsitroFormateado = regsitroFormateado + '\n' + separador
    print(regsitroFormateado)





#Funcion de leer
def mostrarRegistro():
    #lee las nueva fila y la emprime
    reader = leerArchivo()
    for index, row in enumerate(reader, start=0):
        mostraRegistroFormatiado(row, index)


#Funcion escribir en archivo
def escribirArchivo(data):
        # Abrir el archivo db.CSV y escribir la nueva fila
        with open(db, 'w', newline='') as file:
            writer = csv.writer(file)

        # Escribir filas en el archivo db.CSV
            for fila in data:
                writer.writerow(fila)


#Funcion de eliminar
def eliminar():
    option = 1
    while option == 1:
        print("¿Esta seguro que desea eliminar algun registro registro?")
        print("1. Si")
        print("0. No")
        print("===========================")
        opcion = intro("Ingrese opcion")
        print("===========================")

        if opcion == 0:
            option = opcion
        elif opcion == 1:
            print("Elimnar datos:")

            # Crear lista de filas
            filas = leerArchivo()

            # Eliminar la fila por índice
            indice_fila_eliminar = int(input("Ingrese  la fila que desea eliminar"))
            filas.pop(indice_fila_eliminar)

            escribirArchivo(filas)
            print("Registro Eliminado")


#Funcion de actualizar
def actualizar():
    option = 1
    while option == 1:
        print("¿Esta seguro que desea actualizar algun registro?")
        print("1. Si")
        print("0. No")
        print("===========================")
        opcion = intro("Ingrese opcion")
        print("===========================")

        if opcion == 0:
            option = opcion
        elif opcion == 1:
            print("Actializar datos")
            # Pedir los campos que se quieren cambiar y valor a cambiar
            filaActualizar = int(input("Ingrese el número de fila a actualizar: "))
            columnaActualizar = int(input("Ingrese el número de columna a actualizar: "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            # Abrir el archivo db.CSV y lee las nueva fila
            filas = leerArchivo()

            # Actualizar el valor de la columna especificada en la fila especificada
            filas[filaActualizar][columnaActualizar] = nuevo_valor
            # Abrir el archivo db.CSV y sobrescribir todas las filas
            escribirArchivo(filas)
            print("Se actualizó una fila en el archivo CSV.")



# Funcion para ingresar datos
def ingresar():
    option = 1
    while option == 1:
        print("¿Esta seguro que desea agregar un nuevo registro?")
        print("1. Si")
        print("0. No")
        print("===========================")
        opcion = intro("Ingrese opcion")
        print("===========================")

        if opcion == 0 :
            option = opcion
        elif opcion == 1:
            print("Ingresando datos")
            # Ingresar los campos
            id = input("Ingrese el id: \n")
            nombre = input("Ingrese el nombre: \n")
            descirpcion = input("Ingrese la despecicion: \n")
            cantidad = input("Ingrese la cantiad: \n")
            precioUnitario = input("Ingrese la Precio de unitario: \n")
            costo = input("Ingrese la Costo: \n")
            precioVenta = input("Ingrese la Precio de venta: \n")
            unidadesInventario = input("Ingrese la unidades de Inventario: \n")
            bodega = input("Ingrese la bodega: \n")
            sucursales = input("Ingrese la sucursales: \n")
            # Agregar los datos a una lista
            data = [id, nombre, descirpcion, cantidad, precioUnitario, costo, precioVenta, unidadesInventario, bodega,
                    sucursales]

            #Leer datos de archivo
            filas = leerArchivo()
            #Agrega en las filas
            filas.append(data)

            #escribir la nueva fila
            escribirArchivo(filas)
        else:
            print("Ingrese una opcion  mencionadas anteriormente")
            print("===========================")

#Funcion de pantalla inicial
def main():
    option = 1
    #Ver opciones que tiene el usuarip
    while option == 1:
        print("===========================")
        print("1. Insertar registro")
        print("2. Ver registro")
        print("3. Actualizar registro")
        print("4. Elimnar registro")
        print("0. Salir")
        print("===========================")
        #Verificar que se ingre un dato correcto
        try:
            opcion = intro("Ingrese opcion")
            if opcion == 1:
                ingresar()
            elif opcion == 2:
                mostrarRegistro()
            elif opcion == 3:
                actualizar()
            elif opcion == 4:
                eliminar()
            elif opcion == 0:
                print("Decidio salir del programa. Tenga un feliz dia User")
                break
        except:
            print("Ingrese una opcion  mencionadas anteriormente")

main()