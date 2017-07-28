from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == '__main__':

    spark=SparkSession.builder.appName("PythonStreamingDirectKafka").getOrCreate()

    # Create DataFrame representing the stream of input from connection to localhost:9092
    streaming_df = spark \
    .readStream \
    .format("kafka") \
    .option("subscribe","test") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .load() 

  
    # Cast value column as string
    parsed_data = streaming_df \
        .selectExpr('cast(value as string) as tweets')
    
    schema1 = StructType() \
        .add('text', StringType()) \
           
    parsed_data = parsed_data \
        .select(from_json('tweets', schema1).alias('data')) \
        .select('data.*')
        
    print(parsed_data.printSchema()) 
    
    # Write to Parquet files 
    query = parsed_data \
        .writeStream \
        .format("json") \
        .option("checkpointLocation", "/home/jovyan/work/spark-2.1.1-bin-hadoop2.7/twitter_parquet") \
        .option("path", "/home/jovyan/work/spark-2.1.1-bin-hadoop2.7/twitter_parquet") \
        .start()

    # Print to console
    query = parsed_data \
        .writeStream \
        .format("console") \
        .start()
        #.outputMode("complete") \

    query.awaitTermination()