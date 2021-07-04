import sys
sys.stdin = open('1970쉬운거스름돈.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    
    while N > 9:
        if N >= 50000:
            N -= 50000
            a += 1
        elif N >= 10000:
            N -= 10000
            b += 1
        elif N >= 5000:
            N -= 5000
            c += 1
        elif N >= 1000:
            N -= 1000
            d += 1
        elif N >= 500:
            N -= 500
            e += 1
        elif N >= 100:
            N -= 100
            f += 1
        elif N >= 50:
            N -= 50
            g += 1
        else:
            N -= 10
            h += 1

    print(f'#{tc} \n{a} {b} {c} {d} {e} {f} {g} {h}')