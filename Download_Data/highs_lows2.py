#/python3

#/python3

#/python3

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    # print(header_row)
    # print(dates)

    # 获取每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # highs = []
    # for row in reader:
    #     high = int(row[1])
    #     highs.append(high)

    # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



