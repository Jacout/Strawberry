import pandas as pd
from TikTokApi import TikTokApi

# Function to ask for user input
def inputUserID(user):
    userName = input("Enter Username: ")
    userInfo = api.get_user(userName)
    userID = userInfo['id']
    secUID = userInfo['secUid']
    return userID, secUID

# Function to scrape user videos
def getUserVideos(userDefID, secDefUID):
    cursorValue = 0
    hasMore = True
    df = pd.DataFrame()

    while hasMore:
        TikTokList = api.user_page(userID=userDefID, secUID=secDefUID, cursor=cursorValue)
        data = cleanData(TikTokList['itemList'])
        df = df.append(data)
        cursorValue = int(TikTokList['cursor'])
        hasMore = TikTokList['hasMore']

    df.to_csv('UserVideos.csv')

# Function to clean the data
def cleanData(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
    flattened_data = {}

    for id, value in enumerate(data):
        flattened_data[id] = {}

        for prop_id, prop_value in value.items():
            if prop_id in nested_values:
                for nested_id, nested_value in prop_value.items():
                    flattened_data[id][prop_id + '_' + nested_id] = nested_value
            else:
                flattened_data[id][prop_id] = prop_value

    return pd.DataFrame.from_dict(flattened_data)


def iniciar():
    # Initialize the API
    api = TikTokApi.get_instance()

    # Get user ID and secUID
    userInfo = inputUserID()

    # Scrape user videos
    getUserVideos(userInfo[0], userInfo[1])