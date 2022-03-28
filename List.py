

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

    def __BorrarOverflow(self):
        if self.altura != 6:
            if self.overflow != None:
                self.overflow.__BorrarOverflow()
            else:
                return
        else:
            self.overflow = None

    #Agregar nodos a la lista

    def append(self, data):
        if not self.size >=3 and self.altura <=6:
            new_node = Node(data)
            if self.size ==0:
                self.first = new_node
                self.last = new_node
            else:
                self.last.next = new_node
                self.last = new_node
            self.size = self.size + 1 
        else:
            if (self.GetLastAltura() != None) and (self.GetLastAltura() <=6):
                if self.overflow == None:
                    self.overflow = Linked_list(self.altura+1)
                self.overflow.append(data)
            else:
                print("no se puede colocar mas contenido")
        
        self.__BorrarOverflow()

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

    def Actualizar(self,node,data):
        aux = self.first
        while(aux.next != None):
            if aux == node:
                aux.data = data
            aux = aux.next
        if aux == node:
            node.data = data
        if self.overflow != None:
            return self.overflow.Actualizar(node,data)
        else:
            return None

    #Eliminar Nodo

    def Delete(self,data):
        ant = self.first
        aux = self.first
        while(aux.next != None):
            if aux.data == data:
                self.__TrueDelete(ant,aux)
            ant = aux
            aux = aux.next
        if aux.data == data:
            self.__TrueDelete(ant,aux)
        if self.overflow != None:
            self.overflow.Delete(data)
        self.__Limpiar()
    
    #Part 2
    def __TrueDelete(self,ant,aux):
        if aux == self.first:
            if self.first == self.last:
                self.last = None
            self.first = aux.next
            self.__PullList()
        elif aux == self.last:
            if self.overflow != None:
                ant.next = self.overflow.first #el anterior va a valer el primero del overflow
                self.overflow.first = self.overflow.first.next #el primero de la lista en el overflow va a ser el siguiente
                self.last = ant.next # el ultimo va a ser lo que era antes el primero del overflow
                self.last.next = None # el puntero al siguiente del ultimo va a ser none
                self.overflow.__PullList()
            else:
                ant.next = None
                self.last = ant
                self.size -=1
        else:
            ant.next = aux.next
            if aux == self.last:
                self.last = aux
            self.__PullList()
    
    #Empujar los elementos 
    def __PullList(self):
        if self.overflow != None:
            self.last.next = self.overflow.first
            self.overflow.first = self.overflow.first.next
            self.last = self.last.next
            self.last.next = None
            if self.overflow.last == self.last:
                self.overflow = None
            else:
                self.overflow.__PullList()
        else:
            self.size -=1

    #Quitar overflow sin contenido

    def __Limpiar(self):
        if self.overflow != None and self.overflow.first == None:
            self.overflow = None
        else:
            if(self.overflow != None):
                self.overflow.__Limpiar()

    #Mostrar lista

    def print_list(self):
        aux = self.first
        while aux.next != None:
            print(aux.data)
            aux = aux.next   
        print(aux.data)
        if self.overflow != None:
            self.overflow.print_list()