#http://weather.tuxnet24.de/?id=GMXX1210
import sqlite3
import time
conn = sqlite3.connect('wetter.db')
c = conn.cursor()
time = time.time()
temp = 10
speed = 5
hum = 66
# Create table
try :
    c.execute('''CREATE TABLE wetter(time float, current_temp float, speed float, humidity int)''')
except:
    pass
# Insert a row of data
c.executemany("INSERT INTO wetter VALUES (?, ?, ?, ?)", [(time, temp, speed, hum)])

# Save (commit) the changes
conn.commit()
c.execute("select * from wetter;")
if c.execute("SELECT COUNT (time) FROM wetter")>5:
    print("VOLL")
else:
    pass
print(c.fetchall())
conn.close()

