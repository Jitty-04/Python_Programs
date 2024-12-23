import pymysql
dbconnect=pymysql.connect(host='localhost',user='root',password='password@123')

#cursorobject-used to execute sql commands and also used to fetch data in mysql
mycursor=dbconnect.cursor()

sql="create database Products"

mycursor.execute(sql)
dbconnect.commit()#to save updates

print('database created successfully...')


