import pandas as pd
import json
import os

follow_data = pd.read_json("Follow.json")
follow_data.to_csv('follow.csv')
search = pd.read_json("SearchQueries.json")
search.to_csv('search.csv')
stream0 = pd.read_json("StreamingHistory0.json")
stream0.to_csv('stream0.csv')
stream1 = pd.read_json("StreamingHistory1.json")
stream1.to_csv('stream1.csv')
stream2 = pd.read_json("StreamingHistory2.json")
stream2.to_csv('stream2.csv')
stream3 = pd.read_json("StreamingHistory3.json")
stream3.to_csv('stream3.csv')
stream4 = pd.read_json("StreamingHistory4.json")
stream4.to_csv('stream4.csv')


with open('YourLibrary.json') as data:
    d = json.load(data)

df = pd.DataFrame.from_dict(d, orient='index')
df = df.transpose()
df.to_csv('library.csv')
