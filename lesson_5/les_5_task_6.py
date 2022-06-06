with open('task_6.txt', 'r', encoding='utf-8') as sd:
    rep_card = {}
    for line in sd:
        i = 0
        a = ''
        sm = 0
        while i < len(line):
            if '0' <= line[i] <= '9':
                a += line[i]
                i += 1
            elif a != '':
                sm += int(a)
                a = ''
            else:
                i += 1
        if a != '':
            sm += int(a)
        r_c = {line.split(':')[0]: sm}
        rep_card.update(r_c)
print(rep_card)
