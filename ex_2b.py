cube_numbers = []
for number in range(1,1001,2):
    cube_numbers.append(number ** 3)

sum_numbers = 0
for index in range(len(cube_numbers)):
    sum_digits = 0
    curr_number = cube_numbers[index] + 17
    while curr_number > 0:
        sum_digits += curr_number % 10
        curr_number //= 10
    if sum_digits % 7 == 0:
        sum_numbers += (cube_numbers[index] + 17)
print(sum_numbers)
