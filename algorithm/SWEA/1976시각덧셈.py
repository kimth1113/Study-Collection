import sys
sys.stdin = open('1976시각덧셈.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    a, b, c, d = map(int, input().split())
    
    hourTotal = a + c
    minTotal = b + d

    if minTotal > 59:
        minTotal -= 60
        hourTotal += 1
    
    if hourTotal > 12:
        hourTotal -= 12

    print(f'#{tc} {hourTotal} {minTotal}')

