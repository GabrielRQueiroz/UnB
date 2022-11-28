class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ""
        while tmp != None:
            lstr += str(tmp.data) + " "
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
print(L)


def inverterLista(L: UnorderedList):
    # Escreva sua solução aqui

    # invertedL = UnorderedList()

    # for _ in range(L.size()):
    #     invertedL.add(L.head.getData())
    #     L.remove(L.head.getData())

    # return invertedL

    previousNode = None
    currentNode = L.head

    for _ in range(L.size() - 1):
        nextNode = currentNode.getNext()

        currentNode.setNext(previousNode)

        previousNode = currentNode

        currentNode = nextNode

    L.head = previousNode

    return L


print(inverterLista(L))
