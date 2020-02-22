import mysql.connector

# conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
# cursor = conn.cursor()
# sql = "SELECT * FROM srhubapp_messengercategory;" 
# cursor.execute(sql)
# result = cursor.fetchall()

# category = []

# for row in result:
#     print(row)
#     category.append(row[1])

# print(category)


conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
cursor = conn.cursor()
sql = "SELECT id,name,description,picture,url,main_id FROM srhubapp_messengercategory;" 
cursor.execute(sql)
result = cursor.fetchall()
print(result)