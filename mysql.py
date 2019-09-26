import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"

)

mycursor=mydb.cursor()
mycursor.execute("use kunja")
mycursor.execute("create table students(st_no integer(10),st_name varchar(50),primary key(st_no))")

#mycursor.execute("INSERT INTO student (st_no,st_name) VALUES (6, "Highway")")

mydb.commit()

print(mycursor.rowcount, "record inserted.")