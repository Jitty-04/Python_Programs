import pymysql


dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()

product=input('enter the product')
sql=f"select product_name,price from Product_data where product_name='{product}'"
mycursor.execute(sql)

data=mycursor.fetchone()
if data:
    print('product name=', data[0], '\nprice=', data[1])

else:
    print('object is not found')

