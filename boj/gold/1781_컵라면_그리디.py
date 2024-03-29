# 220730
# 나동빈님 풀이
import heapq

n = int(input())
array = []
q = []

# 문제 정보를 입력 받은 이후에, 데드라인을 기준으로 정렬
for i in range(n):
    a, b = map(int, input().split(' '))
    array.append((a, b))
array.sort()

for i in array:
    a = i[0]  # i[0] - 데드라인
    heapq.heappush(q, i[1])  # i[1] - 컵라면 개수
    # 데드라인을 초과하는 경우에는 최소 원소를 제거
    if a < len(q):
        heapq.heappop(q)

print(sum(q))
