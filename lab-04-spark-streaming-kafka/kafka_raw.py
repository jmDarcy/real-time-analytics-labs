from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import from_json, col, to_timestamp
 
SCHEMA = StructType([
    StructField("tx_id",     StringType()),
    StructField("user_id",   StringType()),
    StructField("amount",    DoubleType()),
    StructField("store",     StringType()),
    StructField("category",  StringType()),
    StructField("timestamp", StringType()),
])
 
 
spark = (
    SparkSession.builder
    .appName("Lab4-Kafka")
    .getOrCreate()
)
 
spark.sparkContext.setLogLevel("WARN")
 
kafka_raw = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "broker:9092")
    .option("subscribe", "transactions")
    .load()
)
 
df = kafka_raw.select(
    from_json(col("value").cast("string"), SCHEMA).alias("tx")
)
 
df2 = (df.select("tx.*")
    .withColumn("timestamp", to_timestamp("timestamp", "yyyy-MM-dd HH:mm:ss"))
      )
q = (
    df2.writeStream
    .format("console") 
    .outputMode("append") 
    .option("truncate", False)
    .start()
)
 
q.awaitTermination()
