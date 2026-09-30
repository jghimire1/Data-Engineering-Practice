from pyspark.sql.functions import col, lit


def car_power_method(spark):
    car = [("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150,3761,"US"),
        ("BMW 2002", 113, 2234, "Europe")
           ]
    columns = ["carr", "horsepower", "weight", "origin"]

    df = spark.createDataFrame(data= car, schema= columns)
    df.show(truncate = False)

    # modifying the default long data type to integer
