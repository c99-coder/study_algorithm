# deque에서 popleft를 사용해 시간을 단축하자..!
# appendleft, popleft 사용시 시간복잡도 비교: https://poorman.tistory.com/412
from collections import deque

pos1, pos2 = map(int, input().split())  # pos1: 경찰위치, pos2: 범인위치

# 경찰위치를 넣은 deque 선언
queue1 = deque([pos1])

# 몇초가 지났는지 확인하는 변수
second = 0

# set을 사용하여 in 함수 사용시 속도를 빠르게하기!
# 사용법: https://wikidocs.net/1015
# 특징: https://naon.me/posts/til38
# list, deque, set, dict 시간복잡도 비교: https://wiki.python.org/moin/TimeComplexity
visited = set()

# 2중 반복을 빠져나가기 위한 flag
flag = True

while flag:  # flag가 False면 탈출
    for _ in range(len(queue1)):  # queue1에 있는 값이 second 단위로 1번씩 실행되도록 반복
        node = queue1.popleft()  # deque의 왼쪽부터 값을 꺼내 node에 저장
        if node == pos2:  # 경찰이 범인 위치와 같으면 for문 종료 -> line:41
            flag = False
            break
        if (node not in visited and  # node의 숫자가 visited에 없는 숫자이며,
                1 <= node <= 100000):  # 문제에 있는 node의 제한 범위를 넘지 않으면 실행
            visited.add(node)  # 현재 node의 숫자를 visited에 추가

            # 현재 node가 범인(pos2)보다 앞에 있다면 모든 경우 탐색, 뒤에 있다면 뒤쪽으로만 탐색 -> 삼항연산자 사용
            nextStep = ([node + 1, node * 3, node - 1]
                        if node < pos2
                        else [node - 1])

            # queue1에 다음 second에 갈 예정인 값을 추가
            queue1.extend(nextStep)

    # 경찰이 범인 위치와 같으면 second를 더하지 않음
    if flag:
        second += 1

print(second)
