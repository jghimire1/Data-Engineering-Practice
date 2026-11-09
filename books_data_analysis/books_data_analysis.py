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

