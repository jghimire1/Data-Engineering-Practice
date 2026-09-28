from pyspark.sql.functions import col, lit


def with_column(spark):
    global columns
    data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
            ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
            ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
            ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
            ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
            ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]

    df = spark.createDataFrame(data=data, schema=columns)

    df.show(truncate = False)

    # change datatype using pySpark with Column()
    print("Table updated with the data type for salary to double:")
    ddf = df.withColumn("salary", col("salary").cast("Double"))
    ddf.show(truncate = False)

    # update the value of the existing column
    print("updating the value of the salary column using withColumn function:")
    udf = df.withColumn("salary", col("salary")*100)
    udf.show(truncate = False)

    # create a column from an exiting column
    print("create a column from an existing column:")
    ncol = df.withColumn("copiedColumn", col("salary")-500)
    ncol.show(truncate = False)

    # Add a new column
    print("Adding new column using withColumn() with constant value.")
    ncol.withColumn("country", lit("USA")).show()

    # Rename a column name
    print("Renaming a column - Gender column to sex")
    ncol.withColumnRenamed("gender","sex") \
    .show(truncate = False)



