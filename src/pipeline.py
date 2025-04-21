import os
import time
import requests
import logging
import logfire
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, PriceBitcoin
from logging import basicConfig, getLogger

logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()

load_dotenv()
URL = os.getenv("URL")
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
    logger.info("Create table successfully!")

def extract_bitcoin_data():
    response = requests.get(URL)
    if response.status_code == 200:
       return response.json()
    else:
        logger.error(f"Request failed: {response.status_code}")
        return None

def transform_bitcoin_data(data):
    price = float(data["data"]["amount"])
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
    logger.info(f"[{data['timestamp']}] Data saved successfully.")


if __name__ == "__main__":
    crate_table()
    logger.info("Starting ETL with update every 15 seconds... (CTRL+C to stop)")

    while True:
        try:
            json_data = extract_bitcoin_data()
            if json_data:
                processed_data = transform_bitcoin_data(json_data)
                logger.info(f"Processed data: {processed_data}")
                save_data(processed_data)
            time.sleep(15)
        except KeyboardInterrupt:
            logger.info("Process interrupted by user. Ending...")
            break
        except Exception as e:
            logger.error(f"Error during execution: {e}")
            time.sleep(15)

