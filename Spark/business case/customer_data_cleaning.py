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
