from pyspark.sql.functions import *
def inc_sal(df):
    df=df.withColumn("salary",col("salary")+1500)
    return df

def ren_col(df):
    return df.withcolumnrenamed("salary","n_salary")