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


    # 2. Handle Null values - Replace null values in the rating column with the average ratings.
    average_rating = df.selectExpr('avg(rating)').collect()[0][0]
    df_filled = df.na.fill({'rating': average_rating})
    print("Data frame with replacing null values with he average ratings. ")
    df_filled.show()

    # 3. Drop Duplicates - Remove duplicate ratings by 'user_id' and 'movie_id'
    df_no_duplicates = df_filled.dropDuplicates(['user_id', 'movie_id'])
    print("Removing duplicates on df_filled--------")
    df_no_duplicates.show()

    # 4. Select Specific Columns - Select 'user_id' and 'ratings' columns
    df_selected = df_filled.select('user_id', 'rating')
    print("Selecting only user_id and rating from df_filled dataframe")
    df_selected.show()

    # 5. Grouping and Aggregating - calculate the average rating per movie
    df_grouped = df_filled.groupBy('movie_id').agg({'rating': 'avg'})
    print("Grouping by Movie id and aggregating on average rating.")
    df_grouped.show()

    # 6. Joining DataFrames - Join the 'movie ratings' DataFrame wiht a 'movie_details' dataframe that contains '
    # movie id' and 'movie name'
    movie_data = [
        (101, 'The Thunder Bolt'),
        (102, 'The ransom crocodile'),
        (103, 'Lady with the Buggies')
        ]

    movie_columns = ["movie_id", 'movie_name']
    df_movies = spark.createDataFrame(movie_data,movie_columns)
    df_movies.show(truncate = False)

    # Joining data frame df and df_movies
    df_joined = df_filled.join(df_movies, on = 'movie_id', how = 'inner')
    print("Joined df and df_movies dataframe.....")
    df_joined.show(truncate = False)

    # 7. Union of DataFrames - Union this DataFrame with another df.new_ratings containing additional ratings data.
    rating_detail = [
        (7, 101, 3, 1622388140001),
        (5, 102, 4, 1622388140002),
        (6, 103, 5, 1622388140003)

    ]
