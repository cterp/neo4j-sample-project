from pyechonest import song, config
from py2neo import Graph, authenticate
from tabulate import tabulate

# API key configuration and localhost access
config.ECHO_NEST_API_KEY = ""
authenticate("localhost:7474", username, password)
graph = Graph()

# user input parameters
user = raw_input("Please enter a user ID: ") or "d1000d372eed407ca20e8900a5f953f72dd3f558"

print

statement = "MATCH (u:User)-[:LISTENED_TO]->(s:Song) " \
            "WHERE u.user_id = {A} " \
            "RETURN s.song_id LIMIT 10"

record_list = []
records = graph.cypher.execute(statement, {"A": user})
print "Found songs, retrieving song metadata from EchoNest..."
print

for record in records:
    try:
        found_song = str(song.Song(record[0]))
        artist = str(song.Song(record[0]).artist_name)
    except IndexError:
        continue

    line = [found_song, artist]
    record_list.append(line)
print "Songs found: \n"
print tabulate(record_list, headers=["Song", "Artist"])