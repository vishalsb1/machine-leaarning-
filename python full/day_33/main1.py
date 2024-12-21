import requests as rq


parameters={
    "lat":18.490573,
    "lng":433.930973,
    "formatted ":0,  # sets time to 12hour mode
}
rs=rq.get(url="https://api.sunrise-sunset.org/json",params=parameters)
rs.raise_for_status()
print(rs.json()["results"]["sunrise"])
print(rs.json()["results"]["sunset"]) 