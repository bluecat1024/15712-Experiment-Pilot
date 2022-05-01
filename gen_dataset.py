import random

file = open("data.csv", "w")
file.write("key,val\n")
for i in range(1000000):
    key = random.randint(1, 300000)
    value = random.randint(1, 30000)
    file.write(str(key) + "," + str(value)+"\n")

file.close()