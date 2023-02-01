
import subprocess
import time
import csv


start = time.time()
n_runs = 0

# inspired by: https://www.pythontutorial.net/python-basics/python-write-csv-file/
#              https://stackoverflow.com/questions/53842716/python-subprocess-output-format
#              https://www.tutorialspoint.com/python/string_decode.htm

header = ["district" , "states" , "score"]
f = open("../../Data/results/results_random.csv", "a")
writer = csv.writer(f)
writer.writerow(header)

# runnen script voor 10 min
while time.time() - start < 600:
    print(f"run: {n_runs}")
    data = subprocess.check_output(["timeout", "60", "python3", "../SmartGrid.py", "1", "-r"])
    data = data.decode('utf-8')
    data = data.strip("\n")
    data = data.split(", ")
    writer.writerow(data)
    n_runs += 1
f.close()
