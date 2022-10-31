import matplotlib.pyplot as plt
import numpy as np #pip install numpy
import sqlite3

conn = sqlite3.connect('weather/weather.db')
cursor = conn.cursor()
yb15 = cursor.execute("select * from yb15").fetchall()
print(yb15)

# #日期
labels = []
# #最低气温
men_means = []
# #最高气温
women_means = []
for item in yb15:
    labels.append(item[0])
    men_means.append(int(item[1]))
    women_means.append(int(item[2]))


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='min')
rects2 = ax.bar(x + width/2, women_means, width, label='max')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('℃')
ax.set_title('15days temprature of yubei')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=8)
ax.bar_label(rects2, padding=8)

fig.tight_layout()

plt.show()