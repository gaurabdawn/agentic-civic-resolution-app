from datetime import datetime
from pyspark.sql import Row

class SessionMemoryManager:

    def __init__(self, spark, config):

        self.spark = spark
        self.config = config

        self.catalog = config["catalog"]
        self.schema = config["schema"]

    def get_table_name(self):

        return f"""
        {self.catalog}.
        {self.schema}.
        {self.config["tables"]["session_memory"]}
        """.replace("\n", "").replace(" ", "")

    def store_memory(
        self,
        session_id,
        user_id,
        message,
        role
    ):

        data = [
            Row(
                session_id=session_id,
                user_id=user_id,
                message=message,
                role=role,
                timestamp=datetime.now()
            )
        ]

        df = self.spark.createDataFrame(data)

        df.write \
            .format("delta") \
            .mode("append") \
            .saveAsTable(self.get_table_name())

    def retrieve_memory(self, user_id):

        query = f"""
        SELECT *
        FROM {self.get_table_name()}
        WHERE user_id = '{user_id}'
        ORDER BY timestamp DESC
        """

        return self.spark.sql(query)