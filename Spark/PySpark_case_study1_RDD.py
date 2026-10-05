# Step 1 - Setting up PySpark
from pyspark.sql import SparkSession
# Create SparkSession
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .master("local[*]") \
    .getOrCreate()

# spark:SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com".getOrCreate()

# Get SparkContext from SparkSession
sc = spark.sparkContext

# Step 2 - Loading the data into an RDD
data = [
    "1,101,5001,Laptop,Electronics,1000.0,1",
    "2,102,5002,Headphones,Electronics,50.0,2",
    "3,101,5003,Book,Books,20.0,3",
    "4,103,5004,Laptop,Electronics,1000.0,1",
    "5,102,5005,Chair,Furniture,150.0,1"
]
transactions_rdd = sc.parallelize(data)

transactions_rdd.collect()
transactions_rdd.count()
