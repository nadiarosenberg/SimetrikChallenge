import pandas
import sqlalchemy
import pymysql
 
# Create the engine to connect to the MySQL database
engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
 
# Read data from CSV and load into a dataframe object
data = pandas.read_csv('../../fig4.csv')
 
# Write data into the table in MySQL database
database = data.to_sql('fig4',engine)

