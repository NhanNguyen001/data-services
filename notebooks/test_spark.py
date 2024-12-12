from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("JupyterTest") \
    .master("spark://spark-master:7077") \
    .config("spark.driver.memory", "1g") \
    .config("spark.executor.memory", "1g") \
    .getOrCreate()

# Create a test DataFrame
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["name", "value"])

# Show the DataFrame
print("DataFrame contents:")
df.show()

# Perform a simple transformation
df_upper = df.select("name", "value") \
    .withColumn("name_upper", df.name.upper())

print("\nTransformed DataFrame:")
df_upper.show()

# Get Spark UI URL
print(f"\nSpark UI available at: http://localhost:8090")

# Clean up
spark.stop() 