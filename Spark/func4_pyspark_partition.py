
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

    # Use repartition() and partitionBy() together
    df.repartition(2).write.option("header",True).partitionBy("state").mode("overwrite").csv("file///tmp/parts/zipcodes-state-more")

    # partitionBy() control number of partitions
    df.write.option("header", True) \
        .option("maxRecordsPerFile", 2) \
        .mode("overwrite")\
        .csv("file:///tmp/parts/multi-zipcodes-state")

    # read a specific partition
    dfSinglePart = spark.read.option("header",True) \
            .csv("file:////tmp/parts/zipcodes-city-state/state=AL/city=SPRINGVILLE")
    dfSinglePart.printSchema()
    print("Reading a specific partition state - AL, city - SPRINGVILLE*****")
    dfSinglePart.show()

    #PySpark SQL - read partition data
    parqDF = spark.read.option("header", True)\
        .csv("file:////tmp/parts/zipcodes-city-state/")
    parqDF.createOrReplaceTempView("ZIPCODE")
    print("Selecting state - AL and city - springville from the temporary view zipcode--")
    spark.sql("select * from ZIPCODE where state = 'AL' and city = 'SPRINGVILLE'")\
    .show()

    

