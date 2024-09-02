import psycopg2

user='postgres.sxonhwjbhsaongvgemzc' 
password='Cautter@030601'
host='aws-0-us-west-1.pooler.supabase.com' 
port=6543 
dbname='postgres'

connection = psycopg2.connect(
    database='postgres'
    , user='postgres.sxonhwjbhsaongvgemzc' 
    , password=password
    , host='aws-0-us-west-1.pooler.supabase.com' 
    , port=5432
)

cursor = connection.cursor()

cursor.execute("SELECT current_user;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)