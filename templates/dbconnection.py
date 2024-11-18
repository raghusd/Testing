#import connector package
import snowflake.connector as sf
#connetion details
conn = sf.connect(account='ahyvjlr-hd34835',
                  user='Niranjana',
                  password='Jana@1308',
                  warehouse='Compute_WH',
                  database='Swift',
                  schema='Connection')
#create cusor object
print(type(conn))
cur = conn.cursor()
try:
  # execute the query
  cur.execute("select * from employee")
  # fetch all the results
  result = cur.fetchall()
  #print all the results
  for row in result:
    print(row)
finally:
  # close the cursor and connection
  cur.close()
  conn.close()
print('Connection successful')