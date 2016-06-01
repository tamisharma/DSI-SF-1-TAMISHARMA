---
title: API Lab
type: lab 3.2
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) API Lab
Week 8 | 3.2

## Introduction

> Note: This will be a very open ended lab, since everyone may end up using different geographies and starting seed geographies. We've tested this out on several locales around me and it works, for most, but if you don't have a good starting seed location, the procedure may not propogate well.

Today's lab is going to get your hands dirty with respect to the Foursquare API. We're also going to build a simple crawling method that will go through the JSON hierarchy, extract the data we want, and deposit them into a Pandas DataFrame so we can do simple analysis.


## Exercise

Today's lab will start by having you access the foursquare API via Python.

 - You will have to traverse real foursquare data
 - Understand where the data is located in the JSON structure, and how to get at it
 - How to iteratively build your Pandas data frame from the JSON data for further analysis

```python
import foursquare
import json
import pandas as pd
import unicodedata


#ACCESS_TOKEN = ""
#client = foursquare.Foursquare(access_token=ACCESS_TOKEN)

CLIENT_ID = 'YOUR CODE HERE'
CLIENT_SECRET = 'YOUR CODE HERE'
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
```


#### Requirements

- Understand how to traverse JSON data
- Understand how to utilize dictionaries data types, array types, and other useful Python containers
- Novice facility with foursquare APIs via reading the Foursquare API docs


#### Starter code

Please utilize the starter code found in the directory to start the students on today's activities
[starter code](./code/w8-3.2-starter.ipynb).

> [Solution Code](./code/w8-3.2-solutions.ipynb)

#### Deliverable

Submit a
 notebook with the code written to complete the exercises!

#### Additional Resources

For those of you who want to read further:

- [Foursquare Developer Notes](https://developer.foursquare.com/)
