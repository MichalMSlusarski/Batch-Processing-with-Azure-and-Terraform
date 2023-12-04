import psycopg2

def parse_user_info(file_path):
    user_info = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            user_info[key] = value
    return user_info

def insert_user_info(user_info, db_config):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    columns = ', '.join(user_info.keys())
    values = ', '.join(['%s'] * len(user_info))
    query = f"INSERT INTO Users ({columns}) VALUES ({values})"

    cursor.execute(query, list(user_info.values()))
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    # Read settings from settings file
    user_info = parse_user_info('user.txt')
    insert_user_info(user_info)