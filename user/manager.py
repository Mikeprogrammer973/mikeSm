from database.manager import Database

class User:
    _instance = None
    _logged_user = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            return cls._instance
        

    def __init__(self):
        self.db = Database()
        

    def login(self, username, password):
        """Authenticate the user"""
        cursor = self.db.get_connection().cursor()

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
        if self.db.get_connection() and self.db.get_connection().is_connected():
            self.db.get_connection().close()
            print("Closed...")