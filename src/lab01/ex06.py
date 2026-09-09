N = int(input())

cnt1 = 0
cnt2 = 0

for _ in range(N):
    s = input().split()
    if s[-1] == 'True':
        cnt1 += 1
    else:
        cnt2 += 1

print(cnt1, cnt2)