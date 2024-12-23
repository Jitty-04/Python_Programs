import pymysql
dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()
# sql="alter table Product_data add added_date date"
# mycursor.execute(sql)
# print("column added")
#YYYY-MM-DD
name=input('enter the product name').strip()
add_date=input('enter the date in the format yyyy-mm-dd').strip()
sql=f"update Product_data set added_date='{add_date}' where product_name='{name}'"
mycursor.execute(sql)
dbconnect.commit()
print('table updated')
