queries = [
    "prepare type_1_{} (int, int) as select id, value from t1 where id > $1 and id < $2;\n",
    "prepare type_2_{} (int) as select id, value from t1 where id = $1;\n",
    "prepare type_3_{} (int, int) as select id, value from t1 where id > $1 and id < $2 order by id desc;\n"
]

execute = [
    "execute type_1_{} ({}, {});\n",
    "execute type_2_{} ({});\n",
    "execute type_3_{} ({}, {});\n"
]

file_path = [
    "type1.txt",
    "type2.txt",
    "type3.txt",
    "type4.txt"
]

for i in range(3):
    file = open(file_path[i], "w")
    start = 1
    end = 50
    point = 1
    cur = 1
    for j in range(1, 601):
        file.write(queries[i].format(j))

    for j in range(1, 6001):
        if i == 0 or i == 2:
            file.write(execute[i].format(cur, start, end))
        else:
            file.write(execute[i].format(cur, point))
        if j == 600 or j == 2400 or j == 4200:
            file.write("create index haha on t1(id);\n")
        elif j == 1800 or j == 3600 or j == 5400:
            file.write("drop index haha;\n")
        
        cur = (cur) % 600 + 1
        point = point + 49
        start += 49
        end += 49

file = open(file_path[3], "w")
for i in range(1, 201):
    file.write(queries[0].format(i))
for i in range(1, 201):
    file.write(queries[1].format(i))
for i in range(1, 201):
    file.write(queries[2].format(i))

start = 1
end = 50
point = 1
cur = 1
for i in range(1, 6001):
    if i % 3 == 0:
        file.write(execute[0].format(cur, start, end))
    elif i % 3 == 1:
        file.write(execute[1].format(cur, point))
    else:
        file.write(execute[2].format(cur, start, end))
    if i == 600 or i == 2400 or i == 4200:
        file.write("create index haha on t1(id);\n")
    elif i == 1800 or i == 3600 or i == 5400:
            file.write("drop index haha;\n")
    cur = (cur) % 200 + 1
    point = point + 49
    start += 49
    end += 49