import sys
sys.stdin = open('456.txt', 'r')

def first():
    global prev
    j = i + 2
    while (0 <= j < len(signal)-1) and signal[j] == 0:
        j += 1
        if j == len(signal):
            print('NONE')
            break
    for idx in range(i-1, j+1):
        signal[idx] = 2
    prev = 1

TC = 2
for tc in range(1, TC+1):
    numbers = input()
    signal = [int(number) for number in numbers]
    
    cnt = 100
    prev = 2
    result = 0
    while cnt:
        for i in range(1, len(signal)-1):
            if signal[i-1] == 1 and signal[i] == 0 and signal[i+1] == 0:
                first()

            elif signal[i-1] == 0:
                if prev != 1 and signal[i] == 0:
                    print('NONE')
                    result = 1
                    break
                elif prev == 1 and signal[i] == 0:
                    first()

                elif prev == 1 and signal[i] == 1:
                    signal[i-1] = 2
                    signal[i] = 2
                    prev = 1

            elif signal[i-1] == 1:
                if prev == 1 and signal[i-1] == 1 and signal[i] == 0 and signal[i+1] == 0:
                    first()
                elif prev != 1

        if result:
            break

        if cnt == 1:
            for k in range(len(signal)):
                if k != 3:
                    print('NONE')
                    result = 1
                    break
            if result:
                break
            result = 1
            print('SUMMARY')
            break
        if result:
            break

        cnt -= 1