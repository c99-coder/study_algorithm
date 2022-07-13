from itertools import product


def solution(user_id, banned_id):
    length = len(banned_id)
    result = [[] for _ in range(length)]
    for i, x in enumerate(banned_id):
        for y in user_id:
            if len(x) != len(y):
                continue
            for a, b in zip(x, y):
                if a == '*':
                    continue
                if a == b:
                    continue
                else:
                    break
            else:
                result[i].append(y)

    product_list = list(product(*result))

    # print(product_list)

    result = set()
    for x in product_list:
        if length == len(set(x)):
            result.add(tuple(sorted(x)))

    # print(result)

    return len(result)


print(solution(["aaaaaaaa", "bbbbbbbb", "cccccccc"],
      ['********', '********', '********']))
