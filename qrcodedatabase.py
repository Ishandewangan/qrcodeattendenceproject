import mysql.connector


def databaseCreate():
    cnx = mysql.connector.connect(user='root', password='Ishan@2000', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS attendence")
    Cursor.execute("")
    Cursor.close()
    cnx.close()

def tableCreate():
    cnx = mysql.connector.connect(user='root', password='Ishan@2000', host='localhost',database='attendence')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Student_attendence(S_no int UNIQUE KEY AUTO_INCREMENT ,Name varchar(20),Roll_no int PRIMARY KEY,Attendence varchar(20),M_no bigint(10)) ")
    Cursor.close()
    cnx.close()


def insertValue(x,y,z,c):
    cnx = mysql.connector.connect(user='root', password='Ishan@2000', host='localhost',database='attendence')
    Cursor = cnx.cursor(buffered=True)
    query="INSERT INTO Student_attendence(Name,Roll_no,Attendence,M_no) values(%s,%s,%s,%s)"
    val=(x,y,z,c)
    Cursor.execute(query,val)
    cnx.commit()
    Cursor.close()
    cnx.close()

def dataVerify(a,b):
    cnx = mysql.connector.connect(user='root', password='Ishan@2000', host='localhost',database='attendence')
    Cursor = cnx.cursor(buffered =True)
    query=f"SELECT * FROM student_attendence WHERE roll_no = {a} "
    Cursor.execute(query)
    myresult = Cursor.fetchall()
    if(str(myresult[0][3]) != 'None'):
        print("Already Marked")
    else:
        Cursor.execute("update student_attendence set attendence=(%s) where roll_no=(%s)",(b,a))
        cnx.commit()
        print("Your Attendence Marked")

def dataFetch():
    cnx = mysql.connector.connect(user='root', password='Ishan@2000', host='localhost',database='attendence')
    Cursor = cnx.cursor()
    Cursor.execute("SELECT * FROM student_attendence")
    myresult = Cursor.fetchall()
    for x in myresult:
        print(x)
