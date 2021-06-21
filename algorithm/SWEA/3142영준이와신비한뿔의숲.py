import sys
sys.stdin = open('3142영준이와신비한뿔의숲.txt', 'r')

def devAnimal(n, m):
    unicorn = 0
    twinHorn = 0

    if n == m:
        unicorn = m
        return [unicorn, twinHorn]

    while n > m: 
        n -= 2
        m -= 1
        twinHorn += 1

    unicorn = n

    return [unicorn, twinHorn]

TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    arr = devAnimal(N, M)

    print(f'#{tc} {arr[0]} {arr[1]}')