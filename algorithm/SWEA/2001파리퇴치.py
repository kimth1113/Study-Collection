import sys
sys.stdin = open('2001파리퇴치.txt', 'r')

# 2001 파리퇴치 D2

def check(Arr, n, m):
    total = 0
    for i in range(n, n+M):
        for j in range(m, m+M):
            total += Arr[i][j]

    return total

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # n은 0부터 N-M까지
    # m은 M-1부터 N-1까지
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if best < check(arr, i, j):
                best = check(arr, i, j)

    print(f'#{tc} {best}')