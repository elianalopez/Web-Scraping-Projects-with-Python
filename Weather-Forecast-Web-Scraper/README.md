# Weather Forecast Web Scrapper
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

<p align="center"><img src="https://github.com/elianalopez/Web-Scraping-Projects-with-Python/blob/main/Weather-Forecast-Web-Scraper/Images/Forecast.PNG" width="100%" height="100%"></p>

<p align="center"><img src="https://github.com/elianalopez/Web-Scraping-Projects-with-Python/blob/main/Weather-Forecast-Web-Scraper/Images/Terminal.PNG" width="100%" height="100%"></p>
