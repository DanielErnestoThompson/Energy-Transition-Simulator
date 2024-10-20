import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Establish MySQL connection
connection = create_connection("localhost", "root", "2268", "consulting_db")

# Test 1: Create Operation - Insert New Client
print("\nTest 1: Create New Client")
create_client_query = """
INSERT INTO Clients (client_name, industry, revenue_tier, region) 
VALUES ('Client C', 'Healthcare', 'Tier 1', 'Asia');
"""
execute_query(connection, create_client_query)

# Check if client was added
result = read_query(connection, "SELECT * FROM Clients WHERE client_name = 'Client C';")
if result:
    print("Test 1 Passed: New Client created successfully.")
else:
    print("Test 1 Failed: New Client was not created.")

# Test 2: Read Operation - Retrieve Clients
print("\nTest 2: Read All Clients")
clients = read_query(connection, "SELECT * FROM Clients;")
if clients:
    print("Test 2 Passed: Clients retrieved successfully.")
    for client in clients:
        print(client)
else:
    print("Test 2 Failed: Could not retrieve clients.")

# Test 3: Update Operation - Update Client Region
print("\nTest 3: Update Client Region")
update_client_query = """
UPDATE Clients SET region = 'Europe' WHERE client_name = 'Client C';
"""
execute_query(connection, update_client_query)

# Check if client region was updated
result = read_query(connection, "SELECT region FROM Clients WHERE client_name = 'Client C';")
if result and result[0][0] == 'Europe':
    print("Test 3 Passed: Client region updated successfully.")
else:
    print("Test 3 Failed: Client region was not updated.")

# Test 4: Delete Operation - Delete Client
print("\nTest 4: Delete Client")
delete_client_query = "DELETE FROM Clients WHERE client_name = 'Client C';"
execute_query(connection, delete_client_query)

# Check if client was deleted
result = read_query(connection, "SELECT * FROM Clients WHERE client_name = 'Client C';")
if not result:
    print("Test 4 Passed: Client deleted successfully.")
else:
    print("Test 4 Failed: Client was not deleted.")

# Test 5: Create Operation - Insert New Consultant
print("\nTest 5: Create New Consultant")
create_consultant_query = """
INSERT INTO Consultants (consultant_name, expertise, utilization_rate) 
VALUES ('John Doe', 'Financial Strategy', 70.00);
"""
execute_query(connection, create_consultant_query)

# Check if consultant was added
result = read_query(connection, "SELECT * FROM Consultants WHERE consultant_name = 'John Doe';")
if result:
    print("Test 5 Passed: New Consultant created successfully.")
else:
    print("Test 5 Failed: New Consultant was not created.")

# Test 6: Update Operation - Update Consultant Utilization Rate
print("\nTest 6: Update Consultant Utilization Rate")
update_consultant_query = """
UPDATE Consultants SET utilization_rate = 85.00 WHERE consultant_name = 'John Doe';
"""
execute_query(connection, update_consultant_query)

# Check if consultant utilization rate was updated
result = read_query(connection, "SELECT utilization_rate FROM Consultants WHERE consultant_name = 'John Doe';")
if result and result[0][0] == 85.00:
    print("Test 6 Passed: Consultant utilization rate updated successfully.")
else:
    print("Test 6 Failed: Consultant utilization rate was not updated.")

# Test 7: Delete Operation - Delete Consultant
print("\nTest 7: Delete Consultant")
delete_consultant_query = "DELETE FROM Consultants WHERE consultant_name = 'John Doe';"
execute_query(connection, delete_consultant_query)

# Check if consultant was deleted
result = read_query(connection, "SELECT * FROM Consultants WHERE consultant_name = 'John Doe';")
if not result:
    print("Test 7 Passed: Consultant deleted successfully.")
else:
    print("Test 7 Failed: Consultant was not deleted.")

# Add more tests for Engagements, Risk Assessment, etc.

# Test 8: Profitability Calculation
print("\nTest 8: Calculate Profitability")
profitability_query = """
SELECT client_name, SUM(profitability) AS total_profitability
FROM Engagements
INNER JOIN Clients ON Engagements.client_id = Clients.client_id
GROUP BY client_name;
"""
profitability = read_query(connection, profitability_query)
if profitability:
    print("Test 8 Passed: Profitability calculation completed.")
    for record in profitability:
        print(record)
else:
    print("Test 8 Failed: Profitability calculation did not complete.")
