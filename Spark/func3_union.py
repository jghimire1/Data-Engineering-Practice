import pyspark


def union(spark):
    global columns
    simpleData = [("James", "Sales", "NY", 90000, 34, 10000), \
                  ("Michael", "Sales", "NY", 86000, 56, 20000), \
                  ("Robert", "Sales", "CA", 81000, 30, 23000), \
                  ("Maria", "Finance", "CA", 90000, 24, 23000) \
                  ]
    columns = ["employee_name", "department", "state", "salary", "age", "bonus"]
    df = spark.createDataFrame(data=simpleData, schema=columns)
    print("--------simple data ---------")
    df.printSchema()
    df.show(truncate=False)

    simpleData2 = [("James","Sales","NY",90000,34,10000), \
        ("Maria","Finance","CA",90000,24,23000), \
        ("Jen","Finance","NY",79000,53,15000), \
        ("Jeff","Marketing","CA",80000,25,18000), \
        ("Kumar","Marketing","NY",91000,50,21000) \
      ]

    columns2= ["employee_name","department","state","salary","age","bonus"]
    df2 = spark.createDataFrame(data = simpleData2, schema = columns2)
    df2.printSchema()
    print("---simple data2---------")
    df2.show(truncate=False)

    # Merging two or more DataFrames using union
    unionDF = df.union(df2)
    print("Union of simple data and simple data 2:")
    unionDF.show(truncate = False)


