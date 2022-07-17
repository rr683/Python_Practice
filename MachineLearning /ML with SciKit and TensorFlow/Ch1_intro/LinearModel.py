### Hands-on Machine Learning with SciKit-Learning, Keras and Tensor Flow ###
# Training a Linear Model using SciKit
# pg21
# Example 1-1 starts @pg 21

import urllib.request
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# Preparing for exmaple 1 -- jupyter notebook repository in GIT

## Python will look for data in this same directory within ch.1_intro folder as "datasets"
datapath = os.path.join("datasets", "lifesat", "")

## Getting data from repo and placing in this directory environment - SUPER HELPFUL
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
os.makedirs(datapath, exist_ok=True)
for filename in ("oecd_bli_2015.csv", "gdp_per_capita.csv"):
    print("Downloading", filename)
    url = DOWNLOAD_ROOT + "datasets/lifesat/" + filename
    urllib.request.urlretrieve(url, datapath + filename)


## Function merges OECD's life expectancy data with IMF's GDP

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    print(oecd_bli.head())
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    print(gdp_per_capita.head())
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    print(full_country_stats.head())
    return full_country_stats[["GDP per capita", "Life satisfaction"]].iloc[keep_indices]


# A simple linear model: life_satisfaction = theta_0 + (theta_1*GDP_Per_Capita)

## Load and read data

oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=",")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")

## prepare data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
x = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

##Visualize the data

country_stats.plot(kind="scatter", x="GDP per capita", y="Life satisfaction")
plt.show()

## select a linear model

model = sklearn.linear_model.LinearRegression()

#Train model

model.fit(x, y)

