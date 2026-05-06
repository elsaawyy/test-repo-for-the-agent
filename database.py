"""
Database module with issues
"""

import sqlite3
import pickle

# Global connection (bad practice)
connection = None

def get_connection():
    global connection
    if connection is None:
        connection = sqlite3.connect('test.db')
    return connection

# SQL injection vulnerability
def get_user_by_name(username):
    conn = get_connection()
    cursor = conn.cursor()
    # Dangerous: SQL injection!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# No error handling
def save_data(data):
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)  # Pickle is dangerous

# Too many responsibilities
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email, age, address, phone):
        # Too many parameters
        user = {
            'name': name,
            'email': email,
            'age': age,
            'address': address,
            'phone': phone
        }
        self.users.append(user)
        self.validate_user(user)
        self.save_to_database(user)
        self.send_notification(user)
        self.log_action(f"Added user {name}")
        return user
    
    def validate_user(self, user):
        if not user.get('name'):
            return False
        if not user.get('email'):
            return False
        return True
    
    def save_to_database(self, user):
        # Code duplication with above
        conn = get_connection()
        cursor = conn.cursor()
        query = f"INSERT INTO users VALUES ('{user['name']}', '{user['email']}')"
        cursor.execute(query)
        conn.commit()
    
    def send_notification(self, user):
        pass
    
    def log_action(self, message):
        with open('log.txt', 'a') as f:
            f.write(f"{message}\n")