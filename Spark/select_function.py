import pyspark
from pyspark.sql.functions import col
from pyspark.sql import SparkSession


def select_single_multiple_col(spark):
    data = [("James", "Smith", "USA", "CA"),
            ("Michael", "Rose", "USA", "NY"),
            ("Robert", "Williams", "USA", "CA"),
            ("Maria", "Jones", "USA", "FL")
            ]
    columns = ["firstname", "lastname", "country", "state"]
    df = spark.createDataFrame(data=data, schema=columns)
    df.show(truncate=False)
    df.show()

    #select single & multiple columns
    df.select("firstname"). show()

    df.select(df["firstname"], df["lastname"]).show()

    # By using col() function
    print("Selecting firstname and lastname using col() function:")
    df.select(col("firstname"), col("lastname")).show()

    # selecting all
    print("Selecting all:")
    df.select("*").show()

    # Selects first 3 columns and top 3 rows
    print("first 3 columns and top 3 rows")
    df.select(df.columns[:3]).show(3)

    # Selects columns 2 to 4  and top 3 rows

    df.select(df.columns[2:4]).show(3)

