# 220812

'''
아이디어:
이동 횟수를 최소화하기 위해서는 처음에는 최대한 가속해야 한다.
그러나 마지막에는 1만큼만 이동해야 하기 때문에 감속해야 한다.
그러면 1을 포함한 증가, 감소 수열이 생기게 된다.
ex) n = 3 일 때, 1 2 3 3 2 1 -> 이동 횟수: 2 * n = 2 * 3 번 이동
목적지 까지의 거리에서 증가, 감소 수열의 이동 거리 n * (n + 1)를 빼고 - 1 ~ n 까지 자연수의 합 * 2
(남은 거리)를 증가, 감소 수열의 중간에 끼워 넣어 채운다.
증가, 감소 수열의 합은 n -> n + 1일 때 2n + 2만큼 증가하기 때문에
(남은 거리)의 범위는 1 ~ 2n + 1이다.
1 ~ n + 1 만큼 남았다면 1회만 더 이동하면 된다.
n + 1은 n과 n 사이에 끼워넣으면 되고 1 ~ n은 같은 숫자 옆에 놓으면 되기 때문.
n + 2 ~ 2n + 1만큼 남았다면 n + 1을 n과 n 사이에 끼워넣고
다시 남은 거리 만큼을 같은 숫자 옆에 놓으면 된다.
'''

import sys; input = sys.stdin.readline


def count(d):
    if d == 1:  # 거리가 1일 때
        return 1

    n = 0  # n 설정
    while (n + 1) * (n + 2) < d:
        n += 1

    if (n + 1) * (n + 2) == d:  # 증가, 감소 수열로 나눠 떨어지는 경우
        n += 1
        return 2 * n

    # 증가, 감소 수열을 빼고 남은 거리에 따라 횟수 계산
    if 1 <= d - n * (n + 1) <= n + 1:             
        return 2 * n + 1

    if n + 2 <= d - n * (n + 1) <= 2 * n + 1:
        return 2 * n + 2


for T in range(int(input().rstrip())):
    x, y = map(int, input().split())
    print(count(y - x))