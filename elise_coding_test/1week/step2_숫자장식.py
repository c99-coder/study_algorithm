# itertools의 product 메소드 임포트
from itertools import product

# 예시
# '4 2' 문자열을 받아 split() -> 기본값인 공백 기준으로 나눠 리스트로 반환
# ['4', '2'] map()을 사용하여 리스트의 요소를 하나씩 꺼내어 int로 변경후 map오브젝트로 반환
# map오브젝트(4, 2)의 값을 N, M에 저장
N, M = map(int, input().split())

# items에 N만큼의 숫자열을 M개 저장
# 예시
# 입력: 4 2
# items = [['1','2','3','4'], ['1','2','3','4']]
# 후에서 join하기 위해 문자열로 저장 -> line:19
items = [[str(i) for i in range(1, N+1)]] * M

# items 의 리스트들을 product 하고, 숫자사이에 공백을 위한 join 후 출력
# 참고: https://velog.io/@davkim1030/Python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-product-itertools
for i in product(*items):
    print(' '.join(i))
