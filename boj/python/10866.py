import sys


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, data):
        if self.empty():
            self.head = self.tail = Node(data)
        else:
            node = self.head
            self.head = Node(data, next=node)
            node.prev = self.head
        self.length += 1

    def push_back(self, data):
        if self.empty():
            self.head = self.tail = Node(data)
        else:
            node = self.tail
            self.tail = Node(data, prev=node)
            node.next = self.tail
        self.length += 1

    def pop_front(self):
        if self.empty():
            return -1
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return node.data

    def pop_back(self):
        if self.empty():
            return -1
        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1
        return node.data

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return -1 if self.empty() else self.head.data

    def back(self):
        return -1 if self.empty() else self.tail.data


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt', 'r')

deque = LinkedDeque()
N = int(input())
for _ in range(N):
    oper = input().split()
    # print(oper)
    if oper[0] == 'push_front':
        deque.push_front(oper[1])
    elif oper[0] == 'push_back':
        deque.push_back(oper[1])
    elif oper[0] == 'pop_front':
        print(deque.pop_front())
    elif oper[0] == 'pop_back':
        print(deque.pop_back())
    elif oper[0] == 'size':
        print(deque.size())
    elif oper[0] == 'empty':
        print(deque.empty())
    elif oper[0] == 'front':
        print(deque.front())
    elif oper[0] == 'back':
        print(deque.back())
