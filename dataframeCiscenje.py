import pandas as pd


##TCX
df = pd.read_csv('CSV-ji/TCX/sportnikiTCX.csv')

df = df.drop(df.columns[0], axis=1)

df.to_csv('CSV-ji/TCX/sportnikiTCX.csv', index=False)

print(df)

df = df[df['tipAktivnosti'] == 'biking']
df['sportnik'].replace(to_replace=0, value=1, inplace=True)
df.to_csv('CSV-ji/TCX/bikingTCX.csv', index=False)


##GPX

df = pd.read_csv('CSV-ji/GPX/datotekeGPX.csv')

df = df[(df['tipAktivnosti'] == 'cycling') | (df['tipAktivnosti'] == 'road_biking')]
print(df)

df.to_csv('CSV-ji/GPX/bikingGPX.csv', index=False)


###Zdruzeno

df1 = pd.read_csv('CSV-ji/GPX/bikingGPX.csv')
df2 = pd.read_csv('CSV-ji/TCX/bikingTCX.csv')


# Convert 'id' to numeric and sort
merged_df = pd.concat([df1, df2]).sort_values(by='sportnik').reset_index(drop=True)

# Drop the last column
merged_df = merged_df.iloc[:, :-1]

merged_df.to_csv('CSV-ji/sportnikiJoined.csv', index=False)



print(merged_df)



