from pyspark.sql import SparkSession

# Inicialize a sessão Spark
spark = SparkSession.builder.appName("Exemplo Spark SQL no Colab").getOrCreate()

# Carregue o arquivo JSON
dados = spark.read.json("dados.json")

# Criar uma visão temporária
dados.createOrReplaceTempView("pessoas")

# Execute uma consulta SQL
consulta = "SELECT MAX(idade) AS max_idade FROM pessoas"
resultado = spark.sql(consulta)

# Exiba o resultado usando f-string
max_idade = resultado.first()["max_idade"]
print(f"A idade máxima é: {max_idade}")

# Pare a sessão Spark
spark.stop()
