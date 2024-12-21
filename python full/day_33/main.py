import requests

# output=requests.get(url="http://api.open-notify.org/iss-now.json")

# # print(output.json())
# lati=output.json()["iss_position"]["latitude"]
# longi=output.json()["iss_position"]["longitude"]

# iss_loc=(lati,longi)

# print(iss_loc)
output=requests.get(url="https://api.kanye.rest")
print(output.json()['quote'])