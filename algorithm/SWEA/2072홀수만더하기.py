import sys
sys.stdin = open("345.txt", 'r')

TC = int(input())
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))

    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            total += arr[i]

    print(f'#{tc} {total}')