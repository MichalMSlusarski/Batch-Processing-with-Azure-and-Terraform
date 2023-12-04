import pyodbc

def insert_user_info(user_info, db_config):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_config['server'] + ';DATABASE=' + db_config['database'] + ';UID=' + db_config['username'] + ';PWD=' + db_config['password'])
    cursor = conn.cursor()

    columns = ', '.join(user_info.keys())
    placeholders = ', '.join('?' * len(user_info))
    query = f"INSERT INTO Users ({columns}) VALUES ({placeholders})"

    cursor.execute(query, list(user_info.values()))
    conn.commit()

    cursor.close()
    conn.close()

# Usage:
user_info = parse_user_info('user.txt')
db_config = {
    'server': 'your_server.database.windows.net',
    'database': 'your_database',
    'username': 'your_username',
    'password': 'your_password'
}
insert_user_info(user_info, db_config)