from pyspark.sql import SparkSession

from func3_map import mapped
from func_union import union

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    # union(spark)
    mapped(spark)

