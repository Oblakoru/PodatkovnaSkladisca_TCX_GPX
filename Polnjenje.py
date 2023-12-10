import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table, DateTime, Time

df = pd.read_csv("CSV-ji/sportnikiJoinedDATE.csv")
df.fillna(0.0, inplace=True)


df['kadenceAvgAktivnosti'] = df['kadenceAvgAktivnosti'].astype(float)
df['sportnik'] = df['sportnik'].astype(str)
df['zacetekAktivnosti'] = pd.to_datetime(df['zacetekAktivnosti'], utc=True)

#df['zacetekAktivnosti'] = pd.to_datetime(df['zacetekAktivnosti'])

# Extracting only the date part and replacing the original column
#df['zacetekAktivnosti'] = df['zacetekAktivnosti'].dt.date

#df.to_csv("CSV-ji/sportnikiJoinedDATE.csv", index=False)


#kilometrina = ["tipAktivnosti",  "zacetekAktivnosti", "trajanjeAktivnosti", "razdaljaAktivnosti", "tempoAktivnosti" ]

kilometrina = ["sportnik", "tipAktivnosti",  "zacetekAktivnosti", "trajanjeAktivnosti", "razdaljaAktivnosti"]
ostali = ["sportnik", "kalorijeAktivnosti", "vzponAktivnosti", "kadenceAvgAktivnosti" ]


df_kilometrina = df[kilometrina]
df_ostali = df[ostali]

povezava = ('mysql+mysqlconnector://root:root@localhost:3308/skladisca_kolesar')

engine = create_engine(povezava, echo=True)




###########################
#Create a metadata object
metadata = MetaData()

# Define the table
activities_table = Table(
    'activities',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('sportnik', Integer),
    Column('tipAktivnosti', String(length=50)),
    Column('zacetekAktivnosti', DateTime),
    Column('trajanjeAktivnosti', Float),
    Column('razdaljaAktivnosti', Float),
)


activities_table = Table(
    'other',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('sportnik', Integer),
    Column('vzponAktivnosti', Float),
    Column('kalorijeAktivnosti', Float),
    Column('tempoAktivnosti', String(length=50)),
    Column('kadenceAvgAktivnosti', Float),
    Column('kadenceMaxAktivnosti', Float)
)

# Create the table in the database
metadata.create_all(engine)

# Convert 'tempoAktivnosti' column to timedelta
#df['tempoAktivnosti'] = pd.to_timedelta(df['tempoAktivnosti'])

# Push data into the database
df_kilometrina.to_sql('activities', engine, if_exists='replace', index=True)
df_ostali.to_sql('other', engine, if_exists='replace', index=True)


###################
#dtype_kilometrina = {'sportnik': 'VARCHAR(255)', 'tipAktibnosti': 'VARCHAR(255)', 'zacetekAktivnosti': 'DATE', 'trajanjeAktivnosti': 'DOUBLE', 'razdaljaAktivnosti': 'FLOAT'}

#df_kilometrina.to_sql('dim_kilometrina', con=engine, if_exists='replace', index=True, dtype=dtype_kilometrina)
#df_ostali.to_sql('dim_ostali', con=engine, if_exists='replace', index=True)

