import pymysql
dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='Products')
mycursor=dbconnect.cursor()

pr_name=input('enter the product name')
price=int(input('enter the price'))

sql=f"insert into Product_data(product_name,price) values('{pr_name}',{price})"
mycursor.execute(sql)
dbconnect.commit()
print(f'{pr_name} details added to the table')