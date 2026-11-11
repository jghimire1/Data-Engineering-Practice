from pyspark.sql.functions import *


# file moving from local D drive to project folder
# docker cp "D:\DataEngineeingBootCamp\Week 8 -9\Spark class project 5 - doc and data-20261013T021358Z-1-001\Spark class project 5 - doc and data\books.json"
# 785a21f825bd5091eb659f38fecb6e22a0fc0e19d51e54673fcc20722ee62bd1:home/takeo/pycharmproject/spark_class_project5_books_data_analysis

def books(spark):

    # creating dataframe from reading file
    df = spark.read.json('file:/home/takeo/pycharmprojects/spark_class_project5_books_data_analysis/books.json')
    df.printSchema()
    df.show(10)

    # counting the number of rows in dataframe
    print("Number of rows in data frame: "+str(df.count()))

# counting the number of distinct rows in data frame
    distinctDF = df.distinct()
    print("Distinct row count: "+str(distinctDF.count()))

    # Removing duplicates
    df2 = df.dropDuplicates()
    print("Distinct count of the rows after removing duplicates: "+str(df2.count()))
    df2.show(10,truncate = False)

 # Select title and assign 0 or 1 depending on title when title is not odd "ODD HOURS" and assign this value to
    # a column named as newHours
    df3 = df2.select("title", when(col("title") != 'ODD HOURS',1).otherwise(0).alias("newHours"))
    print("Assigning 1 when ODD hours is not equal to 1 and otherwise 0 and column naming as newHours: ")
    df3.show(10, truncate = False)
