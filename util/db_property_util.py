def get_connection_string(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        conn_str = ""
        for line in lines:
            if not line.strip().startswith("#"):
                conn_str += line.strip()
        return conn_str
