# Sum of squares less than n, list of squares under n
# Can be easily adapted for other exponents

summed = 0
n = 10
sumlist = []
for i in range(2, n):
    if i ** 2 < n:
        summed += i
    if i ** 2 < n:
        sumlist.append(i)
print(summed)
print(sumlist)
