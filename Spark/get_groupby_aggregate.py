
from pyspark.sql.functions import sum, avg, max, min, mean, count, col


def groupby_aggregate_function(spark):
    simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
                  ("Michael", "Sales", "NY", 86000, 56, 20000),
                  ("Robert", "Sales", "CA", 81000, 30, 23000),
                  ("Maria", "Finance", "CA", 90000, 24, 23000),
                  ("Raman", "Finance", "CA", 99000, 40, 24000),
                  ("Scott", "Finance", "NY", 83000, 36, 19000),
                  ("Jen", "Finance", "NY", 79000, 53, 15000),
                  ("Jeff", "Marketing", "CA", 80000, 25, 18000),
                  ("Kumar", "Marketing", "NY", 91000, 50, 21000)
                  ]

    schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
    df = spark.createDataFrame(data=simpleData, schema=schema)
    df.printSchema()
    df.show(truncate=False)

    # using groupby() to group the department and getting the sum of salary
    print("Grouping by the department and calculating sum of the salary:")
    df.groupBy("department").sum("salary").show(truncate = False)

    # counting department
    print("Department count:")
    df.groupBy("department").count().show()

    # getting minimum salary by department
    print("Minimum salary by department:")
    df.groupBy("department").min("salary").show()

    # getting maximum salary by department
    print("Maximum salary by department:")
    df.groupBy("department").max("salary").show()

    # getting average salary by department
    print("Average salary by department:")
    df.groupBy("department").avg("salary").show()

    # getting mean salary by department
    print("Mean salary by department:")
    df.groupBy("department").mean("salary").show()


    # Grouping on multiple columns
    print("Grouping by department and state and getting sum of salary and sum of bonus:")
    df.groupBy("department", "state") \
    .sum("salary", "bonus") \
    .show()

    # Aggregate function
    print("calculating more than one aggregation at a time with department, salary, bonus:")
    df.groupBy("department")\
        .agg(sum("salary").alias ("sum_salary"), \
            avg("salary").alias("average_salary"), \
            sum("bonus").alias("sum_bonus"), \
            max("bonus").alias("max_bonus") \
        )\
        .show(truncate = False)

    # Filter on aggregate data
    print("Filtering on aggregate data:")
    df.groupBy("department") \
        .agg(sum("salary").alias("sum_salary"), \
             avg("salary").alias("avg_salary"), \
             sum("bonus").alias("sum_bonus"), \
             max("bonus").alias("max_bonus"),
             ) \
        .where(col("sum_bonus") >= 50000) \
        .show(truncate=False)
