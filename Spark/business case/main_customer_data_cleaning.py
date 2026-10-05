from pyspark.sql import SparkSession

from customer_data_cleaning import customer_data

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()


customer_data(spark)

