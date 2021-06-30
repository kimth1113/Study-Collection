import sys
sys.stdin = open('1983조교의성적매기기.txt', 'r')

# 1983 조교의 성적 매기기 D2

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    grade = []
    for stu in range(N):   
        a, b, c = map(int, input().split())
        score = a * 0.35 + b * 0.45 + c * 0.2
        grade.append(score)

    scoreOfK = grade[K-1]
    grade.sort()
    grade.reverse()
    IndexOfK = grade.index(scoreOfK)

    if IndexOfK < (N // 10):
        print(f'#{tc} A+')
    elif IndexOfK < (N // 10)*2:
        print(f'#{tc} A0')
    elif IndexOfK < (N // 10)*3:
        print(f'#{tc} A-')
    elif IndexOfK < (N // 10)*4:
        print(f'#{tc} B+')
    elif IndexOfK < (N // 10)*5:
        print(f'#{tc} B0')
    elif IndexOfK < (N // 10)*6:
        print(f'#{tc} B-')
    elif IndexOfK < (N // 10)*7:
        print(f'#{tc} C+')
    elif IndexOfK < (N // 10)*8:
        print(f'#{tc} C0')
    elif IndexOfK < (N // 10)*9:
        print(f'#{tc} C-')
    else:
        print(f'#{tc} D0')
        
