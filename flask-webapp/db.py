import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='********', db='test') # worked
#conn = MySQLdb.connect(host='ec2-13-234-120-184.ap-south-1.compute.amazonaws.com', user='', passwd='', db='test') # failing
cursor = conn.cursor()

cursor.execute('SELECT * FROM test')
row = cursor.fetchone()

conn.close()

print(row)
