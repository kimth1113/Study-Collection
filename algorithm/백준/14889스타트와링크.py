import sys
sys.stdin = open('123.txt', 'r')

TC = 3
for i in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    newList = [[0] * (N-1) for _ in range(N-1)]

    for i in range(N):
        for j in range(N):
            if i < j:
                newList[i][j-1] = arr[i][j]+arr[j][i]

    newN = len(newList)
    # for i in range(newN):
    #     test = [0, ... , newN-1]
    #     for j in range(newN):

    test = list(range(0, N-1))
    print(test)

5 9 6 6 10 7
# 5 9 6 
# 0 6 10 
# 0 0 7

# 2 3 4 5 6 
# 0 4 5 6 7 
# 0 0 6 7 8 
# 0 0 0 8 9 
# 0 0 0 0 10