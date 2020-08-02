# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (

)

""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user (

)
""")

song_table_create = """
CREATE TABLE IF NOT EXISTS song (
    id VARCHAR(255) PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    artist_id VARCHAR(255) REFERENCES artist(id) NOT NULL,
    year INT NOT NULL,
    duration NUMERIC NOT NULL
)
"""

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (

)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (

)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]