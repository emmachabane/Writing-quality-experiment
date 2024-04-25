import csv
import pandas as pd


columns = ['Batch ID'] + [f'Task {i}' for i in range(1,11)]

with open('exp_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)


