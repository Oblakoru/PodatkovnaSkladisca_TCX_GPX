import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table, DateTime, Time

df = pd.read_csv("CSV-ji/sportnikiJoinedDATE.csv")
df.fillna(0.0, inplace=True)


df['kadenceAvgAktivnosti'] = df['kadenceAvgAktivnosti'].astype(float)
df['sportnik'] = df['sportnik'].astype(str)
df['zacetekAktivnosti'] = pd.to_datetime(df['zacetekAktivnosti'], utc=True)


kilometrina = ["sportnik", "tipAktivnosti",  "zacetekAktivnosti", "trajanjeAktivnosti", "razdaljaAktivnosti"]
ostali = ["sportnik", "kalorijeAktivnosti", "vzponAktivnosti", "kadenceAvgAktivnosti" ]


df_kilometrina = df[kilometrina]
df_ostali = df[ostali]

povezava = ('mysql+mysqlconnector://root:root@localhost:3308/skladisca_kolesar')

engine = create_engine(povezava, echo=True)


metadata = MetaData()

# activities_table = Table(
#     'activities',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('sportnik', Integer),
#     Column('tipAktivnosti', String(length=50)),
#     Column('zacetekAktivnosti', DateTime),
#     Column('trajanjeAktivnosti', Float),
#     Column('razdaljaAktivnosti', Float),
# )
#
#
# activities_table = Table(
#     'other',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('sportnik', Integer),
#     Column('vzponAktivnosti', Float),
#     Column('kalorijeAktivnosti', Float),
#     Column('tempoAktivnosti', String(length=50)),
#     Column('kadenceAvgAktivnosti', Float),
#     Column('kadenceMaxAktivnosti', Float)
# )

metadata.create_all(engine)

df_kilometrina.to_sql('activities', engine, if_exists='replace', index=True)
df_ostali.to_sql('other', engine, if_exists='replace', index=True)


