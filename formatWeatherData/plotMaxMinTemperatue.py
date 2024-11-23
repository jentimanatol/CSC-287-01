from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Read the CSV file
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)
print(header_row)

# Print headers and positions
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Collecting the high temperatures (TMAX) and dates
highs, lows , dates = [], [], []
for row in reader:
    high = int(row[4])
    highs.append(high)
    

    low= int(row[5])
    lows.append(low)


    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)

print(highs)
print(lows)
print(dates)


# Plotting the data
plt.style.use('seaborn-v0_8')
plt.plot(dates, highs)
plt.ylabel('Temperatures')
plt.xlabel('Dates')
plt.title('High Temperatures in Sitka, July 2021')
plt.xticks(rotation=45)
plt.show()
