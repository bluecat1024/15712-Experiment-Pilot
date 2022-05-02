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
    "type1_small.txt",
    "type2_small.txt",
    "type3_small.txt",
    "type4_small.txt"
]

for i in range(3):
    file = open(file_path[i], "w")
    start = 1
    end = 25
    point = 1
    cur = 1
    for j in range(1, 21):
        file.write(queries[i].format(j))

    for j in range(1, 21):
        if i == 0 or i == 2:
            file.write(execute[i].format(j, start, end))
        else:
            file.write(execute[i].format(j, point))
        point = point + 1
        point %= 50
        start += 1
        start %= 50
        end += 1
        end %= 50

    start = 1
    end = 25
    point = 1

    file.write("prewarm:\n")

    for j in range(1, 6001):
        if start > end:
            temp = start
            start = end
            end = temp
            
        if i == 0 or i == 2:
            file.write(execute[i].format(cur, start, end))
        else:
            file.write(execute[i].format(cur, point))
        if j == 100 or j == 2100 or j == 4100:
            file.write("create index haha on t1(id);\n")
        elif j == 1900 or j == 3900 or j == 5900:
            file.write("drop index haha;\n")
        
        cur = (cur) % 20 + 1
        point = point + 1
        point %= 50
        start += 1
        start %= 50
        end += 1
        end %= 50

file = open(file_path[3], "w")
for i in range(1, 8):
    file.write(queries[0].format(i))
for i in range(1, 8):
    file.write(queries[1].format(i))
for i in range(1, 8):
    file.write(queries[2].format(i))

start = 1
end = 25
point = 1
for i in range(20):
    if i % 3 == 0:
        file.write(execute[0].format(i // 3 + 1, start, end))
    elif i % 3 == 1:
        file.write(execute[1].format(i // 3 + 1, point))
    else:
        file.write(execute[2].format(i // 3 + 1, start, end))

    point = point + 1
    point %= 50
    start += 1
    start %= 50
    end += 1
    end %= 50


start = 1
end = 25
point = 1
cur = 1
file.write("prewarm:\n")
for i in range(1, 6001):
    if start > end:
        temp = start
        start = end
        end = temp
    if i % 3 == 0:
        file.write(execute[0].format(cur, start, end))
    elif i % 3 == 1:
        file.write(execute[1].format(cur, point))
    else:
        file.write(execute[2].format(cur, start, end))
    if i == 100 or i == 2100 or i == 4100:
        file.write("create index haha on t1(id);\n")
    elif i == 1900 or i == 3900 or i == 5900:
            file.write("drop index haha;\n")
    cur = (cur) % 7 + 1
    point = point + 1
    point %= 50
    start += 1
    start %= 50
    end += 1
    end %= 50