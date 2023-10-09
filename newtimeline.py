from datetime import datetime

import sys


import mysql.connector
from facebook_scraper import get_posts




# def dictfetchall(cursor):
#     columns = [col[0] for col in cursor.description]
#     return [dict(zip(columns, row)) for row in cursor.fetchall()]
# conn = mysql.connector.connect(user='root', password='', host='localhost', database='sentimental')
# cursor = conn.cursor()


# query='''SELECT profile_id FROM `pythonscripts_lockprofiledata`'''
# cursor.execute(query)


# data=dictfetchall(cursor)

# all_new=[]

# for i in data:
#     all_new.append(i["profile_id"])

all_new=["ducsuvpnur","profile.php?id=100093009597499","tuhin.fakir.10","profile.php?id=100083390656618","sohayel.arman"]


for i in all_new:

    try:

        profile_id=i
        daten=datetime.now()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='sentimental')
        cursor = conn.cursor()
        for post in get_posts(profile_id, pages=2,cookies="cookies.txt"):
           

            print(post['timestamp'])

            
            dt_obj=datetime.now()
            sql = "INSERT INTO new_trends (profile_id,content, status, reach, post_url, duration, post_creator,	my_get_date) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)"
            val = (profile_id,post['text'], 'pending', post['reaction_count'], post['post_url'],str(dt_obj), post['username'],daten)
            try:
                cursor.execute(sql, val)
                conn.commit()
            except:
                conn.rollback()
            print("Data inserted")

    
        conn.close()
    except:
        continue    