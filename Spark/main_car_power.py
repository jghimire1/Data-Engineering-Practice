from pyspark.sql import SparkSession

from car_power import car_power_method

if __name__ == "__main__":
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    car_power_method(spark)
