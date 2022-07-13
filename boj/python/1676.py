import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
print(N//5 + N//25 + N//125)
