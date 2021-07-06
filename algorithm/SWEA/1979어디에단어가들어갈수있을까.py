import sys
sys.stdin = open('1979어디에단어가들어갈수있을까.txt', 'r')

def check(Arr, k):
    for i in range(len(Arr)):
        cnt = 0
        for j in range(len(Arr)-k+1):
            if Arr[i][j] == Arr[i][j+1]:
                cnt += 1

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(arr, N, K, arr, N, K)