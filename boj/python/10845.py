import sys


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.tail
            self.tail = Node(data, prev=node)
            node.next = self.tail
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return node.data

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return self.head.data if self.head else -1

    def back(self):
        return self.tail.data if self.tail else -1


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt', 'r')

N = int(input())

queue = LinkedQueue()
for _ in range(N):
    oper = input().split()
    if oper[0] == 'push':
        queue.push(oper[1])
    elif oper[0] == 'pop':
        print(queue.pop())
    elif oper[0] == 'size':
        print(queue.size())
    elif oper[0] == 'empty':
        print(queue.empty())
    elif oper[0] == 'front':
        print(queue.front())
    elif oper[0] == 'back':
        print(queue.back())
