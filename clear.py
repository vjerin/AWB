import pymysql as sql
import os


conn=sql.connect(host='localhost',user='root',password='',db='summer_training')
cur=conn.cursor()
cur.execute("""DELETE FROM awb""")
conn.commit()
cur.close()
conn.close()
os.system('cls')