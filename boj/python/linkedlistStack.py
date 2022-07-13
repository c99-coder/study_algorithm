import sys


class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            self.tail = self.head
        else:
            node = self.tail
            self.tail = Node(data, None, node)
            node.next = self.tail
        self.len += 1

    def pop(self):
        if self.head is None:
            return -1
        else:
            node = self.tail
            self.tail = self.tail.prev

            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None

            self.len -= 1
            return node.data

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return -1 if self.len == 0 else self.tail.data


sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

stack = Stack()
for _ in range(n):
    oper = input().strip().split()
    if oper[0] == 'push':
        stack.push(oper[1])
    elif oper[0] == 'top':
        print(stack.top())
    elif oper[0] == 'size':
        print(stack.size())
    elif oper[0] == 'pop':
        print(stack.pop())
    elif oper[0] == 'empty':
        print(stack.empty())
