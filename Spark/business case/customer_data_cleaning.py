from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

def customer_data(spark):
    global columns
    data = [
        ("Smith", 23, 5.3),
        ("Rashmi", 27, 5.8),
        ("Smith", 23, 5.3),
        ("Payal", 27, 5.8),
        ("Megha", 27, 5.4)
    ]

    columns = StructType([
        StructField('name', StringType(), True),
        StructField('age', IntegerType(), True),
        StructField('height', DoubleType(), True)])

    df = spark.createDataFrame(data=data, schema=columns)
    df.printSchema()
    df.show(truncate=False)
 # Removing duplicates rows
    distinct_df = df.distinct()
    print("Distinct row record of the data frame:")
    distinct_df.show(truncate = False)

    # removing duplicates based on the height and age columns
    print("Data after removing duplicates based on the age and height:")
    NoDupDF = df.dropDuplicates(["age", "height"])
    NoDupDF.show(truncate = False)
