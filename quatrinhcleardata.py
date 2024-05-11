# -*- coding: utf-8 -*-
"""quatrinhcleardata.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-KvsbGrj8ZUXO4bSbw3sncDxXVn59YMe
"""

from google.colab import files
upload = files.upload()

import pandas as pd

df= pd.read_csv('e-shop clothing 2008.csv')

df

df[['	year','month','day','order','country','session ID','page 1 (main category)','page 2 (clothing model)','colour','location','model photography','price','price 2','page']]= df['year;month;day;order;country;session ID;page 1 (main category);page 2 (clothing model);colour;location;model photography;price;price 2;page'].str.split(';',expand = True)
df

df.drop('year;month;day;order;country;session ID;page 1 (main category);page 2 (clothing model);colour;location;model photography;price;price 2;page', axis = 1, inplace =True)

df

df.rename({'\tyear':'Year'}, axis = 1,inplace = True)
df

df.info()

df['month'] = df['month'].astype(str).astype(int)
df['day'] = df['day'].astype(str).astype(int)
df['order'] = df['order'].astype(str).astype(int)
df['country'] = df['country'].astype(str).astype(int)
df['session ID'] = df['session ID'].astype(str).astype(int)
df['page 1 (main category)'] = df['page 1 (main category)'].astype(str).astype(int)
df['colour'] = df['colour'].astype(str).astype(int)
df['location'] = df['location'].astype(str).astype(int)
df['model photography'] = df['model photography'].astype(str).astype(int)
df['price'] = df['price'].astype(str).astype(int)
df['price 2'] = df['price 2'].astype(str).astype(int)
df['page'] = df['page'].astype(str).astype(int)

df.dropna()

country_map = {
    "1": "Australia",
    "2": "Austria",
    "3": "Belgium",
    "4": "British Virgin Islands",
    "5": "Cayman Islands",
    "6": "Christmas Island",
    '7': "Croatia",
    '8': "Cyprus",
    '9': "Czech Republic",
    '10': "Denmark",
    "11": "Estonia",
    "12": "unidentified",
    "13": "Faroe Islands",
    "14": "Finland",
    "15": "France",
    "16": "Germany",
    '17': "Greece",
    "18": "Hungary",
    "19": "Iceland",
    "20": "India",
    "21": "Ireland",
    "22": "Italy",
    "23": "Latvia",
    "24": "Lithuania",
    "25": "Luxembourg",
    "26": "Mexico",
    "27": "Netherlands",
    "28": "Norway",
    "29": "Poland",
    "30": "Portugal",
    "31": "Romania",
    '32': "Russia",
    '33': "San Marion",
    "34": "Slovakia",
    "35": "Slovenia",
    "36": "Spain",
    '37': "Sweden",
    "38": "Switzerland",
    "39": "Ukraine",
    "40": "United Arab Emirates",
    "41": "United Kingdom",
    "42": "USA",
    "43": "biz (.biz)",
    "44": "com (.com)",
    "45": "int (.int)",
    "46": "net (.net)",
    "47": "org (*.org)"
}

df['country'] = df['country'].astype("string")
df["country"] = df["country"].map(country_map)

page1_map = {
    1: "trousers",
    2: "skirts",
    3: "blouses",
    4: "sale"
}
df["page 1 (main category)"] = df["page 1 (main category)"].map(page1_map)

location_map = {
    1: "top left",
    2: "top in the middle",
    3: "top right",
    4: 'bottom left',
    5: "bottom in the middle",
    6: "bottom right"
}

df["location"] = df["location"].map(location_map)

color_map = {
    1: "beige",
    2: "black",
    3: "blue",
    4: "brown",
    5: "burgundy",
    6: "gray",
    7: "green",
    8: "navy blue",
    9: "of many colors",
    10: "olive",
    11: "pink",
    12: "red",
    13: "violet",
    14: "white"
}

df["colour"] = df["colour"].map(color_map)

model_map = {
    1: "En face",
    2: "Profile"}

df["model photography"] = df["model photography"].map(model_map)

month_map = {
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
}

df["month"] = df["month"].map(month_map)

df

df.info()