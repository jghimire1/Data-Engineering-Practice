# MapType(Dict)
from pyspark.sql.types import StringType, MapType
from pyspark.sql.types import StructField, StructType, StringType, MapType
from pyspark.sql.functions import explode
from pyspark.sql.functions import map_keys
from pyspark.sql.functions import explode,map_keys
from pyspark.sql.functions import map_values


def map_type_method(spark):
    global schema
    mapCol = MapType(StringType(), StringType(), False)

    schema = StructType([
        StructField('name', StringType(), True),
        StructField('properties', MapType(StringType(), StringType()), True)
    ])

    dataDictionary = [
        ('James', {'hair': 'black', 'eye': 'brown'}),
        ('Michael', {'hair': 'brown', 'eye': None}),
        ('Robert', {'hair': 'red', 'eye': 'black'}),
        ('Washington', {'hair': 'grey', 'eye': 'grey'}),
        ('Jefferson', {'hair': 'brown', 'eye': ''})
    ]
    df = spark.createDataFrame(data=dataDictionary, schema=schema)
    df.printSchema()
    df.show(truncate=False)

    #Pyspark maptype elements
    df3 = df.rdd.map(lambda x: \
                         (x.name, x.properties["hair"], x.properties["eye"])) \
        .toDF(["name", "hair", "eye"])
    df3.printSchema()
    print("pyspark maptype elements......")
    df3.show()

    df.withColumn("hair", df.properties.getItem("hair")) \
        .withColumn("eye", df.properties.getItem("eye")) \
        .drop("properties") \
        .show()

    df.withColumn("hair", df.properties["hair"]) \
        .withColumn("eye", df.properties["eye"]) \
        .drop("properties") \
        .show()

    # explode functions
    df.select(df.name, explode(df.properties)).show()

    # map_keys() - Get all map keys
    df.select(df.name, map_keys(df.properties)).show()

    # In case you wanted to get all map keys as Python List.
    keysDF = df.select(explode(map_keys(df.properties))).distinct()
    keysList = keysDF.rdd.map(lambda x: x[0]).collect()
    print(keysList)
    # ['eye', 'hair']

    # map_values() -- get all map values
    df.select(df.name, map_values(df.properties)).show()
