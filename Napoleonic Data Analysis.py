#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In this file I am attempting to run some analytics on a db of napoleonic injuries from some czech website. This is a work in progress
#So far, I have completed the initial scrape of the data
#Stay tuned to see the analytics

import requests
from bs4 import BeautifulSoup
import pandas as pd

#function to convert ages into integers
def numeric_ages(age):
    #check if the value is a string, if yes, return age as an integer
    if age.isnumeric() == True:
        age = int(age)
    return age


#scrape page with Bsoup and requests
url = 'https://www.myczechroots.com/names-databases/database-of-casualties-of-napoleonic-wars-in-military-hospitals'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#get data from every column
regiments = soup.select('td.tableJX11Regiment')
battalions = soup.select('td.tableJX11Battalion')
companys = soup.select('td.tableJX11Company')
ranks = soup.select('td.tableJX11Rank')
names = soup.select('td.tableJX11Name')
#for class names with a space, I had to use .find_all instead of .select
birth_places = soup.find_all('td', class_ = 'tableJX11Birth place')
countrys = soup.select('td.tableJX11Country')
ages = soup.select('td.tableJX11Age')
religions = soup.select('td.tableJX11Religion')
marital_statuses = soup.select('td.tableJX11Status')
causes_of_death = soup.find_all('td', class_ = 'tableJX11Cause of death')
dates_of_death = soup.find_all('td', class_ = 'tableJX11Date of death')
hospitals = soup.select('td.tableJX11Hospital')

#empty list to collect dictionary
list = []

#iterate through data, collect it in a dictionary, append dictionary to empty list
for i in range(len(regiments)):
    regiment = regiments[i].get_text()
    battalion = battalions[i].get_text()
    company = companys[i].get_text()
    rank = ranks[i].get_text()
    name = names[i].get_text()
    birth_place = birth_places[i].get_text()
    country = countrys[i].get_text()
    age = numeric_ages(ages[i].get_text())
    religion = religions[i].get_text()
    marital_status = marital_statuses[i].get_text()
    cause_of_death = causes_of_death[i].get_text()
    date_of_death = dates_of_death[i].get_text()
    hospital = hospitals[i].get_text()
    data = {'regiment': regiment,
           'battalion': battalion,
           'company': company,
           'rank': rank,
           'name': name,
           'birth_place': birth_place,
           'country': country,
           'age': age,
           'religion': religion,
           'marital_status': marital_status,
           'cause_of_death': cause_of_death,
           'date_of_death': date_of_death,
           'hospital': hospital
           }
    list.append(data)
    
#Bon Apetit
print(list)


