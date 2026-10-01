
def spark_partition(spark):
    df = spark.read.option("header", True) \
        .csv("file:///home/takeo/pycharmprojects/simple-zipcodes.csv")
    df.printSchema()
    df.show()

    # partition by
    df.write.option("header", True) \
        .partitionBy("state") \
        .mode("overwrite") \
        .csv("file:///tmp/parts/zipcodes-state")

    # partition by multiple columns
    df.write.option("header", True) \
        .partitionBy("state", "city") \
        .mode("overwrite") \
        .csv("file:///tmp/parts/zipcodes-city-state")

 
    

