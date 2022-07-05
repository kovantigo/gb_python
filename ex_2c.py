sum_numbers = 0
for number in range(1,1001,2):
    sum_digits = 0
    curr_number = number ** 3 + 17
    curr_number_sp = curr_number
    while curr_number_sp > 0:
        sum_digits += curr_number_sp % 10
        curr_number_sp //= 10
    if sum_digits % 7 == 0:
        sum_numbers += curr_number
print(sum_numbers)
