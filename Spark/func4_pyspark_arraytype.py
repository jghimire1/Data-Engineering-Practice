from pyspark.sql.types import StringType, ArrayType,StructType,StructField
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import array
from pyspark.sql.functions import array_contains


# ArrayType Column Using StructType

def arraytype_column(spark):
    global schema
    data = [
        ("James,,Smith", ["Java", "Scala", "C++"], ["Spark", "Java"], "OH", "CA"),
        ("Michael,Rose,", ["Spark", "Java", "C++"], ["Spark", "Java"], "NY", "NJ"),
        ("Robert,,Williams", ["CSharp", "VB"], ["Spark", "Python"], "UT", "NV")
    ]

    schema = StructType([
        StructField("name", StringType(), True),
        StructField("languagesAtSchool", ArrayType(StringType()), True),
        StructField("languagesAtWork", ArrayType(StringType()), True),
        StructField("currentState", StringType(), True),
        StructField("previousState", StringType(), True)
    ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()

    # explode() function
    # function to create a new row for each element in the given array column
    print("dispersing languages at school using explode function ")
    df.select(df.name, explode(df.languagesAtSchool)).show()

    #Split() method - sql function returns an array type after splitting the string column by delimiter.
    print("using the splitting function --split()-- ")
    df.select(split(df.name,",").alias("nameAsArray")).show()

  











