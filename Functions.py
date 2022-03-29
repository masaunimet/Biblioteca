import pickle

#Función hash, toma el key, lo convierte en su equivalente ascii y toma el residuo de la división entre 2

def hash_function(string,numero):
    hash_value = 0
    for letter in string:
        hash_value +=  ord(letter)
    hash_value += numero
    hash_value = hash_value%2

    return hash_value

#Funcion para ecribir la lista en el archivo

def write_on_file(list):
    with open('database.txt','wb') as f:
        pickle.dump(list,f)

def read_file():
    with open('database.txt', 'rb') as f:
        lista = pickle.load(f)
        return lista

def write_on_file2(list):
    with open('database2.txt','wb') as f:
        pickle.dump(list,f)

def read_file2():
    with open('database2.txt', 'rb') as f:
        lista = pickle.load(f)
        return lista
        