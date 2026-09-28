
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


   
