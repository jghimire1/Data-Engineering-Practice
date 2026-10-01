from pyspark.sql import SparkSession

from func4_maptype import map_type_method
from func4_pyspark_arraytype import arraytype_column
from func4_pyspark_partition import spark_partition

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    #spark_partition(spark)
    #arraytype_column(spark)
    map_type_method()
