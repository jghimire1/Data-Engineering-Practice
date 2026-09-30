def mapped(spark):
    data = [('James', 'Smith', 'M', 30),
            ('Anna', 'Rose', 'F', 41),
            ('Robert', 'Williams', 'M', 62),
            ]

    columns = ["firstname", "lastname", "gender", "salary"]
    df = spark.createDataFrame(data=data, schema=columns)
    print("----data frame----")
    df.show()

    # Referring columns by index.
    rdd2 = df.rdd.map(lambda x: (x[0]+","+x[1],x[2],x[3]*2))
    df2 = rdd2.toDF(["name","gender","new_salary"])
    print("----data frame 2---")
    df2.show()

    # Referring columns Names
    rdd3 = df.rdd.map(lambda x: (x["firstname"]+","+x["lastname"],x["gender"],x["salary"]*2))
    rdd3.collect()
    print(rdd3)

    # Referring Column Names- alternate method
    rdd4 = df.rdd.map(lambda x:
                      (x.firstname + "," + x.lastname, x.gender, x.salary * 2)
                      )

    rdd4.collect()
    print(rdd4)

     # By Calling function
    def func1(x):
        firstName = x.firstname
        lastName = x.lastname
        name = firstName + "," + lastName
        gender = x.gender.lower()
        salary = x.salary * 2
        return (name, gender, salary)

    rdd2 = df.rdd.map(lambda x: func1(x))
    rdd2.collect()

    # Foreach example
    def f(x): print(x)

    df.foreach(f)

    # Another example
    df.foreach(lambda x:
               print("Data ==>" + x["firstname"] + "," + x["lastname"] + "," + x["gender"] + "," + str(x["salary"] * 2))
               )
   







