with open("first_file.txt", "w") as first_f:
    n = 1
    while True:
        s = input(f'введите {n} строку: ')
        if len(s) > 0:
            first_f.write(s + '\n')
            n += 1
        else:
            break
