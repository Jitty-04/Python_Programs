import pymysql


dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()

sql="select * from Product_data"
mycursor.execute(sql)

data=mycursor.fetchall()#complete data single data-fetchone

for i in data:
      print('id=',i[0], 'product name=',i[1],'price=',i[2])