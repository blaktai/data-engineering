# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES
songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplay (
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp NOT NULL, 
    user_id VARCHAR REFERENCES users(user_id) NOT NULL,
    level VARCHAR NOT NULL,
    song_id VARCHAR REFERENCES song(song_id),
    artist_id VARCHAR REFERENCES artist(artist_id),
    session_id VARCHAR NOT NULL,
    location VARCHAR,
    user_agent VARCHAR NOT NULL
)
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1) NOT NULL,
    level VARCHAR NOT NULL
)
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS song (
    song_id VARCHAR PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INT NOT NULL,
    duration NUMERIC NOT NULL
)
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artist (
    artist_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    latitude VARCHAR,
    longitude VARCHAR
)
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY NOT NULL,
                        hour INT NOT NULL,
                        day INT NOT NULL,
                        week INT NOT NULL,
                        month INT NOT NULL,
                        year INT NOT NULL,
                        weekday VARCHAR NOT NULL
)
"""

# INSERT RECORDS

songplay_table_insert = """
INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES
 (%s,%s,%s,%s,%s,%s,%s,%s)
"""

user_table_insert = """
    INSERT INTO users (user_id, first_name, last_name, gender, level ) VALUES
    (%s,%s,%s,%s,%s)
    ON CONFLICT (user_id) 
    DO UPDATE SET level = excluded.level
"""

song_table_insert = """
    INSERT INTO song (song_id, title, artist_id, year, duration) VALUES
     (%s,%s,%s,%s,%s)
     ON CONFLICT (song_id)
     DO NOTHING
"""

artist_table_insert = """INSERT INTO artist (artist_id, name, location, latitude, longitude) VALUES
(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id)
     DO NOTHING
"""

time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES 
    (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (start_time)
     DO NOTHING
"""

# FIND SONGS

song_select = """ SELECT s.song_id, a.artist_id FROM song s
    JOIN artist a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s
"""

# QUERY LISTS

create_table_queries = [
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]

