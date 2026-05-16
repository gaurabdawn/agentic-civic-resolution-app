from pyspark.sql import SparkSession

def get_spark_session(app_name="LakebaseMemory"):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )

    return spark