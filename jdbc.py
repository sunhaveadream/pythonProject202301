import jaydebeapi

url = 'jdbc:mysql://localhost:3306/test_db'

user = 'root'

password = '123456'

dirver = 'com.mysql.cj.jdbc.Driver'

jarFile = 'D:\softwares\mysql-connector-j-8.0.33\mysql-connector-j-8.0.33\mysql-connector-j-8.0.33.jar'

sqlStr = 'select * from users;'

conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)

curs=conn.cursor()

curs.execute(sqlStr)

result=curs.fetchall()

print(result)

curs.close()

conn.close()