arr = [1, 2, 2, 1, 3]
Hash_table = dict()
for i in arr:
    if i not in Hash_table.keys():
        Hash_table[i] = 1
    else:
        Hash_table[i] += 1
list1 = [value for value in Hash_table.values()]
for j in range(0, len(list1)):
    for n in range(j+1, len(list1)):
        if list1[j] == list1[n]:
            print('Flase')
print('OK')