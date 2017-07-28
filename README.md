# sudo docker run -it --rm -p 8889:8889 -p4040:4040 -v /Users/michaelstarin:/home/jovyan/work jupyter/all-spark-notebook
sudo docker run -it --rm -p 8889:8889 -p4040:4040 -v /Users/michaelstarin:/home/jovyan/work michaelstarin/custom-spark-notebook

docker build -t michaelstarin:/home/jovyan/work jupyter .
docker build -t michaelstarin:/home/jovyan/work michaelstarin/custom-spark-notebook


#To build container from docker file
 docker build -t michaelstarin/custom-spark-notebook .

#To run container 
sudo docker run -it --rm -p 8888:8888 -v /Users/michaelstarin:/home/jovyan/work michaelstarin/custom-spark-notebook

# Use Spark Structured Stream to consume kafka topic
./bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0 /home/jovyan/work/forex_direct_kafka.py localhost:9092 test

~/spark-2.1.0-bin-hadoop2.7/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-8_2.11:2.1.0 sink.py


df = spark.read.parquet('/home/jovyan/work/spark-2.1.1-bin-hadoop2.7/twitter_parquet')


# Start Zookeeper.
./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties

# Start Kafka, also in its own terminal.
./bin/kafka-server-start ./etc/kafka/server.properties

# Start the Schema Registry, also in its own terminal.
./bin/schema-registry-start ./etc/schema-registry/schema-registry.properties

# Start producer
python twitter_producer.py 

./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-8_2.11:2.1.0 sink.py

# Use Spark Structured Stream to consume kafka topic and append to local Parquet file sink
./bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.1.0 /home/jovyan/work/direct_kafka.py localhost:9092 test



# Scala
./bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.1.0 /home/jovyan/work/twitter_direct_kafka.scala localhost:9092 test

./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0  --packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.1.0 --class com.inndata.StructuredStreaming.Kafka --master local[*] /home/jovyan/work/twitter_direct_kafka.py localhost:9092 test

./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0 --class com.inndata.StructuredStreaming.Kafka --master local[*] /home/jovyan/work/twitter_direct_kafka.py localhost:9092 test

./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0 --class com.inndata.StructuredStreaming.Kafka --master local[*] /home/jovyan/work/twitter_direct_kafka.py localhost:9092 test



./bin/spark-submit --master local[4] /home/jovyan/work/myProject/target/scala-2.11/MyProject-assembly-0.1.jar
./bin/spark-submit --master local[4] /home/jovyan/work/sentimentAnalysis/target/scala-2.11/SentimentAnalysis-assembly-2.0.0.jar
