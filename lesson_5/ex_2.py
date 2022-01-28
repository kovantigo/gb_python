from itertools import islice

n = int(input())
odd_numb = (num for num in range(1, n + 1, 2))
print(*islice(odd_numb, n))
