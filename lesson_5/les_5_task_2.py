with open("task_2.txt", "r", encoding="utf-8") as task_2:
    n = 0
    for s in task_2:
        n += 1
        print(f'в {n} строке {len(s.split(" "))} слов')
    print(f'всего {n} строк')
