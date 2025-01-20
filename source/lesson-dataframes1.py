# What is a dataFrame? I like to think of it as a kind of table create during execution of a program
# Using SQL we can do everything with a table that is done with a dataFrame. 

# What is Pandas? an open-source library in Python for data manipulation and analysis. It provides 
# data structures and functions to efficiently handle structured data.

# Pandas offers two data structures:
# Series (1-dimensional labeled array)
# DataFrame (2-dimensional labeled data structure with columns of potentially different types)

# Data Manipulation: Pandas offers various functions for filtering, sorting, grouping, merging, reshaping, and pivoting data.
# Data Analysis: Pandas integrates well with other popular data analysis libraries in Python, such as NumPy, Matplotlib, and 
#                Scikit-learn.
# Data Input/Output: Pandas supports reading and writing data from various file formats, including CSV, Excel, JSON, and SQL 
#                    databases.

import pandas as pd

# DataFrames can be created from these sources: 
# 1. Dictionaries - unordered collection of key-value pairs, where:
# - Keys: Unique identifiers or labels (e.g., strings, integers)
# - Values: Associated data or objects (e.g., strings, integers, lists)

# dictionary = {'Name': ['John', 'Anna', 'Peter'],
#               'Age': [28, 24, 35],
#               'Country': ['USA', 'UK', 'Australia']}

# df = pd.DataFrame(dictionary)
# print(df)

# 2. From a List of Lists

# listOfLists = [['John', 28, 'USA'],
#                ['Anna', 24, 'UK'],
#                ['Peter', 35, 'Australia']]

# with a list of Lists, we can copy-paste what is above
# df = pd.DataFrame(listOfLists)
# print(df)

# but what if we gave it column headings corresponding to the data in each column, instead of 0, 1 and 2?
# we use columns= (a parameter of the DataFrame function) and define a list where each element corresponds 
# to the columns of the dataFrame.
# df = pd.DataFrame(listOfLists, columns=['Name', 'Age', 'Country'])
# print(df)
# Note: we can do this for any dataFrame we create.

# 3. From a NumPy Array
import numpy as np
# data = np.array([[1, 2, 3], [4, 5, 6]])

# df = pd.DataFrame(data, columns=['A', 'B', 'C'])
# print(df)

# These are interesting; however, I love data. Mockaroo is a good place to create your own data. 
# https://www.mockaroo.com/

# 4. From a CSV File
# df = pd.read_csv('resources/csv/school_data.csv')
# print(df)

# import openpyxl
# # 5. From an Excel File
# df = pd.read_excel('resources\csv\setCheatSheet.xlsx')
# print(df)

# 6. From a JSON File
df = pd.read_json('resources/json/school_data.json')
#print(df)

# Key Operations
# 1. Filtering: Selecting specific rows or columns based on conditions.

# Selecting Specific Rows Based on Conditions
#                    ---- 
# select rows where grade is less than 60.00
# filtered_grades_less_60_df = df[df['grade'] < 60.00]
# print(filtered_grades_less_60_df)

# filtered_grades_higher_class4 = df[(df['grade'] >= 60.00) & (df['class'] == 4) | (df['class'] == 3)]
# print(filtered_grades_higher_class4)

# Select rows where City is either "New York" or "Phoenix"
# filtered_df = df[df['last_name'].isin(['Aish', 'Kayley'])]
# print(filtered_df)

# Selecting Specific Columns Based on Conditions
#                    -------
# Select only the 'Name' and 'City' columns
# filter_first_grade = df[['first_name', 'grade']]
# print(filter_first_grade)

# Select 'Name' and 'Age' where City is 'New York'
# filter_class4 = df[df['class'] == 4][['first_name', 'grade']]
# print(filter_class4)

# Using .loc[] to filter rows based on condition and select specific columns
# filtered_class_4 = df.loc[df['class'] == 4, ['first_name', 'grade']]
# print(filtered_class_4)

# Using .iloc[] for position-based indexing
# print(df)
# selected_df = df.iloc[0:3, 0:2] # to select the first three rows and first two columns
# print(selected_df)

# 2. Sorting: Arranging data in ascending or descending order.
# sorted_df = filtered_grades_higher_class4.sort_values(by='grade')
# print(sorted_df)

# descending order
# sorted_df = sorted_df.sort_values(by='grade', ascending=False)
# print(sorted_df)

# Sorting by Multiple Columns
sorted_df = df.sort_values(by=['class', 'grade'])
print(sorted_df)

# sort the above data in ascending class order and descending grade order

# 3. groupby and agg, aggregating data by one or more columns.
# sum(): To sum the values within each group.
# mean(): To find the average within each group.
# count(): To count the number of entries in each group.
# min() / max(): To find the minimum or maximum value in each group.
# agg(): To apply multiple aggregation functions at once.

# count the number of students in each class: 
count_by_class_df = df.groupby('class').agg(total_students=('id', 'count')).reset_index()
print(count_by_class_df)

# what is the average grade in each class: 
mean_by_class_df = df.groupby('class').agg(average_grade = ('grade','mean')).reset_index()
print(mean_by_class_df)

# what is the max grade in each class: 
max_grade_class_df = df.groupby('class').agg(highest_grade = ('grade', 'max')).reset_index()
print(max_grade_class_df)

# aggregation for each class, student count, mean grade, max grade.
agg_count_mean_max_df = df.groupby('class').agg(
    total_students=('id', 'count'),
    average_grade=('grade', 'mean'),
    max_grade=('grade', 'max')
).reset_index()
print(agg_count_mean_max_df)

