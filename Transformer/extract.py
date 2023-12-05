import json
import os

def generate_insert_from_json(json_file, table_name):
    with open(json_file, 'r') as file:
        data = json.load(file)

    columns = []
    values = []

    def format_value(value):
        if isinstance(value, bool):
            return int(value)
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return value

    for key, value in data.items():
        columns.append(key)
        values.append(format_value(value))

    sql_insert = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(str(v) for v in values)})"
    return sql_insert

# Directory containing JSON files
directory = 'path_to_directory_containing_json_files'

# Table name for SQL insert statement
table_name = 'YourTableName'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        sql_insert = generate_insert_from_json(file_path, table_name)
        print(sql_insert)  # Perform database operation here with sql_insert

