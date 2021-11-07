import sys
sys.stdin = open('123.txt', 'r')

words = input().split()

A = words[0]
B = words[1]

j = 0 # B의 인덱스
minCnt = 9999999999
while len(B) - j >= len(A):
    cnt = 0
    i = 0 # A의 인덱스

    while i < len(A):
        if A[i] != B[j]:
            cnt += 1
        i += 1 
        j += 1
        
    if cnt < minCnt:
        minCnt = cnt
    j = j - len(A) + 1 # B의 첫 인덱스를 (+1)

print(minCnt)