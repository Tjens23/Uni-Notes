---
creation date: 2024-11-09 16:15
modification date: Saturday 9th November 2024 16:15:16
tags:
  - Assignments
year: 2024
semester: 3
links: "[[OD Lecture 3]]"
---

---
# [[OD Lecture 3 Assignments]]


## Task 1


## Task 2


## Task 3

```python
from flask import Flask, request

  

app = Flask(__name__)

  

@app.route('/')

def index():

    return "Hello, World!"

  

@app.route('/welcome')

def welcome():
    return "Welcome to this excellent page"

  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```



## Task 4


```python
from flask import Flask, request

  

app = Flask(__name__)

  

@app.route('/')

def index():

    return "Hello, World!"

  

@app.route('/welcome/<name>')

def welcome(name):

    return f"Welcome to this excellent page, {name}!"

  

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
```

```dockerfile
FROM python:latest

WORKDIR /app

COPY . /app/

RUN pip install flask

EXPOSE 5000

CMD ["python", "Main.py"]
```


```
docker buildx build -t tjens23/odl3l4 -f Dockerfile .
```

```
docker run -d -p 7000:5000 tjens23/odl3l4
```


## Task 5

```
curl https://api.zippopotam.us/DK/5000 | jq
```



## Task 6

```sh
curl "https://api.open-meteo.com/v1/forecast?timezone=auto&daily=temperature_2m_max,temperature_2m_min&latitude=55.4038&longitude=10.4024" | jq
```


## Task 7

```python
from flask import Flask
import requests 
app = Flask(__name__)

@app.route('/weather/<postcode>')

def weather(postcode):

    postcode_url = f"https://api.dataforsyningen.dk/postnumre/{postcode}"

    location_response = requests.get(postcode_url)

    if location_response.status_code != 200:

        return f"Error: Could not find postcode {postcode}", 404

    location_data = location_response.json()

    city = location_data['navn']

    lat = location_data['visueltcenter'][1]  # Note: API returns [lon, lat]

    lon = location_data['visueltcenter'][0]

  

    weather_url = f"https://api.open-meteo.com/v1/forecast?timezone=auto&daily=temperature_2m_max,temperature_2m_min&latitude={lat}&longitude={lon}"

    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:

        return "Error: Could not fetch weather data", 404

    weather_data = weather_response.json()

    temp_min = weather_data['daily']['temperature_2m_min'][1]  # Tomorrow's temperature

    temp_max = weather_data['daily']['temperature_2m_max'][1]  # Tomorrow's temperature

  

    return f"The temperature in {city} will be between {temp_min} and {temp_max} tomorrow"
```
