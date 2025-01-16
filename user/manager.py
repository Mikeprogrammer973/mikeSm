from database.manager import Database

class User:

    def __init__(self):
        self._logged_user = None
        self.db = Database()
        

    def login(self, username, password, mode):
        """Authenticate the user"""
        return True

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