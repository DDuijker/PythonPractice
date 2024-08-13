import pandas

data = pandas.read_csv("squirel_data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

color_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}

data = pandas.DataFrame(color_data)
data.to_csv("./squirrel_count.csv")

