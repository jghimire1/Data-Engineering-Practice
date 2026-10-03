from pyspark.sql import SparkSession
from movie_rating_analysis_method import movie_rating

if __name__== '__main__':
    spark: SparkSession = SparkSession.builder.appName("Movie Ratings Analysis").getOrCreate()

    movie_rating(spark)
