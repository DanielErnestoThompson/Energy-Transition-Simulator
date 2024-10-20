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

# Create Services table first, since it's referenced by Engagements
create_services_table = """
CREATE TABLE IF NOT EXISTS Services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    cost DECIMAL(10,2)
);
"""
execute_query(connection, create_services_table)

# Create Clients table
create_clients_table = """
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    revenue_tier VARCHAR(50),
    region VARCHAR(255)
);
"""
execute_query(connection, create_clients_table)

# Create Consultants table
create_consultants_table = """
CREATE TABLE IF NOT EXISTS Consultants (
    consultant_id INT AUTO_INCREMENT PRIMARY KEY,
    consultant_name VARCHAR(255) NOT NULL,
    expertise VARCHAR(255),
    availability BOOLEAN DEFAULT TRUE,
    utilization_rate DECIMAL(5,2)
);
"""
execute_query(connection, create_consultants_table)

# Create Engagements table after the necessary tables are created
create_engagements_table = """
CREATE TABLE IF NOT EXISTS Engagements (
    engagement_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    consultant_id INT,
    service_id INT,
    start_date DATE,
    end_date DATE,
    profitability DECIMAL(10,2),
    status VARCHAR(50),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (consultant_id) REFERENCES Consultants(consultant_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);
"""
execute_query(connection, create_engagements_table)

# Create Performance Metrics table
create_performance_metrics_table = """
CREATE TABLE IF NOT EXISTS Performance_Metrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    engagement_id INT,
    kpi_name VARCHAR(255),
    kpi_value DECIMAL(10,2),
    FOREIGN KEY (engagement_id) REFERENCES Engagements(engagement_id)
);
"""
execute_query(connection, create_performance_metrics_table)

# Create Risk Assessment table
create_risk_assessment_table = """
CREATE TABLE IF NOT EXISTS Risk_Assessment (
    risk_id INT AUTO_INCREMENT PRIMARY KEY,
    engagement_id INT,
    risk_description TEXT,
    mitigation_strategy TEXT,
    risk_level VARCHAR(50),
    FOREIGN KEY (engagement_id) REFERENCES Engagements(engagement_id)
);
"""
execute_query(connection, create_risk_assessment_table)

# Insert initial data
insert_clients = """
INSERT INTO Clients (client_name, industry, revenue_tier, region) VALUES
('Client A', 'Finance', 'Tier 1', 'North America'),
('Client B', 'Retail', 'Tier 2', 'Europe');
"""
insert_consultants = """
INSERT INTO Consultants (consultant_name, expertise, utilization_rate) VALUES
('Alice Smith', 'Digital Transformation', 75.50),
('Bob Johnson', 'Market Strategy', 80.00);
"""
insert_services = """
INSERT INTO Services (service_name, cost) VALUES
('Market Analysis', 5000.00),
('Business Strategy', 10000.00);
"""
execute_query(connection, insert_clients)
execute_query(connection, insert_consultants)
execute_query(connection, insert_services)

### CRUD OPERATIONS ###

# Create Operation (Insert New Engagement)
def create_engagement(client_id, consultant_id, service_id, start_date, end_date, profitability, status):
    query = f"""
    INSERT INTO Engagements (client_id, consultant_id, service_id, start_date, end_date, profitability, status) 
    VALUES ({client_id}, {consultant_id}, {service_id}, '{start_date}', '{end_date}', {profitability}, '{status}');
    """
    execute_query(connection, query)

create_engagement(1, 1, 1, '2024-10-01', '2024-12-01', 15000.00, 'In Progress')

# Read Operation (Retrieve All Engagements)
def get_engagements():
    query = "SELECT * FROM Engagements;"
    engagements = read_query(connection, query)
    if engagements:
        for engagement in engagements:
            print(engagement)
    else:
        print("No engagements found or table does not exist.")

get_engagements()

# Update Operation (Update Engagement Status)
def update_engagement_status(engagement_id, new_status):
    query = f"""
    UPDATE Engagements 
    SET status = '{new_status}' 
    WHERE engagement_id = {engagement_id};
    """
    execute_query(connection, query)

update_engagement_status(1, 'Completed')

# Delete Operation (Delete Engagement)
def delete_engagement(engagement_id):
    query = f"DELETE FROM Engagements WHERE engagement_id = {engagement_id};"
    execute_query(connection, query)

delete_engagement(1)

# Read Operation (Retrieve All Consultants)
def get_consultants():
    query = "SELECT * FROM Consultants;"
    consultants = read_query(connection, query)
    if consultants:
        for consultant in consultants:
            print(consultant)
    else:
        print("No consultants found or table does not exist.")

get_consultants()

# Update Operation (Update Consultant Utilization Rate)
def update_consultant_utilization(consultant_id, new_utilization_rate):
    query = f"""
    UPDATE Consultants 
    SET utilization_rate = {new_utilization_rate} 
    WHERE consultant_id = {consultant_id};
    """
    execute_query(connection, query)

update_consultant_utilization(1, 85.00)

# Insert Operation (Insert New Risk Assessment)
def create_risk_assessment(engagement_id, risk_description, mitigation_strategy, risk_level):
    query = f"""
    INSERT INTO Risk_Assessment (engagement_id, risk_description, mitigation_strategy, risk_level) 
    VALUES ({engagement_id}, '{risk_description}', '{mitigation_strategy}', '{risk_level}');
    """
    execute_query(connection, query)

create_risk_assessment(1, 'High budget overrun risk', 'Adjust consultant allocation', 'High')

# Update Operation (Update Risk Level)
def update_risk_level(risk_id, new_risk_level):
    query = f"""
    UPDATE Risk_Assessment 
    SET risk_level = '{new_risk_level}' 
    WHERE risk_id = {risk_id};
    """
    execute_query(connection, query)

update_risk_level(1, 'Medium')

# Delete Operation (Delete Risk Assessment)
def delete_risk_assessment(risk_id):
    query = f"DELETE FROM Risk_Assessment WHERE risk_id = {risk_id};"
    execute_query(connection, query)

delete_risk_assessment(1)

# SQL Test for Profitability Calculation
def calculate_profitability():
    query = """
    SELECT client_name, SUM(profitability) AS total_profitability
    FROM Engagements
    INNER JOIN Clients ON Engagements.client_id = Clients.client_id
    GROUP BY client_name;
    """
    profitability = read_query(connection, query)
    if profitability:
        for record in profitability:
            print(record)
    else:
        print("No profitability data found.")

calculate_profitability()
