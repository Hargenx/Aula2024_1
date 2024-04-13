# Importe as bibliotecas necessárias
from pyspark.sql import SparkSession
import locale
# Inicialize a sessão Spark
spark = SparkSession.builder.appName(
    "Análise de Dados de Habitação na Califórnia com Spark SQL"
).getOrCreate()

# Carregue o conjunto de dados california_housing_data.csv
df = spark.read.csv(
    "/content/sample_data/california_housing_train.csv", header=True, inferSchema=True
)

# Exiba o schema do DataFrame
df.printSchema()

# Exiba as primeiras linhas do conjunto de dados
df.show(5)

# Crie uma visão temporária
df.createOrReplaceTempView("habitat")

# Consulta 1: Calcule a média do valor mediano das casas
consulta_media_valor_mediano = (
    "SELECT AVG(median_house_value) AS media_valor_mediano FROM habitat"
)
resultado_media_valor_mediano = spark.sql(consulta_media_valor_mediano)
media_valor_mediano = resultado_media_valor_mediano.first()["media_valor_mediano"]
print(f"A média do valor mediano das casas é: {media_valor_mediano:.2f}")

# Consulta 2: Determine a quantidade de bairros únicos
consulta_qtd_bairros_unicos = (
    "SELECT COUNT(DISTINCT housing_median_age) AS qtd_bairros_unicos FROM habitat"
)
resultado_qtd_bairros_unicos = spark.sql(consulta_qtd_bairros_unicos)
qtd_bairros_unicos = resultado_qtd_bairros_unicos.first()["qtd_bairros_unicos"]
print(f"A quantidade de bairros únicos é: {qtd_bairros_unicos}")

# Consulta 3: Identifique o bairro com o valor mediano das casas mais alto
consulta_bairro_valor_maximo = """
    SELECT housing_median_age, MAX(median_house_value) AS max_valor_mediano
    FROM habitat
    GROUP BY housing_median_age
    ORDER BY max_valor_mediano DESC
    LIMIT 1
"""

resultado_bairro_valor_maximo = spark.sql(consulta_bairro_valor_maximo)
bairro_max_valor_mediano = resultado_bairro_valor_maximo.first()["housing_median_age"]
max_valor_mediano = resultado_bairro_valor_maximo.first()["max_valor_mediano"]
print(
    f"O bairro com o valor mediano das casas mais alto é: {bairro_max_valor_mediano}, com o valor de {max_valor_mediano:.2f}"
)

# Consulta 4: Determine o valor mediano das casas por cada bairro e ordene os resultados em ordem decrescente
consulta_valor_mediano_por_bairro = """
    SELECT housing_median_age, AVG(median_house_value) AS valor_mediano
    FROM habitat
    GROUP BY housing_median_age
    ORDER BY valor_mediano DESC
"""
resultado_valor_mediano_por_bairro = spark.sql(consulta_valor_mediano_por_bairro)
print("Valor mediano das casas por bairro:")
resultado_valor_mediano_por_bairro.show()




# Configurar a localidade para formatar os números como moeda
locale.setlocale(locale.LC_ALL, "")

# Exibir os resultados das consultas
print("Consulta 1: Média do valor mediano das casas")
print(
    f"Média do valor mediano das casas: ${locale.format_string('%.2f', media_valor_mediano, grouping=True)}"
)

print("\nConsulta 2: Quantidade de bairros únicos")
print(f"Quantidade de bairros únicos: {qtd_bairros_unicos}")

print("\nConsulta 3: Bairro com o valor mediano das casas mais alto")
print(
    f"Bairro com o valor mediano das casas mais alto: {bairro_max_valor_mediano}, valor: ${locale.format_string('%.2f', max_valor_mediano, grouping=True)}"
)

print("\nConsulta 4: Valor mediano das casas por bairro (ordenado)")
print("Bairro \t\t\t\t Valor Mediano das Casas")
for row in resultado_valor_mediano_por_bairro.collect():
    print(
        f"{row['housing_median_age']: <30} ${locale.format_string('%.2f', row['valor_mediano'], grouping=True)}"
    )


# Encerre a sessão Spark
spark.stop()
