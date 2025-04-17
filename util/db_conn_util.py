import pyodbc

def get_connection():
    
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-6PSEMB9\\NANDHIHA;"
        "Database=ordermanagementsystem;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)