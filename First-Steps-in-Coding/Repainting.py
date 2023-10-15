quantily_of_nylon = int(input())
quantily_of_paint = int(input())
quantily_of_thinner = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40
materials_price = nylon_price*(quantily_of_nylon+2)\
    +paint_price*(quantily_of_paint*1.1)\
    +thinner_price*quantily_of_thinner\
    +bags_price
workers_payment = materials_price*0.3*hours
total_sum = materials_price + workers_payment
print(total_sum)
