import sqlite3
from flask import *
app = Flask(__name__)

db_source = "data.sqlite"

# Connecting to the database file
conn = sqlite3.connect(db_source)
c = conn.cursor()

'''c.execute("CREATE TABLE users ("
    "ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
    "name VARCHAR(30) NOT NULL,"
    "passw VARCHAR(100) NOT NULL"
")")'''

'''c.execute("INSERT INTO users(name, passw) values"
          "('admin', '1234')"
)'''


@app.route('/', methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['passw']
        c.execute("SELECT * from users WHERE name='" + user + "' and passw='" + passw + "';")
        if c.fetchone() is not None:
            return "Hello there"
        else:
            c.execute("INSERT INTO users(name, passw) values"
                      "('" + user + "', '" + passw + "')")
            conn.commit()
            return "user does not exist so we created you :)"
    else:
        return render_template("index.html")


app.run("0.0.0.0", port=8080)

conn.close()