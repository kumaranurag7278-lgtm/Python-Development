# OBJECTIVE :To Take out all the primary colors and their total numbers into a diffrent file 
''' TODO -
1. convert the data file into dataframe 

2.Take only the unique Colors and its value__count into other variable

3.make another df of  number of counts of those unique colors

4. Create a file automatically of those data store in it .

'''

import pandas as pd

# import data from another file 


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# make it a data frame
color_data = pd.DataFrame(data)

# print(color_data.head())     head() is use to show the top 5 values of the df

# count the total number of values for each color 
# use value_count() to count the values


unique_color = color_data["Primary Fur Color"].value_counts()
final_data = pd.DataFrame(unique_color)



# create a new file for this data
final_data.to_csv("count_of_squirel.csv")


