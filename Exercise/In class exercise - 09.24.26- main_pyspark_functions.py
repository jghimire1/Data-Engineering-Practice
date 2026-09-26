
from pyspark.sql import SparkSession

from Get_Joins import join_function
from get_distinctRows import get_distinct_rows
from get_groupby_aggregate import groupby_aggregate_function
from get_order_sortBy import sort_orderBy_Function

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

#get_distinct_rows(spark)

#sort_orderBy_Function(spark)

# groupby_aggregate_function(spark)
join_function(spark)

 
