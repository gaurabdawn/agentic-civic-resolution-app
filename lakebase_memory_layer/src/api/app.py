# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/health")
# def health():

#     return {
#         "status": "running"
#     }

# @app.get("/memory/{user_id}")
# def get_memory(user_id: str):

#     return {
#         "user_id": user_id,
#         "message": "Memory endpoint working"
#     }

from src.utils.config import load_config
from src.utils.spark_session import get_spark_session

config = load_config()

spark = get_spark_session()

@app.get("/session-memory/{user_id}")

def get_session_memory(user_id: str):

    query = f"""
    SELECT *
    FROM workspace.memory.session_memory
    WHERE user_id = '{user_id}'
    """

    df = spark.sql(query)

    rows = df.collect()

    results = []

    for row in rows:

        results.append(row.asDict())

    return results