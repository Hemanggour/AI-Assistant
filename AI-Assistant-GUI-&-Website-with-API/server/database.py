import mysql.connector as sql

class Database:
    def __connectDB(self):
        # self.mydb = sql.connect(host="HemangGour.mysql.pythonanywhere-services.com", user="HemangGour", password="812004@MySQL", database="HemangGour$todolistdb")
        self.mydb = sql.connect(host="localhost", user="root", password="812004Hemang", database="todolistdb", charset="utf8mb4")
        self.cur = self.mydb.cursor()

    def __init__(self):
        self.__connectDB()
        # self.dataBase = "HemangGour$todolistdb"
        self.dataBase = "webAI"
        self.table_users = "users"
        self.table_chats = "chats"
        self.table_tokens = "tokens"
        self.table_verifyEmail = 'verifyEmail'

    def createTables(self):
        query = f"""CREATE TABLE IF NOT EXISTS {self.dataBase}.{self.table_users}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        apikey varchar(255) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL);"""
        self.cur.execute(query)
        self.mydb.commit()

        query = f"""CREATE TABLE IF NOT EXISTS {self.dataBase}.{self.table_tokens} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        token VARCHAR(255) NOT NULL,
        expires_at DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES {self.dataBase}.{self.table_users}(id) ON DELETE CASCADE);"""
        self.cur.execute(query)
        self.mydb.commit()

        query = f"""CREATE TABLE IF NOT EXISTS {self.dataBase}.{self.table_verifyEmail} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL,
        token VARCHAR(255) NOT NULL,
        expires_at DATETIME NOT NULL);"""
        self.cur.execute(query)
        self.mydb.commit()

        query = f"""CREATE TABLE IF NOT EXISTS {self.dataBase}.{self.table_chats} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        message TEXT NOT NULL,
        sender ENUM('user', 'ai') NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES {self.dataBase}.{self.table_users}(id) ON DELETE CASCADE
        );"""
        self.cur.execute(query)
        self.mydb.commit()

    # Insert a message
    def addMessage(self, userId, message, sender):
        query = f"INSERT INTO {self.dataBase}.{self.table_messages} (user_id, message, sender) VALUES (%s, %s, %s);"
        self.cur.execute(query, (userId, message, sender))
        self.mydb.commit()

    # Retrieve messages for a specific user
    def getMessages(self, userId):
        query = f"SELECT message, sender, timestamp FROM {self.dataBase}.{self.table_messages} WHERE user_id = %s ORDER BY timestamp ASC;"
        self.cur.execute(query, (userId,))
        return self.cur.fetchall()

    # Delete all messages for a specific user
    def deleteMessagesByUser(self, userId):
        query = f"DELETE FROM {self.dataBase}.{self.table_messages} WHERE user_id = %s;"
        self.cur.execute(query, (userId,))
        self.mydb.commit()