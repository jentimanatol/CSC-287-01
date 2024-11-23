from pathlib import Path
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)
print(header_row)


# Reading a CSV File - Printing Headers and Positions
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Fun with DateTime
from datetime import datetime
first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
print(first_date)



# Collecting the High Temperatures (TMAX)
highs, dates = [],[]
for row in reader:
    high = int(row[4])
    highs.append(high)
    

    date = int(row[3])
    dates.append(dates)


print(highs)


plt.plot(highs,dates )
plt.ylabel('High Temperatures (TMAX)','dates')
plt.show()

