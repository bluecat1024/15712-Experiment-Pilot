import sys

file_path = sys.argv[1]
finish_count=[[], [], []]
start_time = None
exec_time = 0
replan_time = 0
overhead_time = 0

output_file = file_path.split(".")[0] + "_processed.txt" 

with open(file_path, "r") as file:
    for line in file:
        if len(line) == 0 or line[0] != 't':
            continue
        segments = line.split(":")
        if start_time == None:
            start_time = int(segments[-1])
        
        if segments[1] == "Execution":
            finish_count[0].append(str(int(segments[-1]) - start_time + int(segments[-2])))
            if len(finish_count[1]) == 0:
                finish_count[1].append("1")
            else:
                finish_count[1].append(str(int(finish_count[1][-1]) + 1))
            finish_count[2].append(segments[-2])
            exec_time += int(segments[-2])
        elif segments[1] == "Build":
            replan_time += int(segments[-2])
        else:
            overhead_time += int(segments[-2])


with open(output_file, "w") as file:
    x = ",".join(finish_count[0])
    y = ",".join(finish_count[1])
    z = ",".join(finish_count[2])
    file.write(x)
    file.write("\n")
    file.write(y)
    file.write("\n")
    file.write(z)
    file.write("\n")
    file.write(str(exec_time))
    file.write("\n")
    file.write(str(replan_time))
    file.write("\n")
    file.write(str(overhead_time))
