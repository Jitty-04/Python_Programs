import pymysql
# dbconnect=pymysql.connect(host='localhost',user='root',password='password@123')
# mycursor=dbconnect.cursor()
# sql="create database Website"
# mycursor.execute(sql)
# dbconnect.commit()
# print('database created successfully...')

dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='website')
mycursor=dbconnect.cursor()
sql="create table register(id int auto_increment primary key,name varchar(50),email varchar(50) unique,phone bigint unique,password varchar(50))"
mycursor.execute(sql)
dbconnect.commit()
print('table created successfully...')