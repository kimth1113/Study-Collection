import sys
sys.stdin = open('1974스도쿠검증.txt', 'r')

# 1974 스도쿠검증 D2

def checkBox(Arr, I, J):
    oneToNine = []
    for n in range(I, I+3):
        for m in range(J, J+3):
            oneToNine.append(Arr[n][m])

    oneToNine.sort()
    if oneToNine == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    return 0

def checkLine(Arr, K):
    oneToNine = []
    for l in range(9):
        oneToNine.append(Arr[l][K])

    oneToNine.sort()
    if oneToNine == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    return 0

def checkLine2(Arr, K):
    oneToNine = []
    for l in range(9):
        oneToNine.append(Arr[K][l])

    oneToNine.sort()
    if oneToNine == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    return 0


TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = []
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            result.append(checkBox(arr, i, j))

    for k in range(9):
        result.append(checkLine(arr, k))
        result.append(checkLine2(arr, k))

    if 0 in result:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
    