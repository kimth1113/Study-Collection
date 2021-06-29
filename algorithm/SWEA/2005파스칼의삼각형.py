import sys
sys.stdin = open('2005파스칼의삼각형.txt', 'r')

# 2005 파스칼의 삼각형 D2

def triangle(Arr, n):
    if len(Arr) <= n:
        print(*Arr)

        newArr = [0] * (len(Arr) + 1)

        newArr[0] = Arr[0]
        newArr[-1] = Arr[-1]
        if len(newArr) > 2:
            for i in range(1, len(newArr)-1):
                newArr[i] = Arr[i-1] + Arr[i]

        Arr = newArr
        return triangle(Arr, n)
    

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [1]
    print(f'#{tc}')
    triangle(arr, N)