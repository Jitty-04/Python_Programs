import pymysql

dbconnect=pymysql.connect(host='localhost',user='root',password='password@123',database='website')
mycursor=dbconnect.cursor()

class Website:
    def register_user(self,name,email,phone,password):
        sql = f"insert into register(name,email,phone,password) values('{name}','{email}',{phone},'{password}')"
        mycursor.execute(sql)
        dbconnect.commit()
        print('registration successfull')

    def login_user(self,email,password):
        sql = "select email,password from register"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            if email == i[0] and password== i[1]:
               print("login successful")
               break
        else:
            print('Login failed')
        dbconnect.commit()

    #
    def delete_user(self,email,password):
            sql = "select email,password from register"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in result:
                if email == i[0] and password== i[1]:
                   sql=f"delete from register where email='{email}'"
                   mycursor.execute(sql)
                   print("Deleted successfully")
                   break
            else:
                print('User not found')
            dbconnect.commit()

    def user_display(self,email,password):
        sql = "select email,password from register"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            if email == i[0] and password == i[1]:
                sql = f"select * from register where email='{email}'"
                mycursor.execute(sql)
                data=mycursor.fetchone()
                print(f"id={data[0]}\nname={data[1]}\ngmail={data[2]}\nphone={data[3]}\npassword={data[4]}")
                break
        else:
                print("user not found")


obj=Website()
# obj.register_user('Nathz','nathz04@gmail.com',980391989,'Nathz@004')
# obj.login_user("nat04@gmail.com","Nathz@004")
# obj.delete_user("nathz04@gmail.com","Nathz@004")
obj.user_display("jincy12@gml.com","Jincy@12")


