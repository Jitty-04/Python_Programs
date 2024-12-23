import pymysql
dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()
id=int(input("enter the id"))
sql="select * from Product_data"
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    if id==i[0]:
        sql=f"delete from Product_data where id={id}"
        mycursor.execute(sql)
        print('id deleted')
        break
else:
    print('id not found')
dbconnect.commit()



