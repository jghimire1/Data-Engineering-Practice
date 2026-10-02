from pyspark.sql.functions import current_date, date_format, col, to_date, datediff, months_between, add_months, \
    date_add, date_sub, year, month, next_day, weekofyear, dayofweek, dayofmonth, dayofyear


def date_time_func(spark):
    # Create SparkSession
    data = [["1", "2020-02-01"], ["2", "2019-03-01"], ["3", "2021-03-01"]]
    df = spark.createDataFrame(data, ["id", "input"])
    df.show()

    # current date
    df.select(current_date().alias("current_date")).show(1)

    # date_format() function
    print("output using date_format()------")
    df.select(col("input"), date_format(col("input"),"MM-dd-yyyy").alias("date_format")).show()

    # to_date() function
    print("Output using to_date() function----")
    df.select(col("input"), to_date(col("input"), "yyyy-MM-dd").alias("to_date")).show()

    df.select(col("input"),to_date(col("input"), "yyyy-MM-dd").alias("to_date")
              ).printSchema()

    df.select(col("input"),to_date(col("input"), "yyyy-MM-dd.HH.mm.ss.SSS").alias("to_date")).show()

