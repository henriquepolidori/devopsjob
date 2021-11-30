# Module Imports
import mysql.connector as mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="7sLLqEJSVk",
        host="my-mariadb.default.svc.cluster.local",
        port=3306,
        database="mysql"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("SELECT * FROM user WHERE User='root'")

myresult = cur.fetchall()

for x in myresult:
  print(x)