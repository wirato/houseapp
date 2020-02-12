with open('houseapp\\fixtures\\Housedata.yaml', 'w', encoding='utf-8') as of:
    with open('DataSet.csv', 'r', encoding='utf-8') as rf:
        for line in rf.readlines()[1:]:
            a = line.strip().split(',')
            of.writelines(f'- model: houseapp.Housedata\n')
            of.writelines(f'  pk: {a[0]}\n')
            of.writelines(f'  fields:\n')
            of.writelines(f'    X1: {a[1]}\n')
            of.writelines(f'    X2: {a[2]}\n')
            of.writelines(f'    X3: {a[3]}\n')
            of.writelines(f'    X4: {a[4]}\n')
            of.writelines(f'    X5: {a[5]}\n')
            of.writelines(f'    X6: {a[6]}\n')

with open('houseapp\\fixtures\\Price_of_unit_area.yaml', 'w', encoding='utf-8') as of:
    with open('DataSet.csv', 'r', encoding='utf-8') as rf:
        for line in rf.readlines()[1:]:
            a = line.strip().split(',')
            of.writelines(f'- model: houseapp.Price_of_unit_area\n')
            of.writelines(f'  pk: {a[0]}\n')
            of.writelines(f'  fields:\n')
            of.writelines(f'    Y: {a[7]}\n')
