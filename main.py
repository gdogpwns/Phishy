import requests
import json

URL = "http://phish.in/api/v1"


def get(param):
    #Pulls .json from Phish.in
    response = requests.get((URL + param))
    #Converts byte type to list
    info = response.json()
    print (info)
    #Gets only the data list within info
    data = info.get("data")
    #Gets only the tracks list within data
    tracks = data.get("tracks")
    # An incriment to see if the track exists
    i = 0
    mp3_list = []
    while True:
        try:
            tracks_dict = tracks[i]
        except:
            break
        else:
            mp3 = tracks_dict.get("mp3")
            mp3_list.append(mp3)
            i += 1
    print (mp3_list)


def date_search():
    # TODO: Change all inputs to voice inputs
    months = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}
    month_input = input("Month: ")
    month = months.get(month_input)
    day_input = input("Day: ")
    year_input = input("Year: ")
    date = (year_input + "-" + month + "-" + day_input)

    get("/shows/" + date)

date_search()