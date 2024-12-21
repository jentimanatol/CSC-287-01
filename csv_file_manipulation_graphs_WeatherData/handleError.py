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

# Collecting the high and low temperatures (TMAX and TMIN) and dates
highs, lows, dates = [], [], []
for row in reader:
    try:
        high = int(row[4])
        low = int(row[5])
        date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {row[2]}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

print(highs)
print(lows)
print(dates)

# Plotting the data
plt.style.use('seaborn-v0_8')
plt.plot(dates, highs, label='Highs', color='red')
plt.plot(dates, lows, label='Lows', color='blue')
plt.fill_between(dates, highs, lows, facecolor='lightgray', alpha=0.5)
plt.ylabel('Temperature (°F)')
plt.xlabel('Dates')
plt.title('High and Low Temperatures in Sitka, July 2021')
plt.xticks(rotation=45)
plt.legend()
plt.show()


#Done good handle errors.