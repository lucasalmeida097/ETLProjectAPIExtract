import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime
from dotenv import load_dotenv
import plotly.express as px
from sqlalchemy import create_engine

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL) 

def fetch_data(engine):
    try:
        query = "SELECT * FROM prices_bitcoin ORDER BY timestamp DESC"
        df = pd.read_sql(query, engine) 
        return df
    except Exception as e:
        st.error(f"Error fetching data from PostgreSQL: {e}")
        return pd.DataFrame()


def main():
    st.set_page_config(page_title="Bitcoin Price Dashboard", layout="wide")
    st.title("📊 Bitcoin Price Dashboard")

    placeholder = st.empty()

    while True:
        df = fetch_data(engine)

        if not df.empty:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values(by='timestamp') 

            with placeholder.container():
                st.subheader("📋 Recent Data")
                st.dataframe(df, use_container_width=True) 

                st.subheader("📈 Bitcoin Price Trend")
                fig = px.line(df, x='timestamp', y='price', title='Bitcoin Price Over Time', 
                              labels={'timestamp': 'Date', 'price': 'Price (USD)'}, 
                              template='plotly_dark')
                st.plotly_chart(fig, use_container_width=True)

                st.subheader("🔢 Key Statistics")
                col1, col2, col3 = st.columns(3)
                col1.metric("Current Price", f"${df['price'].iloc[-1]:,.2f}")
                col2.metric("Highest Price", f"${df['price'].max():,.2f}")
                col3.metric("Lowest Price", f"${df['price'].min():,.2f}")
                
                st.markdown(f"***Última Atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***")

        else:
            st.warning("No data found in the PostgreSQL database.")
            
        time.sleep(15)


if __name__ == "__main__":
    main()