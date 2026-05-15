"""
lab 16
Ari Papke
reading data
05/14/26
"""

from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

try:
    path = Path('/home/mya_applesauce/Documents/lab16/OHUR.csv')
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)
    
    dates = []
    rates = []

    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        rate = float(row[1])
        dates.append(date)
        rates.append(rate)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, rates, color='red')

    ax.set_title("Ohio Unemployment (by Month): 1976 - 2022", fontsize=25)
    ax.set_xlabel("Date", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Unemployment Rate", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.savefig("ohio_unemployment.png")
except Exception as err:
    print("didn't work :[\nproblem is this: ", err)