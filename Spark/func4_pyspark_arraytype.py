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

  # array()
    # Use array() function to create a new array column by merging the data from
    # multiple columns. All input columns must have the same data type. The below
    # example combines the data from currentState and previousState and creates a new column states.
    print("Array combined the data from current state and previous state and creating the states column.")
    df.select(df.name, array(df.currentState, df.previousState).alias("States")).show()

    # array_contains()
    # array_contains() sql function is used to check if array column contains a value.
    # Returns null if the array is null, true if the array contains the value, and false otherwise.
    print("Printing data using array_contains---")
    df.select(df.name, array_contains(df.languagesAtSchool, "Java").alias("array_contains")).show()
  











