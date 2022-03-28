

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, altura=0):
        self.first = Node()
        self.last = Node()
        self.altura = altura
        self.overflow = None
        self.size = 0

    #agarrar la altura más alta de los overflow o base
    def GetLastAltura(self):
        if self.overflow != None:
            return self.overflow.GetLastAltura()
        else:
            return self.altura

    #Agregar nodos a la lista

    def append(self, data):
        if not self.size >=3 and self.altura <=6:
            new_node = Node(data)
            aux = self.first
            while aux.next != None:
                aux = aux.next
            aux.next = new_node
            self.size = self.size + 1 
        else:
            if (self.GetLastAltura() != None) and (self.GetLastAltura() <=6):
                if self.overflow == None:
                    self.overflow = Linked_list(self.altura+1)
                self.overflow.append(data)
            else:
                print("no se puede colocar mas contenido")


    #Buscar lista

    def Search(self,data):
        aux = self.first
        while(aux.next != None):
            if aux.data == data:
                return aux
            aux = aux.next
        if aux.data == data:
            return aux
        if self.overflow != None:
            return self.overflow.Search(data)
        else:
            return None

    #Actualizar lista

    def Actualizar(self,data):
        aux = self.first
        while(aux.next != None):
            if aux.data == data:
                return aux
            aux = aux.next
        if aux.data == data:
            return aux
        if self.overflow != None:
            return self.overflow.Search(data)
        else:
            return None

    #Mostrar lista

    def print_list(self):
        aux = self.first
        while aux.next != None:
            aux = aux.next     
            print(aux.data)
        if self.overflow != None:
            self.overflow.print_list()