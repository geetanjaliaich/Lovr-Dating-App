import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1", user = "root", password="", database="tinder")
mycursor = conn.cursor()

#lines to create datbase. no longer needed
#mycursor.execute("CREATE DATABASE tinder")
#conn.commit()

# step 2: Create a Table
# user_id - Int ----> Primary Key ---> Not Null -- Auto_Increment
# name - Varchar --- Not Null
# email - Varchar --- Not Null
# password - Varchr --- Not Null

mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, romeo INT NOT NULL, juliet INT NOT NULL)")
conn.commit()

#create
#mycursor.execute("INSERT INTO users (user_id, name, email, password) VALUES (NULL, 'Geetanjali Aich', 'geetanjali.aich@gmail.com', 'jkrowling')")
#conn.commit()

#retrieve
#mycursor.execute("SELECT * FROM users WHERE email LIKE 'virat@gmail.com'")
#data = mycursor.fetchall()
#print(data)

#for i in data:
#    print(i[1])

#Update
#mycursor.execute("UPDATE users SET password='vk' WHERE user_id=1")
#conn.commit()

#Delete
#mycursor.execute("DELETE FROM users WHERE user_id=2")
#conn.commit()
