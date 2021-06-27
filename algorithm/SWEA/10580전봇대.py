import sys
sys.stdin = open('10580.txt', 'r')

# 10580 전봇대 D3

def checkPoint(p1, p2, Arr):
    point = 0

    for k in range(len(Arr)):
        if p1 < Arr[k][0] and p2 > Arr[k][1]:
            point += 1
        elif p1 > Arr[k][0] and p2 < Arr[k][1]:
            point += 1
    return point

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = []

    for i in range(N):
        A, B = map(int, input().split())
        arr.append([A, B])

    total = 0
    for [a, b] in arr:
        total += checkPoint(a, b, arr)

    total //= 2
    print(f'#{tc} {total}')
