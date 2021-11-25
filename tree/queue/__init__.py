from typing import Any


class Node:
    def __init__(self, data: Any, post: 'Node'):
        self.value = data
        self.next = post


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# nowy węzeł na początku listy
#     def push(self, data):
#         new_n = Node(data, self.head)
#         new_n.next = self.head
#         self.head = new_n

    def push(self, data):
        new = Node(data, self.head)
        self.head = new
        if self.tail is None:
            self.tail = self.head

# nowy wezel na koncu listy
#     def append(self, data):
#         frnode = Node(data, None)
#         if self.head is None:
#             self.head = frnode
#             return
#         new = self.head
#         while new.next is not None:
#             new = new.next
#         new.next = frnode

    def append(self, data):
        new = Node(data, None)
        if self.tail is None:
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        if self.head is None:
            self.head = self.tail

# printowanie mojej listy
#     def print_list(self):
#         if self.head is None:
#             print("Lista nie ma elementów")
#         else:
#             new = self.head
#             while new is not None:
#                 print(new.value, " ")
#                 new = new.next

# metoda __str__
    def __str__(self):
        if self.head is None:
            print("Lista nie posiada elementów")
            return
        pom = self.head
        lista = str(pom.value)
        while pom.next is not None:
            pom = pom.next
            lista += ' -> ' + str(pom.value)
        return lista

# zwraca węzeł znajdujący się na wskazanej pozycji

    # def node(self, at: int):
    #     licznik = 0
    #     if self.head is None:
    #         print("Lista pusta")
    #     pom = self.head
    #     while licznik < at:
    #         if pom is None:
    #             print("Brak elementu na tej liscie, szukaj dalej")
    #             break
    #         pom = pom.next
    #         licznik += 1
    #     print(pom.value)

    def node(self, at: int) -> Node:
        licznik = 0
        if self.head is None:
            print('Lista pusta')
            return
        pom = self.head
        while licznik < at:
            if pom is None:
                print('Brak elementu')
                break
            pom = pom.next
            licznik += 1
        return pom

    def insert(self, data: Any, after: Node):
        if self.head is None:
            print("Pusta lista")
            return
        pom = self.head
        while pom is not after:
            pom = pom.next
        new = Node(data, pom.next)
        pom.next = new
        if pom == self.tail:
            self.tail = Node(data, None)

    def pop(self) -> Any:
        if self.head is None:
            print('Lista pusta')
            return
        if self.head.next is None:
            self.tail = self.head
        pop_ = self.head
        self.head = self.head.next
        return pop_.value

    def remove_last(self) -> Any:
        if self.head is None:
            print('Lista pusta')
            return
        pom = self.head
        if pom.next is None:
            self.head = None
            return pom.value
        while pom.next.next is not None:
            pom = pom.next
        remove_last_ = pom.next
        pom.next = None
        self.tail = pom
        return remove_last_.value

    def remove(self, after: Node):
        if self.head is None:
            print("Pusta lista")
            return
        pom = self.head
        while pom is not after:
            pom = pom.next
        if pom.next is None:
            return
        pom.next = pom.next.next

    def __len__(self):
        licznik = 0
        pom = self.head
        while pom is not None:
            pom = pom.next
            licznik += 1
        return licznik


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any):
        self._storage.append(element)

    def pop(self):
        return self._storage.remove_last()

    def __str__(self) -> str:
        if self._storage.head is None:
            print('Stos pusty')
        temps = self._storage
        mystack = str(temps.pop())
        helper = self._storage.head
        while helper is not None:
            mystack += '\n' + str(temps.pop())
            helper = helper.next
        return mystack

    def __len__(self):
        licznik = 0
        helper = self._storage.head
        while helper is not None:
            helper = helper.next
            licznik += 1
        return licznik


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self):
        return self._storage.head.value

    def enqueue(self, element: Any):
        self._storage.append(element)

    def dequeue(self):
        return self._storage.pop()

    def __str__(self):
        if self._storage.head is None:
            print('Kolejka pusta')
            return
        helper = self._storage.head
        mqueue = str(helper.value)
        while helper.next is not None:
            helper = helper.next
            mqueue += ', ' + str(helper.value)
        return mqueue

    def __len__(self) -> int:
        licz = 0
        helper = self._storage.head
        while helper is not None:
            helper = helper.next
            licz += 1
        return licz


li = LinkedList()
assert li.head is None

li.push(1)
li.push(0)
assert str(li) == '0 -> 1'

li.append(9)
li.append(10)
assert str(li) == '0 -> 1 -> 9 -> 10'

middle = li.node(at=1)
li.insert(5, after=middle)
# print(li)
assert str(li) == '0 -> 1 -> 5 -> 9 -> 10'
# #
first_element = li.node(at=0)
returned_first_element = li.pop()
assert first_element.value == returned_first_element
#
last_element = li.node(at=3)
returned_last_element = li.remove_last()
#
# print(li)
assert last_element.value == returned_last_element
assert str(li) == '1 -> 5 -> 9'
#
second_node = li.node(at=1)
li.remove(second_node)
assert str(li) == '1 -> 5'
#
# #..............................................
stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2