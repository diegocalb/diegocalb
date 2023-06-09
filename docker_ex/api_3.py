import os
import pyEX as p
import requests
import pandas as pd
from dateutil import parser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Credentials for postgres connections
dbname=os.environ.get("POSTGRES_DB"),
user=os.environ.get("POSTGRES_USER"),
password=os.environ.get("POSTGRES_PASS"),
host=os.environ.get("POSTGRES_HOST"),
port=os.environ.get("POSTGRES_PORT")

def stock_data_date_SQL(date = None):
    """
    Get the AAPL data and store it into a Postgres Table

    Parameters
    ----------
    date: string
        Date format of 'YYYY-MM-DD'
    
    """
    
    Atoken = os.environ.get("ATOKEN")
    p.Client(api_token=Atoken, version='stable')
    base_url = 'https://cloud.iexapis.com/v1'
    params = {'token': Atoken}
    new_date = None
    try:
        n_date = parser.parse(date)
        new_date = n_date.strftime('%Y%m%d')
    except:
        print ("Invalid date format. Expected: 'YYYY-MM-DD'")
        return
    endpoint = f'{base_url}/stock/AAPL/chart/date/{new_date}'    
    resp = requests.get(endpoint, params=params, timeout=20)
    resp.raise_for_status()
    df = pd.DataFrame(resp.json())
    engine = create_engine(f"postgresql://{user}:{password}@{host}/{dbname}")
    my_scoped_session = scoped_session(sessionmaker(bind=engine))
    db = my_scoped_session()
    db.execute("CREATE TABLE IF NOT EXISTS public.table1")
    df.to_sql('table1', engine)
    db.commit()
    db.close()
    print("Done")

if __name__ == '__main__':
    if 'DATE' in os.environ:
        date = os.environ.get('DATE')
        stock_data_date_SQL(date)
    else:
        print("You must provide a date")