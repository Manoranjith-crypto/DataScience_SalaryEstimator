# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:23:36 2021

@author: Manoranjith
"""



import pandas as pd

df = pd.read_csv("C:/Users/Manoranjith/Documents/DS_Project/glassdoor_jobs.csv")

#salary parsing

df['hourly salary'] = df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower() else 0)
df['employer salary'] = df['Salary Estimate'].apply(lambda x:1 if 'employer provided salary' in x.lower() else 0)

df =df[df['Salary Estimate'] != '-1']
Salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0] )

minus = Salary.apply(lambda x:x.replace('K','').replace('$',''))
min_hr= minus.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#compsny name

df['Company '] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis =1)

#Company Age

df['Age'] = df['Founded'].apply(lambda x: x if x<1 else 2021 - x)

#State 

df['Job_State'] = df['Location'].apply(lambda x: x.split(',')[1])

#Headquartres

df['Same_State'] = df.apply (lambda x: 1 if x.Headquarters == x.Job_State else 0, axis =1)

#Skills ->Python -> R-Studio ->AWS ->Spark ->Excel

#->Python
df['Python_skill'] = df['Job Description'].apply (lambda x: 1 if 'python' in x.lower() else 0)
df.Python_skill.value_counts()

#->R-Studio
df['R_skill'] = df['Job Description'].apply (lambda x: 1 if 'r-studio' or 'r studio' in x.lower() else 0)
df.R_skill.value_counts()

#->AWS
df['AWS_skill'] = df['Job Description'].apply (lambda x: 1 if 'aws' in x.lower() else 0)
df.AWS_skill.value_counts()

#->Spark
df['Spark_skill'] = df['Job Description'].apply (lambda x: 1 if 'spark' in x.lower() else 0)
df.Spark_skill.value_counts()

#->Excel
df['Excel_skill'] = df['Job Description'].apply (lambda x: 1 if 'excel' in x.lower() else 0)
df.Excel_skill.value_counts()

#Droping unwanted column

df1 = df.drop(['Unnamed: 0'], axis =1)

#Save the cleaned data to new csv file (Cleaned_data.csv)
df1.to_csv('Cleaned_data.csv', index =False)

pd.read_csv('Cleaned_data.csv' )

