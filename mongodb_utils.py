
import pymongo
import config

# Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
client = pymongo.MongoClient(config.MONGO_DB_CONNECTION_STRING)
db = client.youtube_data

# FUNCTION TO GET CHANNEL NAMES FROM MONGODB
def get_channel_names_from_mongodb():   
    ch_name = []
    for i in db.channel_details.find():
        ch_name.append(i['Channel_name'])
    return ch_name

def get_channel_details_from_mongodb():
    return db.channel_details

def get_video_details_from_mongodb():
    return db.video_details

def get_comments_details_from_mongodb():
    return db.comments_details