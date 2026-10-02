from pyspark.sql.functions import current_timestamp, col, to_timestamp, hour, minute, second


def current_timestamp_method(spark):
    data = [["1", "02-01-2020 11 01 19 06"], ["2", "03-01-2019 12 01 19 406"], ["3", "03-01-2021 12 01 19 406"]]
    df2 = spark.createDataFrame(data, ["id", "input"])
    df2.show(truncate=False)
    # current_timestamp()
    df2.select(current_timestamp().alias("current_timestamp")
               ).show(1, truncate=False)

    # converting string timestamp to timestamp format type using to_timestamp()
    # to_timestamp()
    df2.select(col("input"),
               to_timestamp(col("input"), "MM-dd-yyyy HH mm ss SSS").alias("to_timestamp")
               ).show(truncate=False)


    # hour(), Minute() and second()
    data = [["1", "2020-02-01 11:01:19.06"], ["2", "2019-03-01 12:01:19.406"], ["3", "2021-03-01 12:01:19.406"]]
    df3 = spark.createDataFrame(data, ["id", "input"])

    df3.select(col("input"),
               hour(col("input")).alias("hour"),
               minute(col("input")).alias("minute"),
               second(col("input")).alias("second")
               ).show(truncate=False)
