# Step 1 - Setting up PySpark
from pyspark.sql import SparkSession
# Create SparkSession
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .master("local[*]") \
    .getOrCreate()

# spark:SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com".getOrCreate()

# Get SparkContext from SparkSession
sc = spark.sparkContext

# Step 2 - Loading the data into an RDD
data = [
    "1,101,5001,Laptop,Electronics,1000.0,1",
    "2,102,5002,Headphones,Electronics,50.0,2",
    "3,101,5003,Book,Books,20.0,3",
    "4,103,5004,Laptop,Electronics,1000.0,1",
    "5,102,5005,Chair,Furniture,150.0,1"
]
transactions_rdd = sc.parallelize(data)

transactions_rdd.collect()
transactions_rdd.count()
# a. map() transformation - Converting csv string into a tuple for better handling
transactions_tuple_rdd = transactions_rdd.map(lambda x: tuple(x.split(",")))
transactions_tuple_rdd.collect()

# b. filter transformation() -filter out transactions where the quantity is greater than 1
high_quantity_rdd = transactions_tuple_rdd.filter(lambda x: int(x[6]) > 1)
high_quantity_rdd.collect()

# c. flat map transformations
# extract all products bought by customers to understand the diversity in purchases.
products_flat_rdd = transactions_tuple_rdd.flatMap(lambda x: [x[3]])
products_flat_rdd.collect()


# Step 4
# a. Creating a pair RDD - Create a pair RDD of (customer_id, (product_name, total_price)) for further analysis.
pair_rdd = transactions_tuple_rdd.map(lambda x:(x[1], (x[3], float(x[5]) * int(x[6]))))
# customer_id (column index 1), (product_name (column index 3), total price (price(column 5)* quantity (column 6))
pair_rdd.collect()

# b. reduceByKey() transformation - find the total amount spent by each customer.
customer_spending_rdd = pair_rdd.map(lambda x: (x[0],x[1][1])).reduceByKey(lambda x, y:x+y)
customer_spending_rdd.collect()

# c. groupByKey() transformation - Get a list of all products purchased by each customer.
customer_products_rdd = pair_rdd.groupByKey().mapValues(list)
customer_products_rdd.collect()

# Step 5
# Join with product_category_rdd to get category information for each product purchased by customers.

# Define the product_category_rdd for joining with transaction data
product_category_data = [
    ('Laptop', 'Electronics'),
    ('Headphones', 'Electronics'),
    ('Book', 'Books'),
    ('Chair', 'Furniture')
    ]

product_category_rdd = sc.parallelize(product_category_data)
product_category_rdd.collect()

customer_product_category_rdd = pair_rdd.map(lambda x:(x[1][0], (x[0], x[1][1]))).join(product_category_rdd)
customer_product_category_rdd.collect()


# Step 6 - Actions to collects Results
# a. collect total spending per customer
total_spending = customer_spending_rdd.collect()
# b. collect products purchased per customer
products_per_customer = customer_products_rdd.collect()
# c. collect product category join results
product_category_info = customer_product_category_rdd.collect()

# Step 7 - Save the results
customer_spending_rdd.saveAsTextFile("file:///home/takeo/pycharmprojects/customer_spending")
customer_products_rdd.saveAsTextFile("file:///home/takeo/pycharmprojects/customer_products")
customer_product_category_rdd.saveAsTextFile("file:///home/takeo/pycharmprojects/customer_product_category")
