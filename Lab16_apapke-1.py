"""
lab 16
Ari Papke
reading data
05/14/26
"""

from pathlib import Path
import matplotlib.pyplot as plt
import csv
import datetime

try:
    path = Path('/home/mya_applesauce/Documents/lab16/OHUR.csv')
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)
    
    dates = []
    rates = []

    for row in reader:
        rate = float(row[1])
        rates.append(rate)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(rates, color='red')

    plt.show()
except Exception as err:
    print("didn't work :[")