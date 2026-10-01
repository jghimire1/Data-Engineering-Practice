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

    










