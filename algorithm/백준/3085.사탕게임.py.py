# import sys
# sys.stdin = open('456.txt', 'r')

# 3085 사탕 게임

def checkLong(Arr):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    point = 1
    for i in range(N):
        for j in range(N):
            cv = Arr[i][j]
            for k in range(4):
                cnt = 1
                nr = i + dr[k]
                nc = j + dc[k]

                while (0 <= nr < N) and (0 <= nc < N) and (Arr[nr][nc] == cv):
                    cnt += 1
                    nr += dr[k]
                    nc += dc[k]

                if cnt > point:
                    point = cnt

    return point

def changArr(Ar):
    mr = [1, 0]
    mc = [0, 1]

    maxP = 0
    for m in range(N):
        for n in range(N):
            for l in range(2):
                fr = m + mr[l]
                fc = n + mc[l]

                if (0 <= fr < N) and (0 <= fc < N):
                    Ar[m][n], Ar[fr][fc] = Ar[fr][fc], Ar[m][n]
                    
                    if checkLong(Ar) > maxP:
                        maxP = checkLong(Ar)

                    Ar[m][n], Ar[fr][fc] = Ar[fr][fc], Ar[m][n]

    return maxP

N = int(input())
arr = [[_ for _ in input()] for x in range(N)]

print(changArr(arr))