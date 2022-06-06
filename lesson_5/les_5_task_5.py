with open('task_5.txt', 'w') as numbers:
    numbers.write('2 34 6 5 8')
with open('task_5.txt', 'r') as numbers:
    sum = 0
    for n in numbers.read().split(' '):
        sum += int(n)
    print(sum)
