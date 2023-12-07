import csv

# data = []
#
# with open('./weather_data.csv') as weather_data:
#     for row in weather_data:
#         row = row.strip("\n")
#         data.append(row)
#

# Shorter version
# with open('./weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#

# --CSV reader--
# with open('./weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# --Using pandas--
import pandas

data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# Average temp
# avg = sum(temp_list) / len(temp_list)
# print(round(avg, 2))

# print(data["temp"].mean())
max_temp = data["temp"].max()

# you can use data.temp or data["temp"], case-sensitive

# Get row of highest temperature
# print(data[data.temp == max_temp])

monday_temp_c = data[data.day == "Monday"]["temp"]
monday_temp_f = (1.8 * monday_temp_c) + 32
# print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "grades": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./student_data.csv")

