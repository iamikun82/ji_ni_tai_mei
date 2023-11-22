arr = [1, 2, 2, 1, 1, 3]
Hash_table = dict()
for i in arr:
    if i not in Hash_table.keys():
        Hash_table[i] = 1
    else:
        Hash_table[i] += 1
print(Hash_table)