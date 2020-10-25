import re

opcion = 0
while opcion != 11:
    print('---------------------------------------------------------- Eliel Novelo ---------------------------------------------')
    print('\nSelecciona una Opción')
    print('1.- Todas las palabras que tengan una longitud de 7 o más letras\n2.- Expresiones que NO finalicen con una vocal.')
    print('3.- Las palabras que inicien con “M” donde la segunda letra no sea vocal.\n4.- Expresiones encerradas entre comillas')
    print('5.- Busqueda de Ip’s\n6.- Horas\n7.- Telefono\n8.- Correos electrónicos\n9.- Url´s')
    print('10.- Codigo Postal\n11.- Salir')
    opcion = int(input("Opción a realizar: "))

    if opcion == 1:
        print('--- Palabras encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "[a-zA-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        print('--- Palabras encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[^aeiou]$"
            for elemento in lista:
                if re.search(regex,elemento):
                   print(elemento)
        textfile.close()   
    elif opcion == 3:
        print('--- Palabras encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "([M][^aeiou][a-zA-z]+)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        print('--- EXpresiones encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "(\".*\")"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        print('--- Ip´s encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 6:
        print('--- Horas encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,2}\:[0-9]{2})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 7:
        print('--- Telefonos encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "(\+[0-9]{2}\ [0-9]{10})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 8:
        print('--- Correos electrónicos encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-z]{0,}\@[a-zA-z]{0,}\.[a-zA-z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 9:
        print('---	Url’s encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-Z]{0,}\:[\/][\/]+[a-zA-Z0-9].*\.[a-zA-Z0-9].*\.[a-zA-Z].*\/[a-zA-Z].*\/[a-zA-Z0-9].*\?[a-zA-Z].*\=[a-zA-Z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 10:
        print('--- postales encontradas ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "[0-9]{5}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()  
    else:
        print('Ingresa valores dentro de las opciones')
    
