import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu


from PIL import Image

from youtube_utils import get_channel_details_from_youtube, get_channel_videos_from_youtube, get_comments_details_from_youtube, get_video_details_from_youtube
from mysql_utils import insert_into_channels, insert_into_comments, insert_into_videos, execute_query
from mongodb_utils import get_channel_names_from_mongodb, get_channel_details_from_mongodb, get_video_details_from_mongodb, get_comments_details_from_mongodb

import constants

# SETTING PAGE CONFIGURATIONS
icon = Image.open("./asset/youtube.png")
st.set_page_config(page_title= "YouTube Data Harvesting and Warehousing using SQL, MongoDB and Streamlit | By Prithivy",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This app is created by *Prithivy (prithivyvampire@gmail.com) !*"""})

# CREATING OPTION MENU
with st.sidebar:
    selected = option_menu(None, ["Home","Extract","Transform","View"], 
                           icons=["house-door-fill","tools","card-text"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#C80101"},
                                   "icon": {"font-size": "30px"},
                                   "container" : {"max-width": "6000px"},
                                   "nav-link-selected": {"background-color": "#C80101"}})




# HOME PAGE
if selected == "Home":
    # Title Image
    col1, col2, col3 = st.columns(3)
    col2.image("./asset/title.png", width=400)
    col1,col2 = st.columns(2,gap= 'medium')
    col1.markdown("## :blue[Domain] : Social Media")
    col1.markdown("## :blue[Technologies used] : Python,MongoDB, Youtube Data API, MySql, Streamlit")
    col2.markdown("## :blue[Overview] : Retrieving the Youtube channels data from the Google API, storing it in a MongoDB as data lake, migrating and transforming data into a SQL database,then querying the data and displaying it in the Streamlit app.")
   
    
    
# EXTRACT PAGE
if selected == "Extract":
    st.write("## :orange[Enter YouTube Channel_ID below : ]")
    ch_id = st.text_input("Hint : Goto channel's home page > Right click > View page source > Find channel_id").split(',')

    if ch_id and st.button("Extract Data"):
        ch_details = get_channel_details_from_youtube(ch_id)
        st.write(f'#### Extracted data from :green["{ch_details[0]["Channel_name"]}"] channel')
        st.table(ch_details)

    if st.button("Upload to MongoDB"):
        with st.spinner('Please Wait for it...'):
            ch_details = get_channel_details_from_youtube(ch_id)
            v_ids = get_channel_videos_from_youtube(ch_id)
            vid_details = get_video_details_from_youtube(v_ids)
            
            def flatten_comments():
                com_d = []
                for i in v_ids:
                    com_d+= get_comments_details_from_youtube(i)
                return com_d
            comm_details = flatten_comments()

            channels = get_channel_details_from_mongodb()
            channels.insert_many(ch_details)

            videos = get_video_details_from_mongodb()
            videos.insert_many(vid_details)

            comments = get_comments_details_from_mongodb()
            comments.insert_many(comm_details)
            st.success("Upload to MogoDB successful !!") 
        

# TRANSFORM PAGE                
if selected == "Transform":
    st.markdown("## :orange[Select a channel to begin Transformation to SQL]")
    
    ch_names = get_channel_names_from_mongodb()
    user_inp = st.selectbox("Select channel",options= ch_names)
    
    if st.button("Submit"):
        try:
            insert_into_channels(user_inp, get_channel_details_from_mongodb())
            insert_into_videos(user_inp, get_video_details_from_mongodb())
            insert_into_comments(user_inp, get_video_details_from_mongodb(), get_comments_details_from_mongodb())
            st.success("Transformation to MySQL Successful !!")
        except:
            st.error("Channel details already transformed !!")

# VIEW PAGE
if selected == "View":
    
    st.write("## :orange[Select any question to get Insights]")
    questions = st.selectbox('Questions',
    [constants.QUESTION_1,
     constants.QUESTION_2,
     constants.QUESTION_3,
     constants.QUESTION_4,
     constants.QUESTION_5,
     constants.QUESTION_6,
     constants.QUESTION_7,
     constants.QUESTION_8,
     constants.QUESTION_9,
     constants.QUESTION_10
    ])
    
    if questions == constants.QUESTION_1:
        cursor = execute_query(constants.QUESTION_QUERY_1)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        
    elif questions == constants.QUESTION_2:
        cursor = execute_query(constants.QUESTION_QUERY_2)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Number of videos in each channel :]")
        fig = px.bar(df,
                     x=cursor.column_names[0],
                     y=cursor.column_names[1],
                     orientation='v',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    elif questions == constants.QUESTION_3:
        cursor = execute_query(constants.QUESTION_QUERY_3)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Top 10 most viewed videos :]")
        fig = px.bar(df,
                     x=cursor.column_names[2],
                     y=cursor.column_names[1],
                     orientation='h',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    elif questions == constants.QUESTION_4:
        cursor = execute_query(constants.QUESTION_QUERY_4)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
          
    elif questions == constants.QUESTION_5:
        cursor = execute_query(constants.QUESTION_QUERY_5)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Top 10 most liked videos :]")
        fig = px.bar(df,
                     x=cursor.column_names[2],
                     y=cursor.column_names[1],
                     orientation='h',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    elif questions == constants.QUESTION_6:
        cursor = execute_query(constants.QUESTION_QUERY_6)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
         
    elif questions == constants.QUESTION_7:
        cursor = execute_query(constants.QUESTION_QUERY_7)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Channels vs Views :]")
        fig = px.bar(df,
                     x=cursor.column_names[0],
                     y=cursor.column_names[1],
                     orientation='v',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    elif questions == constants.QUESTION_8:
        cursor = execute_query(constants.QUESTION_QUERY_8)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        
    elif questions == constants.QUESTION_9:
        cursor = execute_query(constants.QUESTION_QUERY_9)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Avg video duration for channels :]")
        fig = px.bar(df,
                     x=cursor.column_names[0],
                     y=cursor.column_names[1],
                     orientation='v',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    elif questions == constants.QUESTION_10:
        cursor = execute_query(constants.QUESTION_QUERY_10)
        df = pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        st.write(df)
        st.write("### :green[Videos with most comments :]")
        fig = px.bar(df,
                     x=cursor.column_names[1],
                     y=cursor.column_names[2],
                     orientation='v',
                     color=cursor.column_names[0]
                    )
        st.plotly_chart(fig,use_container_width=True)
        
        