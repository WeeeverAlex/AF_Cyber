from fastapi import FastAPI
from dotenv import load_dotenv
import pymysql
import os

# Carregar variáveis do .env
load_dotenv()

# Configurações do banco de dados
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.get("/data")
def get_data():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tabela_exemplo")
        result = cursor.fetchall()
        connection.close()
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}
