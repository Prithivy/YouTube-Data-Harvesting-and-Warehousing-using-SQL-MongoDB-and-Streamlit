
## Questions 
QUESTION_1 = "1. What are the names of all the videos and their corresponding channels?"
QUESTION_2 = "2. Which channels have the most number of videos, and how many videos do they have?"
QUESTION_3 = "3. What are the top 10 most viewed videos and their respective channels?"
QUESTION_4 = "4. How many comments were made on each video, and what are their corresponding video names?"
QUESTION_5 = "5. Which videos have the highest number of likes, and what are their corresponding channel names?"
QUESTION_6 = "6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?"
QUESTION_7 = "7. What is the total number of views for each channel, and what are their corresponding channel names?"
QUESTION_8 = "8. What are the names of all the channels that have published videos in the year 2022?"
QUESTION_9 = "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?"
QUESTION_10 = "10. Which videos have the highest number of comments, and what are their corresponding channel names?"


## Questions fetch Query 
QUESTION_QUERY_1 = """SELECT title AS Video_Title, channel_name AS Channel_Name
                            FROM video
                            ORDER BY channel_name"""
QUESTION_QUERY_2 = """SELECT channel_name AS Channel_Name, video_count AS Total_Videos
                            FROM channel
                            ORDER BY video_count DESC"""
QUESTION_QUERY_3 = """SELECT channel_name AS Channel_Name, title AS Video_Title, view_count AS Views 
                            FROM video
                            ORDER BY views DESC
                            LIMIT 10"""
QUESTION_QUERY_4 = """SELECT a.video_id AS Video_id, a.title AS Video_Title, b.Total_Comments
                            FROM video AS a
                            LEFT JOIN (SELECT video_id,COUNT(comment_id) AS Total_Comments
                            FROM comment GROUP BY video_id) AS b
                            ON a.video_id = b.video_id
                            ORDER BY b.Total_Comments DESC"""
QUESTION_QUERY_5 = """SELECT channel_name AS Channel_Name,title AS Title,like_count AS Likes_Count 
                            FROM video
                            ORDER BY like_count DESC
                            LIMIT 10"""
QUESTION_QUERY_6 = """SELECT title AS Title, like_count AS Likes_Count
                            FROM video
                            ORDER BY like_count DESC"""
QUESTION_QUERY_7 = """SELECT channel_name AS Channel_Name, channel_views AS Views
                            FROM channel
                            ORDER BY channel_views DESC"""
QUESTION_QUERY_8 = """SELECT channel_name AS Channel_Name
                            FROM video
                            WHERE published_date LIKE '2022%'
                            GROUP BY channel_name
                            ORDER BY channel_name"""
QUESTION_QUERY_9 = """SELECT channel_name AS Channel_Name,
                            AVG(duration)/60 AS "Average_Video_Duration (mins)"
                            FROM video
                            GROUP BY channel_name
                            ORDER BY AVG(duration)/60 DESC"""
QUESTION_QUERY_10 = """SELECT channel_name AS Channel_Name,video_id AS Video_ID,comment_count AS Comments
                            FROM video
                            ORDER BY comment_count DESC
                            LIMIT 10"""


##UC98iMDij96Xx9XZs_Yo0FPQ
