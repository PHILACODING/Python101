
"""list_1 = [ 3, 5, 6, 78]
print(list_1)
list_sum = print(sum(list_1))
list_length = print(len(list_1))
list_average = (list_sum) / (list_length)
"""

list = [3,5,2,6, 4, 3,6,1,7]

sum = 0

for i in list:
    sum = sum + i

    sum += 1

    average = sum / len(list)

print(sum,average)



