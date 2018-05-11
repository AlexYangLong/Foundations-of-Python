import math

num = int(input())

nums = input()
num_list = nums.split(' ')
sum = 0
for i in num_list:
    sum += int(i)
avg = sum / num

sum = 0
for i in num_list:
    sum += (int(i) - avg) ** 2

print('%.5f' % math.sqrt(sum/num))