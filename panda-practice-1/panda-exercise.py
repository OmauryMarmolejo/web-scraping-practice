import pandas as pd

df_premier22 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

df_premier22.rename(columns={ 'Date': 'date',
                              'HomeTeam': 'home_team',
                              'AwayTeam': 'away_team',
                              'FTHG': 'home_goals',
                              'FTAG': 'away_goals',}, inplace=True)

print(df_premier22)