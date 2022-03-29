import numpy as np
from List import *
from Functions import *

prueba = Linked_list()
prueba2 = Linked_list()


 #########################################################

prueba.append(1)
prueba.append(2)
prueba.append(3)
prueba.append(4)
prueba.append(5)
prueba.append(6)
prueba.append(7)
prueba.append(8)
prueba.append(9)
prueba.append(10)
prueba.append(11)
prueba.append(12)
prueba.append(13)
prueba.append(14)
prueba.append(15)
prueba.append(16)
prueba.append(17)
prueba.append(18)
prueba.append(19)
prueba.append(20)
prueba.append(21)
prueba.append(54)

prueba.print_list()
prueba.Actualizar(prueba.Search(21),34)
print('--------------------------------')
prueba.print_list()
print('--------------------------------')
prueba.Delete(34)
prueba.print_list()
print('--------------------------------')
prueba.Delete(20)
prueba.print_list()
print('--------------------------------')
prueba.Delete(19)
prueba.print_list()
print('--------------------------------')
prueba.append(18)
prueba.append(19)
prueba.append(20)
prueba.append(21)
prueba.append(54)
print('--------------------------------')

#########################################################

lineas_Facheras = "------------------------------------------------------"
mensaje_Intro = "Bienvenido a la Libreria Publica de Manhattan!\n\nQue desea hacer?\n1. Insertar un nuevo libro\n2. Buscar un libro\n3. Prestar un libro\n4. Devolver un libro\n5. Eliminar libro"

def Inicio():
    print(lineas_Facheras)
    print(mensaje_Intro)
    

def Main():

    Inicio()
    opcion = input('Ingrese el numero de la operacion:' )

    if opcion.isdigit :
        
        if int(opcion) >=1 and int(opcion) <=5:

            Opcion(opcion)
        else:

            Dato_mal_suministrado()
    else:

        Dato_mal_suministrado()

def Opcion(opcion):

    if int(opcion) ==1:

        while True:
            
            print("La cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            cota_numero = cota[6:]
            cota_letras = cota[0:6]
            
            if (not cota_numero.isalpha()) and (not cota_letras.isdigit()):

                break

        while True:
            print("El titulo es un nombre unico de libro con un maximo de 30 caracteres")
            titulo = input("Ingrese el titulo del libro (ejem: El Principito): ")
            
            if(not len(titulo) <= 30):
               
                break
            else:
                titulo = int(titulo)

        while True:
            print("El serial de 12 digitos, es un numero unico de libro puesto por la editorial")
            serial = input("Ingrese el serial del libro (ejem: 000012345678): ")
               
            if(not len(serial) <= 10) or (not serial.isdigit()):
                
                break
            else:
                serial = int(serial)

        while True:
            
            disponibles = input("Ingrese el numero de libros disponibles: ")
            
            if(not disponibles.isdigit()):
                    
                break
                
        while True:
            
            prestados = input("Ingrese el numero de libros prestados: ")
            
            if(not prestados.isdigit()):
                
                break
                
    elif int(opcion) ==2:

        print("buscar libro")
    elif int() ==3:

        print("Prestar libro")
    elif int() ==4:

        print("Devolver libro")
    else:

        print("Eliminar libro")
    
    titulo = int(titulo)
    cota = int(cota)
    serial = int(serial)
    matriz1(cota, titulo)
    matriz2(cota, serial)

def matriz1(cota, titulo):
    
    arr = np.array([[cota, titulo]])        
    
def matriz2(cota, serial):
    
    arr = np.array([[cota, serial]])        

def ordenar(arr):

    arr[arr[:, 0].argsort()]


cota = input("Cota")
cota = int(cota)
titulo = input("titulo")
L = "Cota"
K = "Titulo"
arr = np.array([[L, K]])
AgregarMatriz1(arr, cota, titulo)
BuscarMatriz1(arr, cota, titulo)
EliminarMatriz1(arr, cota, titulo)

def AgregarMatriz1(arr, cota, titulo):

    row = np.array([[cota, titulo]])
    arr = np.vstack([arr, row])
    print(arr)

def BuscarMatriz1(arr, cota, titulo):
   
    index = np.where((arr == (cota, titulo)).all(axis=1))
    print("Se encontro el elemento")
    print(arr)

def EliminarMatriz1(arr, cota, titulo):

    index = np.where((arr == (cota, titulo)).all(axis=1))
    delete = np.delete(arr, index, 0)
    print("Se elimino el elemento")
    print(arr)
    
def Dato_mal_suministrado():

    print("El dato que se le ha pedido suministrar es incorrecto, vuelva a intentarlo")
    Main()

Main()
