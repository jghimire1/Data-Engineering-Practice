from pyspark.sql import SparkSession

from func_5_current_timestamp import current_timestamp_method
from func_5_date_time import date_time_func
from func_5_windowfunction import windowFunction

if __name__== '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    #windowFunction(spark)
    #date_time_func(spark)
    current_timestamp_method(spark)


