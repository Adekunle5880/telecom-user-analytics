import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:Adekunle_5880@localhost:5432/telecom')

xdr_data = pd.read_sql_table('xdr_data', engine)

print(xdr_data.head())