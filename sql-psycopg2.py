import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist table"
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "Name" coliumn from the "Artist" table
# cursor.execute('SELECT "name" FROM "artist"')v

# Query 3 - select only "Queen" from the Artist table
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query 5 - select only the albums with "artistid" #51 on the 'Album' table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select all tracks where the ccomposer is Queen from the track table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection 
connection.close()

# print results
for result in results:
    print(result)
