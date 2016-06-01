---
title: API Review with Foursquare API
type:  lesson
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  API Review with Foursquare API
Week 8 | 3.1


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

- Describe HTTPS and define an API
- Introduce the Foursquare API
- Discuss Foursquare API Functions
- Receive and iterate through data from the Foursquare API
- Describe how JSON stores data

### STUDENT PRE-WORK
*Before this lesson, students will need to be able to:*

- Review API environment and access
- Use python data structures
- Simple Exploratory Data Analysis

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| Timing | Type | Topic |
| --- | --- | --- |
| 5 min | [Opening](#opening) | A Brief Review of APIs |
| 10 min | [Introduction](#introduction) | Introduction to the Foursquare API and Python |
| 15 min | [Demo](#demo) | Looking through datatypes in Foursquare |
| 25 min | [Guided Practice](#Guided)  | Summarizing Foursquare data in Python |
| 25 min | [Independent Practice](#Indy) | Data Analysis with Foursquare API |
| 5 min |  [Conclusion](#conclusion)| Concluding Remarks |

---


#### Opening (5 min):
<a name = "opening"></a>
## (Re)Introducing APIs with Foursquare in mind

As a review, an API call is just making HTTP requests to a server and sending/receiving structured data from that endpoint. We are still communicating with URLs, however instead of receiving markup, like we do with HTML pages, we receive data. If that data is structured as JSON, we can easily start reacting and communicating with it thanks to the provided JSON methods.


#### APIs: A Quick Review (10 min):

<a name = "introduction"></a>

**Quick Check:** How do clients relate to servers?

Because our pages will be fully or partially rendered on the client side after we receive this data, there are a few best scenarios we need to take into account:

  - Certain APIs require authentication, and we need to provide an API key either as a request parameter, in the header, or in the body of the call.
  - When we make an API call after a user action, we need to give the user feedback that something is happening.
  - We update our view(s) only after we get a return from the server.
  - We need to account for us not receiving data back due to different interruptions/causes:
    - Server timeout
    - Wrong authentication information
    - User loses connection
    - Request URL not found
- [Representational state transfer (REST)](https://en.wikipedia.org/wiki/Representational_state_transfer) is the most common architecture style for passing information to and from these API endpoints.

**Quick Check:** With the person next to you, open the REST link above and in your own words, come up with a description of REST.

---

As many of you probably know, Foursquare is a quasi-Geo-spatial social network, geared towards surfacing recommendations, location, and coordinated meetups. The end-user accomplishes this through a combination of texting, geo-tagging, and light content creation in the form of recommendations/reviews/etc. Often times the service is accessed via a mobile device, although one can engage in Foursquare activity through a desktop/laptop as well.

The end user activity is incentivized/rewarded through accumulation of badges, titles (A sort of Gamification), and through getting (what's hoped) activity appropriate/contextualized coupons/discounts/sometimes free goods that are machine determined (i.e. some matching procedure/algorithm produced). Also, there is an intrinsic element to the incentive, like Facebook, many foursquare power-users end up using the service because their immediate friends/social network also utilize the service (the so-called "Network effect").


---

<a name = "demo"></a>
## Demo: Accessing the Foursquare API (15 mins)

Accessing the Foursquare API has become much simpler in recent years through the construction of 3rd party Python libraries that make the Oauth an data pull process much simpler, and wraps the data/meta-data in appropriate Python data-types.

We will use 'foursquare' in Python, which can be loaded up in your system via easy_install or pip in the usual way (i.e. `pip install foursquare`).

#### Foursquare API OAuth process  

**Brief Review:** "OAuth" is a web protocol for authentication with a third-party service, like when you try to sign up for a website and get directed to sign in with Google. Essentially, the website is using Google to prove who you are

To access the Foursquare API you must first register an App using the [foursquare App registration service](https://foursquare.com/developers/apps)

Setup your new "App"
<img = AppSN.png>

This will give you the credentials you need to pull/use Foursquare data.

```python
import foursquare
import pandas as pd

CLIENT_ID = ''   # Input your client id/ client secret here
CLIENT_SECRET = ''
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
```

We're going to do a fun exercise that looks at our local venues and do simple counts. The first thing we need to do is construct a bounding box around our geo-area. A simple tool for this is here: http://boundingbox.klokantech.com/. Select your home location, and create a bounding box around it. Make sure your output coordinates is set to "raw CSV". Get that data and input it into a python list

```python
# Example
#bounding_box = [x,y,z,t]  - Input the raw CSV file in here
```

<a name = "Guided"></a>
## Foursquare Data and Methods Overview (15 min)

> Note: Break timing for this into two section at 15min + 10 min each, respectively

Before we delve deeper into Python procedures, we need to understand the Foursquare data so we can better build a container to house the JSON data into a common tabular format.

```python
client.venues.search(params={'ll': 'x,y'})  # Put in a lat/long you're interested in
```

Observe that the data is housed in a nested hierarchy, we can access the data using the bracket notation in Python Pandas.

Ex:
u'stats': {u'checkinsCount': 7197, u'tipCount': 15, u'usersCount': 2266}

Can be accessed as data_frame['stats']['checkingCount']

#### Foursquare API Data Types (10 min)

Below is a useful table for data types that can be accessed in Foursquare. In general, Foursquare Data for the users require explicit permission. However, Venues data can be used for exploratory analysis with a user-less credential.

| Type  | General  | Aspects | Actions |  
|---|---|---|---|
| Users  | Search, Requests  | venuehistory, photos, tastes, friends, checkins, tips, venuelikes, mayorships, lists | deny, setpings, update, unfriend, approve |
| Venues | Search, SuggestionCompletion, Categories, Timeseries, Trending, Exploring, Add, Managed  | similar, photos, events, likes, nextvenues, hours, stats, links, menu, tips, herenow, listed | claim, dislike, flag, proposeedit, like, setrole, edit, setsinglelocation | update, addvenue, edit, removevenue |
| VenueGroups  | List, Delete, Add | timeseries | update, addvenue, edit, removevenue |
  checkins | Resolve, Recent, Add | likes | deletecomment, like, addpost, addcomment |
| tips | Add | likes, saves, listed |  unmark, flag, like | update, deleteitem, updateitem, follow, unfollow, moveitem,, share, additem |
| lists | Add | followers, suggestphoto, suggesttip, saves, items, suggestvenues | update, deleteitem, updateitem, follow, unfollow, moveitem, share, additem |
|updates | Notifications | | marknotificationsread |
| photos | Add | Read the docs! |Read the docs! |

---

<a name = "Indy"></a>
## Data-Crawling with Foursquare (15 minutes)

> Note: Have students discuss this in pairs with partners after reading the following question before moving on:

Suppose we wanted to generate a list of venues for a given geographical boundary, such as our previously defined bounded box. How would we go about doing so?

We could use a search procedure to go through the data bounded by a lat/long. First, we have to identify which columns we would like to include in our data frame.

```python
# We should include the lat, lon, name of the venue, and all of the data housed in hte "stats" heading in the JSON example.

venues = venues.append(pd.DataFrame({"name":res["venue"]["name"],"users":res["venue"]["stats"]["usersCount"],
"checkins":res["venue"]["stats"]["checkinsCount"], "tips":nv["stats"]["tipCount"], "lat":res["venue"]["location"]["lat"],
"lng":res["venue"]["location"]["lng"]}, index=[v]))
```

An important method we will explore for the independent practice is 'nextvenue' method. You can find more info on this method in [these API notes](https://developer.foursquare.com/docs/venues/nextvenues). The 'nextvenue' method:

"Returns venues that people often check in to after the current venue. Up to 5 venues are returned in each query, and results are sorted by how many people have visited that venue after the current one. Homes are never returned in results."

This method will form the kernel of a depth-first search procedure you will complete to crawl foursquare web-data.


## Foursquare Independent Practice (10 min)

To get more facility with Foursquare JSON structures, let's do a little practice. Select any resteraunt venue in your list of venues:

```python
client.venues('venue number here')
```

Now, your task is to extract a list of comments, and only the comments from the JSON. You can use the json library in Python to help you visualize the data in a more organized manner, but nothing else.

Now let's try something a bit more difficult. Select any venue in your list of venues:

```python
import json

temp = client.venues('4ba8cefdf964a520a9f039e3')
client.venues('4ba8cefdf964a520a9f039e3')

temp['venue']['tips']['groups']
# Use the Json library to better output your json dump, otherwise it will take you forever to traverse the hierarchy
print(json.dumps(temp, indent = 4))
# Compare the nested data-structure, how would you go deeper to extract the comments?
print(json.dumps(temp['venue']['tips']['groups'], indent = 4))
#Voila! Simple, and elegant, but requires you to understand how the different data types are nested in each other
map(lambda h: h['text'], temp['venue']['tips']['groups'][0]['items'])
```

---

<a name = "conclusion"></a>
## Conclusion (5 min)

Some parting thoughts on today's activities:

- Describe what an API allows you to do?
- How does an API response compare with a HTTP response in the browser?
- In what format is the data returned?

Excellent, we have done a lot in learning about the Foursquare API , and we now have a data set we can use for basic analysis. In the lab, we will engage in some exploratory analysis, and explore foursquare data more!


### ADDITIONAL RESOURCES

- [Working with APIs](https://zapier.com/learn/apis/chapter-1-introduction-to-apis/)
- [Foursquare Developer API docs](https://developer.foursquare.com)
