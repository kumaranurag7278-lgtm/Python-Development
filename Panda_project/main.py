import pandas as pd



'''with open("weather_data.csv") as weather_report:
    data = weather_report.readlines()
    print(data)'''
# A better way to read csv files are using inbuilt csv package
'''
import csv
with open("weather_data.csv") as weather_report:
    data = csv.reader(weather_report)
    # Add a  variable containg only temperatur 
    temperature = []
    for row in data:
        temp =row[1]
        if temp != 'temp':

            temperature.append(int(temp))
    print(temperature)
'''
# Even shorter way 


data = pd.read_csv("weather_data.csv")
'''



# convert .csv to dic or list
data_list = data["temp"].to_list()
print(len(data_list))


average = data["temp"].mean()    #average value of temerature
print(average)


# max value of temp
max_value = data["temp"].max()
print(max_value)
'''


# Get Data in row
print(data[data.day == "Monday"])

# Which row of data have the highest temperature 
max_value = data["temp"].max()
print(data[data.temp == max_value])


