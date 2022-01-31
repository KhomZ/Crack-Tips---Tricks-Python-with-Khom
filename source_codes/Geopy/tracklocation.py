# @KhomZ
# geocoder

import geocoder

g = geocoder.ip("me")
# g = geocoder.ip("192.168.1.78")


print("Your Latitude and Longitude is :", g.latlng)



'''
Output:
Your Latitude and Longitude is : [---, ---]

Your Latitude and Longitude is : []
'''