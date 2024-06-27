# Databricks notebook source
#renames the columns of a DataFrame (df) by converting camelCase column names to snake_case.
dbutils.fs.ls('/mnt/silver/SalesLT')

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('/mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/'+name
    print(path)
    df = spark.read.format('delta').load(path)

    #list column names
    column_names = df.columns

    for old_col_name in column_names:
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = '/mnt/gold/SalesLT/' +name +'/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

display(df)