import pymysql



conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zhoufangyu',db='app',charset='utf8');

cur = conn.cursor()

cur.execute("SELECT * FROM tab_agent")

for r in cur.fetchall():

           print(r[1])

cur.close()

conn.close()