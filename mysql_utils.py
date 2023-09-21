
import mysql.connector as sql
import config

# CONNECTING WITH MYSQL DATABASE
db = sql.connect(host=config.MYSQL_HOST_NAME,user=config.MYSQL_USER_NAME,password=config.MYSQL_PASSWORD,database= config.MYSQL_DATABASE,auth_plugin='mysql_native_password')
cursor = db.cursor(buffered=True)

def insert_into_channels(user_inp, channels):
        query = """INSERT INTO channel VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        for i in channels.find({"Channel_name" : user_inp},{'_id' : 0}):
            cursor.execute(query,tuple(i.values()))
            db.commit()
        
def insert_into_videos(user_inp, videos):
    query1 = """INSERT INTO video VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    for i in videos.find({"Channel_name" : user_inp},{'_id' : 0}):
        cursor.execute(query1,tuple(i.values()))
        db.commit()

def insert_into_comments(user_inp, videos, comments):
    query2 = """INSERT INTO comment VALUES(%s,%s,%s,%s,%s,%s,%s)"""

    for vid in videos.find({"Channel_name" : user_inp},{'_id' : 0}):
        for i in comments.find({'Video_id': vid['Video_id']},{'_id' : 0}):
            cursor.execute(query2,tuple(i.values()))
            db.commit()
        

def execute_query(query):
    cursor.execute(query)
    return cursor