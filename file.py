import requests
import pandas as pd
import sqlalchemy as db



url = 'https://statsapi.mlb.com/api/v1/schedule'

params = {
  'sportId': 1,
  'date': '06/17/2026'
}

resp = requests.get(url, params=params)

data = resp.json()


games = data['dates'][0]['games']

mlbdata = pd.DataFrame.from_dict(games)

engine = db.create_engine('sqlite:///data_base_name.db')
mlbdata.to_sql('mlb_table', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))