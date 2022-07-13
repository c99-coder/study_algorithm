import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))

sum, max, min = 0, -4000, 4000
dict_a = {}

for num in l:
    # 1
    sum += num

    # 3
    if num not in dict_a:
        dict_a[num] = 1
    else:
        dict_a[num] += 1

    # 4
    if max < num:
        max = num

    if min > num:
        min = num

sorted_dict = sorted(dict_a.items(), key=lambda item: item[1], reverse=True)
unique_dict = set(dict_a.values())
# print(dict_a.values(), unique_dict, sorted_dict)

if len(sorted_dict) > 1 and sorted_dict[0][1] == sorted_dict[1][1]:
    list_a = []
    for key, value in dict_a.items():
        if value == sorted_dict[0][1]:
            list_a.append(key)
    list_a.sort()
    answer_3 = list_a[1]
else:
    answer_3 = sorted_dict[0][0]


print(round(sum/N))
print(sorted(l)[N//2])
print(answer_3)
print(max - min)
