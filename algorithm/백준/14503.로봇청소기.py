import sys
sys.stdin = open('456.txt', 'r')

def countSpace(r, c, d, Arr):
    curR = r
    curC = c
    Arr[curR][curC] = 2
    cnt = 1

    # 북 동 남 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    fail = 0
    while True:
        if d == 0:
            d = 4
        d -= 1

        # 다음 왼쪽 공간
        nr = curR + dr[d]
        nc = curC + dc[d]

        # 다음 왼쪽 공간이 범위 내 있을 때
        if (0 <= nr < len(Arr)) and (0 <= nc < len(Arr[0])):
            if Arr[nr][nc] > 0:
                fail += 1
                
            else:
                curR = nr
                curC = nc
                Arr[curR][curC] = 2
                cnt += 1

        # 다음 지점이 범위 밖에 있을 때
        else:
            fail += 1

        # 청소할 곳이 없을 때
        if fail == 4:

            if d == 0:
                d = 4
            d -= 1

            nr = curR + dr[d]
            nc = curC + dc[d]

            if Arr[nr][nc] == 1:
                return cnt
            elif Arr[nr][nc] == 2:
                curR = nr
                curC = nc
                fail = 0
            else:
                curR = nr
                curC = nc
                fail = 0
                Arr[curR][curC] = 2
            
TC = 2
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    cr, cc, de = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(countSpace(cr, cc, de, arr))
