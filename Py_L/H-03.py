def sum_cal(*nums):
    result = 0
    for n in nums:
        result += n
    print(result)


a = range(1, 101)
sum_cal(*a)
