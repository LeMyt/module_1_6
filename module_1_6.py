my_dict = {'Антон': 2001, 'Борис': 2002, 'Галина': 2003}
print(my_dict)
print(my_dict['Борис'])
print(my_dict.get('Семен'))
my_dict['Олег'] = 2005
my_dict['Илья'] = 2006
print(my_dict.pop('Олег'))
print(my_dict)
print()
my_set = {'Аист', 'Барабан', 1, 2, 1, 'Барабан', 3.14}
print(my_set)
my_set.add((9, 8, 7))
my_set.add((7, 8, 9))
my_set.discard((9,8,7))
print(my_set)
