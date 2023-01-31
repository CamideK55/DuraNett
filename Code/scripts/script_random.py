# voorbeeld:
import subprocess
import time
import csv
import os.path

start = time.time()
n_runs = 0

# print(os.path.abspath("../SmartGrid.py"))
# DuraNett/code/SmartGrid.py

# runnen script voor 10 min
while time.time() - start < 60:
    print(f"run: {n_runs}")
    f = open("Data/results/results_random.csv", "a", newline='')
    subprocess.call(["timeout", "60", "python3", "../SmartGrid.py", "1", "-r"], stdout=f)
    # subprocess.check_output(["timeout", "60", "python3", "../SmartGrid.py", "1", "-r"])
    n_runs += 1
    # decode()



# # saving the data output
# # inspired by: https://www.pythontutorial.net/python-basics/python-write-csv-file/
# header = ["district", "iteration", "score" ]
# data = []
# with open("Data/results/results_random.csv", "a", newline='') as results_random:
#     writer = csv.writer(results_random)
#     writer.writerow(header)
#     writer.writerows(data)
