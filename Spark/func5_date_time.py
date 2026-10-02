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


    # datediff() function
    df.select(col("input"),
              datediff(current_date(), col("input")).alias("datediff")
              ).show()

    # months_between()
    df.select(col("input"),
              months_between(current_date(), col("input")).alias("months_between")
              ).show()

    #add_months(), date_add(), date_sub()
    df.select(col("input"),
              add_months(col("input"), 3).alias("add_months"),
            add_months(col("input"), -3).alias("sub_months"),
            date_add(col("input"), 4).alias("date_add"),
            date_sub(col("input"), 4).alias("date_sub")
            ).show()

    #year(), month(), month(), next_day(), weekofyear()
    df.select(col("input"),
              year(col("input")).alias("year"),
              month(col("input")).alias("month"),
              next_day(col("input"), "Sunday").alias("next_day"),
              weekofyear(col("input")).alias("weekofyear")
              ).show()

    # dayofweek(), dayofmonth(), dayofyear()
    df.select(col("input"),
              dayofweek(current_date()).alias("dayofweek"),
              dayofmonth(current_date()).alias("dayofmonth"),
              dayofyear(current_date()).alias("dayofyear"),
              ).show()

