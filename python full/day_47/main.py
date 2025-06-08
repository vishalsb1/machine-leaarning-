# import requests 
# from bs4 import BeautifulSoup
# import lxml

# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
#     "Accept-Language":"en-US,en;q=0.9"
# }
# data_html=requests.get(url="https://www.amazon.com/dp/B08628GW1P/ref=sbl_dpx_kitchen-electric-cookware_B08YFH1NLG_0?keywords=Duo+Evo+Plus+10-in-1+Pressure+Cooker%2C+Rice+Cooker%2C+Slow+Cooker%2C+Yogurt+Maker%2C+Sous+Vide%2C+Saut%C3%A9%2C+Food+Warmer%2C+Bake%2C+Stock+Pot%2C+Steamer%2C+Cookware+Grade+Stainless+Steel+Inner+Pot%2C+6+Quart&th=1",headers=headers)

# soup_html=BeautifulSoup(data_html.text,'lxml')
# price=soup_html.find(class_='a-offscreen')
# print(price)

# import smtplib

# title = soup.find(id="productTitle").get_text().strip()
# print(title)

# BUY_PRICE = 200

# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"

#     with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
#         connection.starttls()
#         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
#         connection.sendmail(
#             from_addr=YOUR_EMAIL,
#             to_addrs=YOUR_EMAIL,
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
#         )

# didint work