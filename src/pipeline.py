import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, PriceBitcoin   

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def crate_table():
    Base.metadata.create_all(engine)

def extract_bitcoin_data():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    if response.status_code == 200:
       return response.json()
    else:
        print(f"Request failed: {response.status_code}")
        return None

def transform_bitcoin_data(data):
    price = data["data"]["amount"]
    cryptocurrency = data["data"]["base"]
    currency = data["data"]["currency"]
    timestamp = datetime.now()

    transformed_data = {
        "price": price,
        "cryptocurrency": cryptocurrency,
        "currency": currency,
        "timestamp" : timestamp
    }

    return transformed_data

def save_data(data):
    session = Session()
    new_register = PriceBitcoin(**data)
    session.add(new_register)
    session.commit()
    session.close()
    print(f"[{data['timestamp']}] Data saved successfully.")


if __name__ == "__main__":
    crate_table()
    print("Starting ETL with update every 15 seconds... (CTRL+C to stop)")

    while True:
        try:
            json_data = extract_bitcoin_data()
            if json_data:
                processed_data = transform_bitcoin_data(json_data)
                print("Processed data:",processed_data)
                save_data(processed_data)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Ending...")
            break
        except Exception as e:
            print(f"Error during execution: {e}")
            time.sleep(15)

