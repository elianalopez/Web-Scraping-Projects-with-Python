# Weather Forecast Web Scraper
<p align = "center"> A simple example of web scrapping in Python by utilizing Beautiful Soup </p>
<p align = "center"> All the data that was web scrapped came from Boston's 7 day weather forcast from weather.gov </p>

## Tools Utilized

* VSCode
* Python 3.8.5

### Python Libraries

* Beautiful Soup 4
* Pandas
* Requests

### Website Utilized

* Boston's 7 day forecast from <a href = "https://forecast.weather.gov/MapClick.php?lat=42.35866000000004&lon=-71.05673999999993#.YAX5A-hKjb0"> weather.gov</a>


## Installation 

```
pip install beautifulsoup4
```

```
pip install requests
```

```
pip install pandas
```

## The Code 

To select the website that you want to web scrape you utilize Requests Library from Python

```python
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.35866000000004&lon=-71.05673999999993#.YAXqz-hKjb0")
```


Utilizing Beautiful Soup to parse the contents of the website's HTML code
```python
soup = BeautifulSoup(page.content, 'html.parser')
```

Within the HTML code the contents of 7 day forcast is within the *seven-day-forecast-body*, so we then utilized Beautiful Soup to only show us the content within the *seven-day-forecast-body*.

```python
week = soup.find(id="seven-day-forecast-body")
```

Within the body, important information regarding the weather forecast such as the weather condition, day of week, and temperature, has been listed and contained in the *tombstone-container*.

```python
items = (week.find_all(class_ = "tombstone-container"))
```

From then we can parse out certain information, down below we parse out the time of day, weather description, and temperature:

```python
period_names = [item.find(class_ = "period-name").get_text() for item in items]
short_descs = [item.find(class_ = "short-desc").get_text() for item in items]
temps = [item.find(class_ = "temp").get_text() for item in items]
```

Utilizing the Pandas Library we can organize the information above into a table utilizing the code below as well as convert the following table into a CSV file.

```python
weather = pd.DataFrame(
    {'period': period_names,
    'short descriptions': short_descs,
    'temperature': temps,
    })
    
print(weather)

weather.to_csv('weather.csv')

```

### The Forecast

<p align="center"><img src="https://github.com/elianalopez/Web-Scraping-Projects-with-Python/blob/main/Weather-Forecast-Web-Scraper/Images/Forecast.PNG" width="100%" height="100%"></p>

### The Data

This is the image of the data after it was parsed from the website. 

With the use of the **Panadas** library I was able to organize the data into a table.


<p align="center"><img src="https://github.com/elianalopez/Web-Scraping-Projects-with-Python/blob/main/Weather-Forecast-Web-Scraper/Images/Terminal.PNG"></p>
