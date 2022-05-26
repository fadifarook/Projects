import time

from matplotlib import pyplot as plt
import pandas
import geopandas
#import geoplot
import seaborn as sns
import math

plt.style.use('seaborn')

data = pandas.read_csv('Meteorite_Landings.csv')
# print(data)


# code for counting the number of valid and relict meteorites
'''
nametype_data = data[['nametype']] == 'Valid'

count_valid = int(nametype_data.sum())
count_relict = len(nametype_data) - count_valid

print(count_valid, count_relict)

width = 0.2
x = ['Valid Meteorites', 'Relict Meteorites']
y = [count_valid, count_relict]
bars = plt.bar(x, y, width=width)

for bar in bars:
    y_val = bar.get_height()
    plt.text(bar.get_x() + 0.075, y_val, y_val)


plt.ylabel('Number of Meteorites')
plt.legend()
plt.title("Number of Valid and Relict Meteorites")

'''

# code for number of meteorites found per year

'''
year_data = data['year']
# print(year_data)

year_list = data['year'].tolist()
remove_list_year = []
for i in range(len(year_list)):
    if math.isnan(year_list[i]):
        remove_list_year.append(i)
    else:
        year_list[i] = float(year_list[i])

remove_list_year.reverse()
for i in remove_list_year:
    year_list.pop(i)
year_list = [int(x) for x in year_list]
# print(year_list)

year_dict = {}
for item in year_list:
    if item < 1950 or item > 2020:
        continue
    if item not in year_dict:
        year_dict[item] = year_list.count(item)

print(year_dict)


# year_list = [int(x) for x in year_list]

#print(year_list)

x_year, y_year = zip(*year_dict.items())
plt.bar(x_year, y_year)
plt.xlabel("Year")
plt.ylabel("Number of Meteorites Found")
plt.title("Number of Meteorites Found By Year (1950 to 2020)")

plt.tight_layout()
plt.grid(False)
plt.show()
'''


# code to find the number of fallen and found meteorites

'''
fall_data = data[['fall']] == 'Fell'

count_fall = int(fall_data.sum())
count_found = len(fall_data) - count_fall

print(count_fall, count_found)

width = 0.2
x = ['Fall Meteorites', 'Found Meteorites']
y = [count_fall, count_found]
bars = plt.bar(x, y, width=width)

for bar in bars:
    y_val = bar.get_height()
    plt.text(bar.get_x() + 0.07, y_val, y_val)


plt.ylabel('Number of Meteorites')
plt.legend()
plt.title("Number of Fallen and Found Meteorites")

plt.show()

'''


# code to plot mass as a histogram

'''
mass_data = data['mass (g)']
#print(mass_data)

mass_list = mass_data.tolist()
#print(mass_list)
mass_renewed = []

for mass in mass_list:
    if mass <= 1000:
        mass_renewed.append(mass)

sns.kdeplot(mass_renewed, shade=True, color='darkblue')

plt.ylabel('Density of Meteorites')
plt.xlabel('Mass (g)')
plt.title('Density of meteorites found under 1kg')
plt.show()


greatest_mass = data[data['mass (g)'] > 10000000]  # greater than 10,000 kg
print(greatest_mass[['name', 'recclass', 'mass (g)', 'year']])

'''


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()
