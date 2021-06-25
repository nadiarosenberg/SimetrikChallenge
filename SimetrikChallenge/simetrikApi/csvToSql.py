import pandas
import sqlalchemy
import pymysql

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
data = pandas.read_csv('../../fig4.csv')
database = data.to_sql('fig4',engine)
engine.dispose()