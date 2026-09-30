from pyspark.sql.functions import col, lit


def car_power_method(spark):
    car = [("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150,3761,"US"),
        ("BMW 2002", 113, 2234, "Europe")
           ]
    columns = ["carr", "horsepower", "weight", "origin"]

    df = spark.createDataFrame(data= car, schema= columns)
    df.show(truncate = False)

    # modifying the default long data type to integer
    print("Modifying the horsepower and weight columns' data type.")
    df1 = df.withColumn("horsepower", col("horsepower").cast("integer"))
    df2 = df1.withColumn("weight", col("weight").cast("integer"))

    df2.show()
    df2.printSchema()

    # adding AvgWeight column
    df3 = df2.withColumn("AvgWeight", lit("200"))
    df3.show(truncate = False)

    # Adding kilowatt_power column
    df4 = df3.withColumn("kilowatt_power", col("horsepower")*1000)
    df4.show(truncate = False)
    # renaming the column
    df5 = df4.withColumnRenamed("carr", "car")
    df5.show(truncate = False)

    #checking data type of the final data frame
    df5.printSchema()
