#Función hash, toma el key, lo convierte en su equivalente ascii y toma el residuo de la división entre 2

def hash_function(string):
    hash_value = 0
    for letter in string:
        hash_value = hash_value + ord(letter)
    hash_value = hash_value%2
    print(hash_value)

    return hash_value
        
hash_function('gnfns')