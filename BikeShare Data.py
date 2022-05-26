from matplotlib import pyplot as plt
import pandas
import numpy as np

plt.style.use('seaborn')

month_list = ['February 2021', 'March 2021', 'April 2021',
              'June 2021', 'July 2021', 'August 2021',
              'September 2021', 'October 2021', 'November 2021',
              'December 2021', 'January 2022', 'February 2022']

x_values = []
for month in month_list:
    split = month.split()
    x_values.append(split[0] + '\n' + split[1])
y_values_annual = []
y_values_casual = []
x_axis = np.arange(len(x_values))

for month in month_list:
    filename = month + '.csv'
    print(filename)
    data = pandas.read_csv(filename, usecols=['Trip  Duration', 'User Type'])

    annual_members = data[data['User Type'] == "Annual Member"]
    casual_members = data[data['User Type'] == "Casual Member"]

    annual_list = annual_members['Trip  Duration'].tolist()
    casual_list = casual_members['Trip  Duration'].tolist()

    # y_values_annual.append((sum(annual_list)/60)/len(annual_list))
    # y_values_casual.append((sum(casual_list)/60)/len(casual_list))
    y_values_annual.append(len(annual_list))
    y_values_casual.append(len(casual_list))

# print(y_values_casual)
width = 0.3
plt.bar(x_axis - 0.15, y_values_annual, width=width, label='Annual Membership')
plt.bar(x_axis + 0.15, y_values_casual, width=width, label='Casual Membership')

plt.xticks(x_axis, x_values, fontsize=8)
# what does this do

plt.ylabel('Duration Biked in Hours')
plt.legend()
plt.title("Average Time Biked by Annual Members vs Casual Members")
plt.tight_layout()
plt.grid(False)
plt.show()
