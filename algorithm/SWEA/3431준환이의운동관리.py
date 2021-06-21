import sys
sys.stdin = open('3431준환이의운동관리.txt', 'r')

# 3431 준환이의 운동관리 D3

TC = int(input())
for tc in range(1, TC+1):
    L, U, X = map(int, input().split())

    result = 0
    if X < L:
        result =  L - X
    elif U < X:
        result = -1
    
    print(f'#{tc} {result}')
    
    
