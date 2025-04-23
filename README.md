# 💰 Bitcoin Data Pipeline: ETL and Real-Time Dashboard with Python

## 📌 Introduction
This project aims to build an ETL pipeline (Extract, Transform, Load) that consumes data from the **Coinbase API**, processes this information, and stores it in a **PostgreSQL** database hosted on **Render**. The collected data is used to power a **real-time dashboard** developed with **Streamlit**.

## 🎯 Project Overview

### Main Objectives
- Develop an automated ETL pipeline to capture the **Bitcoin price** in real-time from the **Coinbase public API**.
- Process and store the data in a **PostgreSQL** database hosted on **Render**.
- Create an **interactive real-time dashboard** using **Streamlit**.
- Implement **advanced observability and structured logging** using **Pydantic Logfire**.

## 🏗️ Project Stages
### 1. Extraction (E):
- Use the **Coinbase API** to obtain the current Bitcoin price.
- Consume public endpoints without authentication requirements.

### 2. Transformation (T):
- Select relevant information: **Bitcoin price, query timestamp, and reference currency (USD)**.
- Organize the data in tabular format using **Pandas**.

### 3. Load (L):
- Store the collected data in a **PostgreSQL** database hosted on **Render**.

### 4. Automation:
- Schedule data collection every **15 minutes**, ensuring continuous dashboard updates.

## 🚀 Technologies Used
### 🔹 Programming Language:
- **Python 3.10+**

### 🔹 Key Libraries:
- **requests** - For making HTTP requests to the Coinbase API.
- **pandas** - For data manipulation and transformation.
- **Streamlit** - For building the interactive real-time dashboard.
- **Logfire** - For monitoring and logging the pipeline.
- **SQLAlchemy** - For interacting with the PostgreSQL database.

## 📊 Interactive Dashboard (Real-Time)
- The **dashboard** was developed with **Streamlit** and displays Bitcoin price trends in real-time.
- The dashboard can be accessed via the link:
  🔗 [Access Dashboard](https://etlprojectapiextract-dashboard.onrender.com/)
- Data is collected in **streaming mode**, meaning every 15 minutes, ensuring constant updates and near real-time visualization.

## ☁️ Hosting on Render
**Render** is a cloud computing platform that simplifies the deployment of containers and databases. In this project, we use Render to host our **PostgreSQL** database.
- To create a database server on Render, visit:
  🔗 [https://render.com/](https://render.com/)

## 🔍 Monitoring with Logfire
- **Logfire** allows monitoring logs and gaining insights into the pipeline's performance.
- More information: [https://pydantic.dev/logfire](https://pydantic.dev/logfire)

## 🛠️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/data-pipeline-bitcoin.git
cd data-pipeline-bitcoin
```

### 2️⃣ Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### 3️⃣ Run the ETL Pipeline
```bash
python pipeline.py
```

### 4️⃣ Run the Dashboard (Optional)
```bash
streamlit run dashboard.py
```


---
🚀 **This project enables the extraction, transformation, and storage of Bitcoin price data, providing a dynamic real-time visualization!**

If you have any questions or suggestions, feel free to contribute! 💡

