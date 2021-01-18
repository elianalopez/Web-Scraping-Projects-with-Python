import pandas as pd
import requests
from bs4 import BeautifulSoup

#This is the website to the Boston 7 day forecast from weather.gov
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.35866000000004&lon=-71.05673999999993#.YAXqz-hKjb0")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

#print(week)

items = (week.find_all(class_ = "tombstone-container"))
#print(items[0])

#print(items[0].find(class_ = "period-name").get_text())
#print(items[0].find(class_ = "short-desc").get_text())
#print(items[0].find(class_ = "temp").get_text())

period_names = [item.find(class_ = "period-name").get_text() for item in items]
short_descs = [item.find(class_ = "short-desc").get_text() for item in items]
temps = [item.find(class_ = "temp").get_text() for item in items]


#print(period_names)
#print(short_descs)
#print(temps)

weather = pd.DataFrame(
    {'period': period_names,
    'short descriptions': short_descs,
    'temperature': temps,
    })

print(weather)

weather.to_csv('weather.csv')
