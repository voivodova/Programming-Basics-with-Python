base_number = int(input())
sum_other_numbers = 0
while True:
    current_number = int(input())
    sum_other_numbers += current_number
    if sum_other_numbers >= base_number:
        print(sum_other_numbers)
        break