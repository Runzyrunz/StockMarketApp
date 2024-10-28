import bcrypt

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='RedRebel1312',
    database='stocks'
)

mycursor = mydb.cursor()  # Initialize cursor of database

mycursor.execute("DROP TABLE IF EXISTS accounts")

# Create the accounts table with additional fields: email, portfolio, money, and ranking
mycursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    portfolio TEXT,
    money DECIMAL(10, 2) DEFAULT 0.00,
    ranking INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Define your account data
accounts = [
    ("Bob", hash_password("password123"), "bob@example.com", "AAPL,GOOGL", 1500.75, 1),
    ("Amanda", hash_password("mypassword321"), "amanda@example.com", "TSLA,MSFT", 3200.50, 2),
    ("Jacob", hash_password("securepass"), "jacob@example.com", "AMZN,NVDA", 5000.25, 3),
    ("Avi", hash_password("passAvi28"), "avi@example.com", "NFLX,FB", 2800.10, 4),
    ("Michelle", hash_password("michelleSecret"), "michelle@example.com", "AMD,INTC", 1700.00, 5),
]

# SQL query for inserting into the 'accounts' table
sqlFormula = """
INSERT INTO accounts (username, password, email, portfolio, money, ranking) 
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Insert multiple accounts into the table
mycursor.executemany(sqlFormula, accounts)

# Commit the changes
mydb.commit()

print(mycursor.rowcount, "accounts inserted.")
