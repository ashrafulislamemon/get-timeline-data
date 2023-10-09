from datetime import datetime

import sys

arg1=sys.argv[1]
import mysql.connector
from facebook_scraper import get_posts
profile_id=arg1
daten=datetime.now()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='sentimental')
cursor = conn.cursor()
for post in get_posts(profile_id, pages=10,cookies="cookies.txt"):
	# print(post)
	#print(post['text'][:50])
	#print(post['text'])


	print(post['timestamp'])
	# dt_obj = datetime.fromtimestamp(post['timestamp'])

	
	dt_obj=datetime.now()
	sql = "INSERT INTO new_trends (profile_id,content, status, reach, post_url, duration, post_creator,	my_get_date) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)"
	val = (profile_id,post['text'], 'pending', post['reaction_count'], post['post_url'],str(dt_obj), post['username'],daten)
	try:
		cursor.execute(sql, val)
		conn.commit()
	except:
		conn.rollback()
	print("Data inserted")

# Closing the connection
conn.close()

