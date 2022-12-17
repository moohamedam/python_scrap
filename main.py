from bs4 import BeautifulSoup as S
import requests
c =input(" enter your country :")
url = f"https://www.google.com/search?q=meteo+{c}&oq=meteo+a&aqs=chrome.2.69i57j0i512l9.18855j0j15&sourceid=chrome&ie=UTF-8"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
r =requests.get(url,headers=headers)
soup =S (r.content,"html.parser")
print(f"meteo now in  {c}")
country_name =soup.find(id="wob_dts")
print(country_name.string, soup.find(id="wob_tm" ).string +"c")
print("Precipitation :",soup.find(id="wob_pp").string)
print("Humidity:",soup.find(id="wob_hm").string)
print("wind :",soup.find(id="wob_ws" ).string)


