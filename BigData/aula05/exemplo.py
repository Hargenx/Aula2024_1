import pandas as pd
import numpy as np

media = 0
desvio_padrao = 0.1
pd_temporario = pd.DataFrame(np.random.normal(media, desvio_padrao, 100))
spark_temporario = spark.createDataFrame(pd_temporario)
print(spark.catalog.listTables())
spark_temporario.createOrReplaceTempView('nova_tabela_temporaria')
print(spark.catalog.listTables())