import time

from geopy.exc import GeocoderTimedOut
from matplotlib import pyplot as plt
import pandas
import numpy as np
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='...')

plt.style.use('seaborn')

data = pandas.read_csv('Meteorite_Landings.csv')
print(data)
geodata = data[data['GeoLocation'] != '(0.0, 0.0)']
coordinate_list = geodata['GeoLocation'].tolist()

remove_list = []
# print(coordinate_list)

for i in range(len(coordinate_list)):
    if not isinstance(coordinate_list[i], str):
        remove_list.append(i)

remove_list.reverse()
for i in remove_list:
    coordinate_list.pop(i)

# print(coordinate_list)
meteorites = []


def get_indian_meteorites(coordinate: str, lst: list):
    coordinate_entry = coordinate.strip('()')
    try:
        location = geolocator.reverse(coordinate_entry)
        country = (location.raw['address']['country'])
        meteorites.append(country)
        # time.sleep(1)
        print('done')
    except GeocoderTimedOut:
        time.sleep(1)
        return get_indian_meteorites(coordinate, lst)
    except:
        pass


for i in coordinate_list:
    get_indian_meteorites(i, meteorites)
print(meteorites)

with open('new2.txt', 'w') as f:
    f.write(str(meteorites))

# width = 0.3
# plt.bar(x_axis - 0.15, y_values_annual, width=width, label='Annual Membership')
# plt.bar(x_axis + 0.15, y_values_casual, width=width, label='Casual Membership')
#
# plt.xticks(x_axis, x_values, fontsize=8)
# # what does this do
#
# plt.ylabel('Duration Biked in Hours')
# plt.legend()
# plt.title("Average Time Biked by Annual Members vs Casual Members")
# plt.tight_layout()
# plt.grid(False)
# plt.show()
