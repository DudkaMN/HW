import json

with open('task_7.txt', 'r', encoding='utf-8') as firms:
    firms_lst = []
    profits = {}
    average_profit = {'average_profit': 0}
    pfs = 0
    n = 0
    for line in firms:
        pf = int(line.split(' ')[2]) - int(line.split(' ')[3])
        profits.update({line.split(' ')[0]: pf})
        if pf >= 0:
            pfs += pf
            n += 1
    firms_lst.append(profits)
    firms_lst.append({'average_profit': pfs / n})
with open('task_7.json', 'w', encoding='utf-8') as t_7_j:
    json.dump(firms_lst, t_7_j)
