from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, dense_rank, lag, lead
from pyspark.sql.functions import rank


def windowFunction(spark):
    global columns
    simpleData = (("James", "Sales", 3000), \
                  ("Michael", "Sales", 4600), \
                  ("Robert", "Sales", 4100), \
                  ("Maria", "Finance", 3000), \
                  ("James", "Sales", 3000), \
                  ("Scott", "Finance", 3300), \
                  ("Jen", "Finance", 3900), \
                  ("Jeff", "Marketing", 3000), \
                  ("Kumar", "Marketing", 2000), \
                  ("Saif", "Sales", 4100))

    columns = ["employee_name", "department", "salary"]
    df = spark.createDataFrame(data=simpleData, schema=columns)
    df.printSchema()
    df.show(truncate=False)

    # row_number() window function
    windowSpec = Window.partitionBy("department").orderBy("salary")
    print("...output using row_number() window function...")
    df.withColumn("row_number",row_number().over(windowSpec)) \
        .show(truncate = False)

    # rank() window function
    print("Adding rank column using rank() function. ")
    df.withColumn("rank", rank().over(windowSpec))\
            .show(truncate = False)

    # dense_rank() window function
    print("Adding rank column with the dense_rank() function. ")
    df.withColumn("dense_rank", dense_rank().over(windowSpec)) \
            .show(truncate = False)

    # lag() window function
    print("Output using the lag() function.-----------")
    df.withColumn("lag", lag("salary",2).over(windowSpec)) \
        .show(truncate = False)

    print("lag by one position------------")
    df.withColumn("lag", lag("salary", 1).over(windowSpec)) \
        .show(truncate=False)

    # lead() window function
    print("output using the lead window function............")
    df.withColumn("lead", lead("salary",2).over(windowSpec)) \
            .show(truncate = False)

    print("lead by one position------------")
    df.withColumn("lead", lead("salary", 1).over(windowSpec)) \
        .show(truncate=False)








