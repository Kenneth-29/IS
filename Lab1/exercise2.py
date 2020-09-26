x = int(input('How many numbers are you averaging?: '))
total_sum = 0
for n in range(x):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum / x
print('Average of the', x, ' numbers provided is :', avg)