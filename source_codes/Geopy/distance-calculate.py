# @author: KhomZ
from turtle import distance
from geopy.distance import geodesic

# loading the latitude and longitude from two places
first_place = (52.2296756, 21.0122287)
second_place = (52.406374, 16.9251681)


# print distance in km
# distance = (geodesic(first_place, second_place).km)
distance = int(geodesic(first_place, second_place).km)
print(distance,"kilometer")



'''
output:
279.35290160430094 kilometer

output:
279 kilometer
integer

'''

