from pyspark.sql.functions import col, avg


def movie_rating(spark):
    global columns
    data = [
        (1, 101, 4, 1622388000000),
        (1, 102, 3, 1622388020000),
        (2, 101, 5, 1622388040000),
        (2, 103, 4, 1622388060000),
        (3, 101, 3, 1622388080000),
        (3, 102, 4, 1622388100000),
        (3, 103, None, 1622388120000),
        (4, 101, 2, 1622388140000)
    ]

    # creating dataframe
    columns = ["user_id", "movie_id", "rating", "timestamp"]
    df = spark.createDataFrame(data, columns)
    df.show()

    # 1. Filter - Find all ratings that are greater than or equal to 4.
    df_filtered = df.filter(df.rating > 4)
    print("Filtered Movie ratings higher than 4")
    df_filtered.show()

