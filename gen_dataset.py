import random

file = open("data.csv", "w")
file.write("key,val\n")
for i in range(10000):
    key = random.randint(1, 7000)
    value = random.randint(1, 100)
    file.write(str(key) + "," + str(value)+"\n")

file.close()