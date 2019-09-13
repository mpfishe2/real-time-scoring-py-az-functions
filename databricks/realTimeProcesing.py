from pyspark.sql.functions import *

streamDF = spark.read.readStream \
                        .format("eventhubs") \
                        .load()

colsToSelect = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]

streamDF.select(*colsToSelect).writeStream.format("eventhubs")