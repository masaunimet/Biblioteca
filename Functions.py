#Función hash, toma el key, lo convierte en su equivalente ascii y toma el residuo de la división entre 2


def hash_function(string):
    hash_value = 0
    for i in range(6):
        hash_value = hash_value + ord(string[i])
    for i in range(6,8):
        hash_value = hash_value + int(string[i])
    hash_value = hash_value%2
    print(hash_value)

    return hash_value
        