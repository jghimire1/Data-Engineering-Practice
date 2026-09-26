from pyspark.sql import SparkSession
#from pyspark.sql.types import StructType,StructField, StringType, IntegerType

from enforce_schema import enforce_schema
from nested_schema import nested_schema


def number_rdd():
    global data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data)
    print(rdd.count())
    print(rdd.collect())



if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

#enforce_schema(spark)
nested_schema(spark)
