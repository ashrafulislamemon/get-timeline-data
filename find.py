import mysql.connector


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
conn = mysql.connector.connect(user='root', password='', host='localhost', database='sentimental')
cursor = conn.cursor()


query='''SELECT profile_id FROM `pythonscripts_lockprofiledata`'''
cursor.execute(query)


data=dictfetchall(cursor)

all_new=[]

for i in data:
    all_new.append(i["profile_id"])


