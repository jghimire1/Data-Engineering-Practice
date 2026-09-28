
def filter_method(spark):
    data = [
        (("James", "", "Smith"), ["Java", "Scala", "C++"], "OH", "M"),
        (("Anna", "Rose", ""), ["Spark", "Java", "C++"], "NY", "F"),
        (("Julia", "", "Williams"), ["CSharp", "VB"], "OH", "F"),
        (("Maria", "Anne", "Jones"), ["CSharp", "VB"], "NY", "M"),
        (("Jen", "Mary", "Brown"), ["CSharp", "VB"], "NY", "M"),
        (("Mike", "Mary", "Williams"), ["Python", "VB"], "OH", "M")
    ]

    schema = StructType([
        StructField('name', StructType([
            StructField('firstname', StringType(), True),
            StructField('middlename', StringType(), True),
            StructField('lastname', StringType(), True)
        ])),
        StructField('languages', ArrayType(StringType()), True),
        StructField('state', StringType(), True),
        StructField('gender', StringType(), True)
    ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show(truncate=False)

 # filtering based on the variable
    df.filter(df.state == "OH").show(truncate=False)

    # not equals condition
    df.filter(df.state != "OH") \
        .show(truncate=False)

    df.filter(~(df.state == "OH")) \
        .show(truncate=False)

    # Using SQL col() function
    from pyspark.sql.functions import col

    # filtering based on the NY using col()
    print("Filtering using col() function.")
    df.filter(col("state") == "NY") \
        .show(truncate=False)

    # filtering using filter() with SQL Expression
    print(" Filtering using filter() function with SQL Expression:")
    # Using SQL Expression
    df.filter("gender == 'M'").show()

    # For not equal
    df.filter("gender != 'M'").show()

    df.filter("gender <> 'M'").show()

    # Filter with multiple conditions
    print("Filtering using multiple condition")
    df.filter((df.state== 'OH')& (df.gender == "M")) \
        .show(truncate = False)

    # Filter based on the list values
    print("Filter based on the list elements:")
    lst = ["OH","CA","DE"]
    df.filter(df.state.isin(lst)).show()

 # Filter NOT IS IN list Values
    # These show all records with NY (NY is not part of the list)
    print("Filtering using NOT IS IN list values")
    df.filter(~df.state.isin(lst)).show()
    df.filter(df.state.isin(lst) == False).show()

    # Filter based on Starts With, Ends With, Contains
    print("Using starts with filtering")
    df.filter(df.state.startswith("N")).show()

    print("Using endswith filtering")
    df.filter(df.state.endswith("H")).show()

    print("Using Contains filtering")
    df.filter(df.state.contains("H")).show()

   

   
