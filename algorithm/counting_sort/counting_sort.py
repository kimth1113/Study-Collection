org = [1, 0, 1, 5, 4, 3, 1, 4, 5, 2, 1]

cnt_arr = [0] * 6

for i in range(len(org)):
    cnt_arr[org[i]] += 1

for i in range(0, len(cnt_arr)-1):
    cnt_arr[i+1] += cnt_arr[i] # 1  5  6  7  9  11

cnt_list = [0] * 11
for i in org:
    cnt_list[cnt_arr[i]-1] = i
    cnt_arr[i] -= 1

print(cnt_list)