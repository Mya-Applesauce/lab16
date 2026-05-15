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

    ax.set_title("Ohio Unemployment (by Month): 1976 - 2022", fontsize=25)
    ax.set_xlabel("Date", fontsize=16)
    ax.set_ylabel("Unemployment Rate", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()
except Exception as err:
    print("didn't work :[")