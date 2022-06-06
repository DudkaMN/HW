with open('task_3.txt', 'r', encoding='utf-8') as task_3:
    n = 0
    mid = 0
    less_20 = []
    for s in task_3:
        n += 1
        mid += float(s.split(' ')[1])
        if float(s.split(' ')[1]) < 20000:
            less_20.append(s.split(' ')[0])
print(f'Менее 20 тысяч получают {less_20}. Средняя зарплата {round((mid / n), 2)}')
