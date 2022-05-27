my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# решение через count:
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# решение через словарь:
new_dict = {}
res_dict = {}
for _ in my_list:
    new_dict.update({_: 0})
for _ in my_list:
    new_dict.update({_: new_dict.get(_) + 1})
for key in new_dict:
    if new_dict.get(key) == 1:
        res_dict.update({key: key})
print(res_dict.keys())