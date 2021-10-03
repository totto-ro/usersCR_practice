from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__(self, user_id, first_name, last_name, email, created_at):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "users_db" ).query_db( query )
        return results

    @classmethod
    def add_data( cls, data ):
        query = "INSERT INTO users(first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return result 
