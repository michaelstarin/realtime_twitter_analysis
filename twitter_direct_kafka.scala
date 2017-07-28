import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession
    
println("###########################################################################")

val spark = SparkSession.builder.appName("SentimentAnalysis").getOrCreate()

// Consume kafka topic
val rawTweets = spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers","localhost:9092")
  .option("subscribe","test")
  .load()
  
    
// Write new data to Parquet files
noAggDF
  .writeStream
  .format("json")
  .option("checkpointLocation", "/home/jovyan/work/spark-2.1.1-bin-hadoop2.7/twitter_parquet")
  .option("path", "/home/jovyan/work/spark-2.1.1-bin-hadoop2.7/twitter_parquet")
  .start()
    