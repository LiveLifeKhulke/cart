import _mysql_connector

mydb=_mysql_connector(
    host= "localhost",
    user="root",
    password = 'Breaking1!'
)

mycursor = mydb.cursor('select name from selenium  where age =12')
mycursor.execute(

)

myresult =mycursor.fetchnone()
print(myresult[0])