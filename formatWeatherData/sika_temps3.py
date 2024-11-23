from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Read the CSV file
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)
print(header_row)


# Print headers and positions
for index, column_header in enumerate(header_row):
    print(index, column_header)




# Collecting the high temperatures (TMAX) and dates
highs, dates = [], []
for row in reader:
    high = int(row[4])
    highs.append(high)
    
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)

print(highs)
plt.style.use('seaborn-v0_8')

# Plotting the data
plt.plot(dates, highs)
plt.ylabel('High Temperatures (TMAX)')
plt.xlabel('Dates')
plt.title('High Temperatures in Sitka, July 2021')
plt.show()
