#python3.12 --version

class Stack:
    class Pointer: # criando o endereçamento
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self): # método inicial
        self.top = None
        self.size = 0

    def pop(self): # método para remover elemento da pilha
        if self.size == 0:
            return "Pilha vazia"

        self.top = self.top.next
        self.size -= 1

    def push(self, add): # método para adicionar elemento da pilha
        newadd = self.Pointer(add)
        newadd.next = self.top
        self.top = newadd
        self.size += 1

    def __repr__(self): # método representativo da pilha
        if self.size == 0:
            return "Pilha vazia"
        
        stack = ''
        element = self.top
        while(element):
            stack += str(element.data) + '\n'
            element = element.next
        return stack


if __name__ == '__main__':
    pilha = Stack()
    pilha.push(2)
    pilha.push(8)
    print(pilha)
    pilha.pop()
    print("\n")
    print(pilha)