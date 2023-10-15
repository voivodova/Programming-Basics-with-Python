town = input()
sales = float(input())
commission = 0
if town == 'Sofia':
    if 0 <= sales <= 500:
        commission = sales * 0.05
    if 500 < sales <= 1000:
        commission = sales * 0.07
    if 1000 < sales <= 10000:
        commission = sales * 0.08
    if sales > 10000:
        commission = sales * 0.12


elif town == 'Varna':
    if 0 <= sales <= 500:
        commission = sales * 0.045
    if 500 < sales <= 1000:
        commission = sales * 0.075
    if 1000 < sales <= 10000:
        commission = sales * 0.10
    if sales > 10000:
        commission = sales * 0.13


elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = sales * 0.055
    if 500 < sales <= 1000:
        commission = sales * 0.08
    if 1000 < sales <= 10000:
        commission = sales * 0.12
    if sales > 10000:
        commission = sales * 0.145

if commission > 0:
    print(f'{commission:.2f}')

else:
    print('error')