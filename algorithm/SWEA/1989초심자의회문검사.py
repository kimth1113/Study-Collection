import sys
sys.stdin = open('1989초심자의회문검사.txt', 'r')

# 1989 초심자의 회문검사 D2

TC = int(input())
for tc in range(1, TC+1):
    word = []
    for x in input():
        word.append(x) 

    if len(word) % 2:
        first = word[0:len(word)//2]
        last = word[len(word)//2+1:len(word)]
        last.reverse()

    else:
        first = word[0:len(word)//2]
        last = word[len(word)//2:len(word)]
        last.reverse()

    if first == last:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
