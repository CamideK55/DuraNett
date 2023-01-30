# voorbeeld:
import subprocess
import time
import csv

start = time.time()
n_runs = 0



# runnen script voor 10 min
while time.time() - start < 600:
    print(f"run: {n_runs}")
    subprocess.call(["timeout", "60", "python3", "1", "random.py"])
    n_runs += 1

# saving the data output
# inspired by: https://www.pythontutorial.net/python-basics/python-write-csv-file/
header = ["district", "iteration", "score" ]
data = []
with open("Data/results/results_random.csv", "a", newline='') as results_random:
    writer = csv.writer(results_random)
    writer.writerow(header)
    writer.writerows(data)
