n = int(input())

sum1 = 0
sum2 = 0

for i in range(0, n):
    number = int(input())
    if i % 2 == 0:
        sum1 += number
    else:
        sum2 += number

diff = abs(sum1 - sum2)
if sum1 == sum2:
    print('Yes')
    print(f'Sum = {sum1}')
else:
    print('No')
    print(f'Diff = {diff}')