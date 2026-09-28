from pyspark.sql import SparkSession

from filter_function import filter_method
from select_function import select_single_multiple_col
from with_column_function import with_column

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    #select_single_multiple_col(spark)
    #with_column(spark)
    filter_method(spark)


