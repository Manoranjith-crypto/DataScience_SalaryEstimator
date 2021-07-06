# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:01:23 2021

@author: Manoranjith
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Manoranjith/Documents/DS_Project/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)