from List import *
from Functions import *


hash_list = read_file()
hash_list2 = read_file2()
indexing_titulo = []
indexing_serial = []

lineas_Facheras = "------------------------------------------------------"
mensaje_Intro = "Bienvenido a la Libreria Publica de Manhattan!\n\nQue desea hacer?\n1. Insertar un nuevo libro\n2. Buscar un libro\n3. Prestar un libro\n4. Devolver un libro\n5. Eliminar libro\n6. Salir"

def Inicio():
    print(lineas_Facheras)
    print(mensaje_Intro)
    

def Main():
    Inicio()
    opcion = input('Ingrese el numero de la operacion:' )

    if opcion.isdigit :
        
        if int(opcion) >=1 and int(opcion) <=5:

            Opcion(opcion)

        elif int(opcion) ==6:
            print("\nCHAOOOOOOOOOOOOOOOOOO!!!!")
        else:

            Dato_mal_suministrado()
    else:

        Dato_mal_suministrado()

def Opcion(opcion):
    cota =""
    hash =0
    titulo =""
    serial=0
    disponibles = 0
    prestados = 0
    if int(opcion) ==1:

        while True:
            
            print("\nLa cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            cota_numero = cota[6:]
            cota_letras = cota[0:6]
            
            if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                hash = hash_function(cota_letras,int(cota_numero))
                if hash ==0:
                    if not hash_list.Vacio():
                        resultado = hash_list.Search(cota)
                        if resultado == None:
                            break
                        else:
                            print("Esa cota ya existe")
                    else:
                        break
                else:
                    if not hash_list2.Vacio():
                        resultado = hash_list2.Search(cota)
                        if resultado == None:
                            break
                        else:
                            print("Esa cota ya existe")
                    else:
                        break
                    

        while True:
            print("\nEl titulo es un nombre unico de libro con un maximo de 30 caracteres")
            titulo = input("Ingrese el titulo del libro (ejem: El Principito): ")
            
            if(len(titulo) <= 30):
    
                resultado=busquedaBinaria2(titulo,0,len(indexing_titulo),0,indexing_titulo)
                if resultado ==-1 or resultado ==None:
                    break
                else:
                    print("Ese Titulo ya esta asignado")

        while True:
            print("\nEl serial de 12 digitos, es un numero unico de libro puesto por la editorial")
            serial = input("Ingrese el serial del libro (ejem: 000012345678): ")
               
            if(len(serial) == 12) and (serial.isdigit()):

                resultado=busquedaBinaria(int(serial),0,len(indexing_serial),0,indexing_serial)
                if resultado ==-1 or resultado ==None:
                    break
                else:
                    print("Ese Serial ya esta asignado")

        while True:
            
            disponibles = input("\nIngrese el numero de libros disponibles: ")
            
            if(disponibles.isdigit()):
                if int(disponibles) >=0:
                    break
                
        while True:
            
            prestados = input("\nIngrese el numero de libros prestados: ")
            
            if(prestados.isdigit()):
                if int(prestados) >=0:
                    break
        
        contenido = [cota,titulo,serial,int(disponibles),int(prestados)]
        contenido_titulo = [titulo,cota]
        contenido_serial = [serial,cota]
        if hash ==0:
            hash_list.append(contenido)
            write_on_file(hash_list)
        else:
            hash_list2.append(contenido)
            write_on_file2(hash_list2)
        indexing_titulo.append(contenido_titulo)
        quicksort(indexing_titulo,0, len(indexing_titulo) - 1)
        indexing_serial.append(contenido_serial)
        quicksort(indexing_serial,0, len(indexing_serial) - 1)
        print("Se ha ingresado el libro con exito")
                
    elif int(opcion) ==2:

        print("\nEscriba la opcion por donde quiere buscar el libro\n1. Cota\n2. Titulo\n3. Serial")
        opcion_busqueda = input("Respuesta: ")

        if int(opcion_busqueda) ==1:
            while True:
            
                print("\nLa cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
                cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

                cota_numero = cota[6:]
                cota_letras = cota[0:6]
            
                if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                    hash = hash_function(cota_letras,int(cota_numero))
                    if hash ==0:
                        if not hash_list.Vacio():
                            resultado = hash_list.Search(cota)
                            if resultado != None:
                                print(resultado.data)
                                break
                        else:
                            print("La lista esta vacia")
                            break
                    else:
                        if not hash_list2.Vacio():
                            resultado = hash_list2.Search(cota)
                            if resultado != None:
                                print(resultado.data)
                                break
                        else:
                            print("La lista esta vacia")
                            break
        
        elif int(opcion_busqueda) == 2:

            while True:
                print("\nEl titulo es un nombre unico de libro con un maximo de 30 caracteres")
                titulo = input("Ingrese el titulo del libro (ejem: El Principito): ")

                if(len(titulo) <= 30):
                    resultado=busquedaBinaria2(titulo,0,len(indexing_titulo),0,indexing_titulo)
                    if resultado ==-1 or resultado ==None:
                        print("El libro no esta en nuestra base de datos")
                    else:
                        cota=resultado[-1]

                        cota_numero = cota[6:]
                        cota_letras = cota[0:6]

                        hash = hash_function(cota_letras,int(cota_numero))

                        if hash ==0:
                            if not hash_list.Vacio():
                                resultado = hash_list.Search(cota)
                                if resultado != None:
                                    print(resultado.data)
                                    break
                            else:
                                print("La lista esta vacia")
                                break
                        else:
                            if not hash_list2.Vacio():
                                resultado = hash_list2.Search(cota)
                                if resultado != None:
                                    print(resultado.data)
                                    break
                            else:
                                print("La lista esta vacia")
                                break

        else:

            while True:
                print("\nEl serial de 12 digitos, es un numero unico de libro puesto por la editorial")
                serial = input("Ingrese el serial del libro (ejem: 000012345678): ")
            
                if(len(serial) == 12) and (serial.isdigit()):
                    resultado=busquedaBinaria(int(serial),0,len(indexing_serial),0,indexing_serial)
                    if resultado ==-1 or resultado ==None:
                        print("El libro no esta en nuestra base de datos")
                    else:
                        cota=resultado[-1]

                        cota_numero = cota[6:]
                        cota_letras = cota[0:6]

                        hash = hash_function(cota_letras,int(cota_numero))

                        if hash ==0:
                            if not hash_list.Vacio():
                                resultado = hash_list.Search(cota)
                                if resultado != None:
                                    print(resultado.data)
                                    break
                            else:
                                print("La lista esta vacia")
                                break
                        else:
                            if not hash_list2.Vacio():
                                resultado = hash_list2.Search(cota)
                                if resultado != None:
                                    print(resultado.data)
                                    break
                            else:
                                print("La lista esta vacia")
                                break

    elif int(opcion) ==3:

        while True:
            
            print("\nLa cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            cota_numero = cota[6:]
            cota_letras = cota[0:6]
            
            if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                hash = hash_function(cota_letras,int(cota_numero))
                if hash ==0:
                    if not hash_list.Vacio():
                        resultado = hash_list.Search(cota)
                        if resultado != None:
                            if resultado.data[3] !=0:
                                disponibles = resultado.data[3] -1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],disponibles,resultado.data[4]]
                                hash_list.Actualizar(resultado,disponibles_nodo)
                                write_on_file(hash_list)
                                prestados = resultado.data[4] +1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],resultado.data[3],prestados]
                                hash_list.Actualizar(resultado,disponibles_nodo)
                                write_on_file(hash_list)
                                print(f"\nSe presto el libro: {resultado.data[1]} , tiene {disponibles} disponibles y {prestados} prestados")
                            else:
                                print("Ya no se pueden prestar mas libros")
                        else:
                            print("No se encontro el libro")
                    else:
                        print("La lista esta vacia")
                    break
                else:
                    if not hash_list2.Vacio():
                        if resultado != None:
                            if resultado.data[3] !=0:
                                disponibles = resultado.data[3] -1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],disponibles,resultado.data[4]]
                                hash_list2.Actualizar(resultado,disponibles_nodo)
                                write_on_file2(hash_list)
                                prestados = resultado.data[4] +1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],resultado.data[3],prestados]
                                hash_list2.Actualizar(resultado,disponibles_nodo)
                                write_on_file2(hash_list2)
                                print(f"\nSe presto el libro: {resultado.data[1]} , tiene {disponibles} disponibles y {prestados} prestados")
                            else:
                                print("Ya no se pueden prestar mas libros")
                        else:
                            print("No se encontro el libro")
                    else:
                        print("La lista esta vacia")
                    break
    elif int(opcion) ==4:

        while True:
            
            print("\nLa cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            cota_numero = cota[6:]
            cota_letras = cota[0:6]
            
            if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                hash = hash_function(cota_letras,int(cota_numero))
                if hash ==0:
                    if not hash_list.Vacio():
                        resultado = hash_list.Search(cota)
                        if resultado != None:
                            if resultado.data[4] !=0:
                                disponibles = resultado.data[3] +1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],disponibles,resultado.data[4]]
                                hash_list.Actualizar(resultado,disponibles_nodo)
                                prestados = resultado.data[4] -1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],resultado.data[3],prestados]
                                hash_list.Actualizar(resultado,disponibles_nodo)
                                write_on_file(hash_list)
                                print(f"\nSe devolvio el libro: {resultado.data[1]} , tiene {disponibles} disponibles y {prestados} prestados")
                            else:
                                print("Ya no se pueden devolver mas libros")
                        else:
                            print("No se encontro el libro")
                    else:
                        print("La lista esta vacia")
                    break
                else:
                    if not hash_list2.Vacio():
                        if resultado != None:
                            if resultado.data[4] !=0:
                                disponibles = resultado.data[3] +1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],disponibles,resultado.data[4]]
                                hash_list2.Actualizar(resultado,disponibles_nodo)
                                prestados = resultado.data[4] -1
                                disponibles_nodo = [resultado.data[0],resultado.data[1],resultado.data[2],resultado.data[3],prestados]
                                hash_list2.Actualizar(resultado,disponibles_nodo)
                                write_on_file2(hash_list2)
                                print(f"\nSe devolvio el libro: {resultado.data[1]} , tiene {disponibles} disponibles y {prestados} prestados")
                            else:
                                print("Ya no se pueden devolver mas libros")
                        else:
                            print("No se encontro el libro")
                    else:
                        print("La lista esta vacia")
                    break
    else:

        while True:
            
            print("\nLa cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            cota_numero = cota[6:]
            cota_letras = cota[0:6]
            
            if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                hash = hash_function(cota_letras,int(cota_numero))
                if hash ==0:
                    if not hash_list.Vacio():
                        resultado = hash_list.Search(cota)
                        if resultado != None:
                            hash_list.Delete(resultado.data)
                            write_on_file(hash_list)
                            index_serial=busquedaBinariaindex(int(resultado.data[2]),0,len(indexing_serial),0,indexing_serial)
                            index_titulo=busquedaBinariaindex2(resultado.data[1],0,len(indexing_titulo),0,indexing_titulo)
                            indexing_serial.pop(index_serial)
                            indexing_titulo.pop(index_titulo)
                            print(f"El libro {resultado.data[1]} ha sido eliminado")
                            break
                        else:
                            print("La Cota no existe")
                    else:
                        print("No hay nada en la base de datos")
                        break
                else:
                    if not hash_list2.Vacio():
                        resultado = hash_list2.Search(cota)
                        if resultado != None:
                            hash_list2.Delete(resultado.data)
                            write_on_file2(hash_list2)
                            index_serial=busquedaBinariaindex(int(resultado.data[2]),0,len(indexing_serial),0,indexing_serial)
                            index_titulo=busquedaBinariaindex2(resultado.data[1],0,len(indexing_titulo),0,indexing_titulo)
                            indexing_serial.pop(index_serial)
                            indexing_titulo.pop(index_titulo)
                            print(f"El libro {resultado.data[1]} ha sido eliminado")
                            break
                        else:
                            print("La Cota no existe")
                    else:
                        print("No hay nada en la base de datos")
                        break

    Main()

def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)

def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda][0]
    while True:
        while arreglo[izquierda][0] < pivote:
            izquierda += 1
        while arreglo[derecha][0] > pivote:
            derecha -= 1
        if izquierda >= derecha:
            return derecha
        else:
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            izquierda += 1
            derecha -= 1

def busquedaBinaria(buscar,inicio,fin,iteraciones,lista):
    if len(lista) == 0:
        return -1
    
    else:
        centro=int((fin-inicio)/2)+inicio
 
        if centro>len(lista)-1 or inicio>fin:
            return None
 
        if buscar>int(lista[centro][0]):
            return busquedaBinaria(buscar,centro+1,fin,iteraciones+1,lista)
        elif buscar<int(lista[centro][0]):
            return busquedaBinaria(buscar,inicio,centro-1,iteraciones+1,lista)
        else:
            return lista[centro]

def busquedaBinaria2(buscar,inicio,fin,iteraciones,lista):
    if len(lista) == 0:
        return -1
    
    else:
        centro=int((fin-inicio)/2)+inicio
 
        if centro>len(lista)-1 or inicio>fin:
            return None
 
        if buscar>lista[centro][0]:
            return busquedaBinaria2(buscar,centro+1,fin,iteraciones+1,lista)
        elif buscar<lista[centro][0]:
            return busquedaBinaria2(buscar,inicio,centro-1,iteraciones+1,lista)
        else:
            return lista[centro]

def busquedaBinariaindex(buscar,inicio,fin,iteraciones,lista):
    if len(lista) == 0:
        return -1
    
    else:
        centro=int((fin-inicio)/2)+inicio
 
        if centro>len(lista)-1 or inicio>fin:
            return None
 
        if buscar>int(lista[centro][0]):
            return busquedaBinariaindex(buscar,centro+1,fin,iteraciones+1,lista)
        elif buscar<int(lista[centro][0]):
            return busquedaBinariaindex(buscar,inicio,centro-1,iteraciones+1,lista)
        else:
            return centro

def busquedaBinariaindex2(buscar,inicio,fin,iteraciones,lista):
    if len(lista) == 0:
        return -1
    
    else:
        centro=int((fin-inicio)/2)+inicio
 
        if centro>len(lista)-1 or inicio>fin:
            return None
 
        if buscar>lista[centro][0]:
            return busquedaBinariaindex2(buscar,centro+1,fin,iteraciones+1,lista)
        elif buscar<lista[centro][0]:
            return busquedaBinariaindex2(buscar,inicio,centro-1,iteraciones+1,lista)
        else:
            return centro

def Dato_mal_suministrado():

    print("El dato que se le ha pedido suministrar es incorrecto, vuelva a intentarlo")
    Main()

Main()
