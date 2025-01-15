import mysql.connector
from mysql.connector import Error

class User:
    _instance = None
    _logged_user = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            return cls._instance
        

    def __init__(self):
        self.connection = None
        self._connect_db()
        
    def _connect_db(self):
        """Connect to the remote database"""
        try:
            self.connection = mysql.connector.connect(
                host="sql.freedb.tech",
                user="freedb_mikeSm_",
                password="kSyK@amWU%79CMm",
                database="freedb_mikeSm"
            )
            if self.connection.is_connected():
                print("Connected...")
        except Error as e:
            print(f"Error while connecting to the remote database: {e}")

    def login(self, username, password):
        """Authenticate the user"""
        cursor =self.connection.cursor()

        cursor.execute("select * from users where username = %s and password = %s", (username, password))

        user = cursor.fetchone()

        if user:
            self._logged_user = {"name": user[0], "username": user[1]}
            print(f"\nWelcome back, {self._logged_user['name']}!\n")
        else:
            print("\nInvalid password or username!\n")

    def logout(self):
        """Disconnect the current logged user"""
        if self._logged_user:
            print(f"\nUser {self._logged_user['name']} logged out!\n")
            self._logged_user = None

    def get_logged_user(self):
        """Return the current logged user"""
        return self._logged_user
    
    def close_db_connection(self):
        """Close remote database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Closed...")