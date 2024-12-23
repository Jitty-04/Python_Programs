import pymysql
dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()
sql="create table Product_data(id int auto_increment primary key,product_name varchar(50),price int)"
mycursor.execute(sql)
dbconnect.commit()
print("table created successfully")
