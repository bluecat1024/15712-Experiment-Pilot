import random

file = open("data.csv", "w")
file.write("key,val\n")
for i in range(100):
    key = random.randint(1, 50)
    value = random.randint(1, 50)
    file.write(str(key) + "," + str(value)+"\n")

file.close()