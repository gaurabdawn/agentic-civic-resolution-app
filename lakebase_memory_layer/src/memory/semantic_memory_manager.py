from pyspark.sql import Row
from datetime import datetime

class SemanticMemoryManager:

    def __init__(
        self,
        spark,
        config,
        embedder
    ):

        self.spark = spark
        self.config = config
        self.embedder = embedder

        self.catalog = config["catalog"]
        self.schema = config["schema"]

    def get_table_name(self):

        return f"""
        {self.catalog}.
        {self.schema}.
        {self.config["tables"]["semantic_memory"]}
        """.replace("\n", "").replace(" ", "")

    def store_memory(
        self,
        doc_id,
        content,
        metadata=None
    ):

        embedding = self.embedder.generate_embedding(
            content
        )

        data = [
            Row(
                doc_id=doc_id,
                content=content,
                embedding=embedding,
                created_at=datetime.now(),
                metadata=metadata
            )
        ]

        df = self.spark.createDataFrame(data)

        df.write \
            .format("delta") \
            .mode("append") \
            .saveAsTable(self.get_table_name())