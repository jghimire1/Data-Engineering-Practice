from pyspark.sql.functions import *


# file moving from local D drive to project folder
# docker cp "D:\DataEngineeingBootCamp\Week 8 -9\Spark class project 5 - doc and data-20261013T021358Z-1-001\Spark class project 5 - doc and data\books.json"


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

 # Select author and title is TRUE if title has "THE" word in titles and assign this value to a column named as universal
    df4 = df2.select("author",
                     "title",
                     col("title").contains("THE").alias("universal")
                     )
    print("selecting author and title is true if title has word 'THE' in titles and assigning this value to a column named universal")
    df4.show(10, truncate = False)
 # Select substring of authro from 1 to 3 and alias as newTitle1
    df5 = df2.select(df.author.substr(1,3).alias("newTitle1"))
    print("Select substring of author from 1 to 3 and alias as newTitle1")
    df5.show(5)
