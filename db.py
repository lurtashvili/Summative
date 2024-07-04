import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password='Lizuna777!',
    database="info"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT hotel_name, price FROM info")

myresult = mycursor.fetchall()

for x in myresult:
    hotel_name, price = x
    print(f"Hotel Name: {hotel_name}, Price: {price}")