
# create a new database
CREATE DATABASE youtube_db;

# use existing database youtube_db
USE youtube_db;

drop table playlist;

# create a table : Playlist
CREATE TABLE playlist (
  playlist_id varchar(255) NOT NULL,
  playlist_name varchar(255) NOT NULL,
  channel_id varchar(255) NOT NULL
);

drop table channel;

# create a table : Channel
CREATE TABLE channel(
	channel_id varchar(255) ,
	channel_name varchar(255),
    playlist_id varchar(255),
    subscribers varchar(10),
	channel_views int,
    video_count int,
	channel_description TEXT,
	country varchar(255)
);

drop table comment;

# create a table : Comment
CREATE TABLE comment(
	comment_id varchar(255),
	video_id varchar(255),
	comment_text TEXT ,
	comment_author varchar(255),
	comment_published_date varchar(255),
    like_count int,
    reply_count int
);
drop table video;
# create a table : Video
CREATE TABLE video(
	channel_name varchar(255),
	channel_id varchar(255),
    video_id varchar(255),
	title TEXT,
    tag varchar(255),
    thumbnail varchar(255),
	video_description TEXT ,
    published_date varchar(255) ,
    duration varchar(10) ,
	view_count varchar(10) ,
	like_count varchar(10) ,
	dislike_count varchar(10) ,
    comment_count varchar(10) ,
	favorite_count varchar(10) ,
	caption_status varchar(255)
);

show tables;
