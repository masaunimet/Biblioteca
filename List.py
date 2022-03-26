
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.size = 0


    #Agregar nodos a la lista

    def append(self, data):
        new_node = Node(data)
        aux = self.first
        while aux.next != None:
            aux = aux.next
        aux.next = new_node
        self.size = self.size + 1 


    #Mostrar lista

    def print_list(self):
        aux = self.first
        while aux.next != None:
            aux = aux.next     
            print(aux.data)



    #No sirve - borrar

    def append_node(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.first = self.last = new_node
            self.size = self.size + 1
        else:
            aux = self.last
            aux.next = new_node
            self.last = new_node
            self.size = self.size + 1
