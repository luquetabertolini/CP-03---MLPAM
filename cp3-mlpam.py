import pandas as pd
import matplotlib.pyplot as plt

# LEITURA DO BANCO

dados = pd.read_csv("genz_social_media_usage_1M.csv")

print(dados.head())


# a) TABELAS DE DISTRIBUIÇÃO DE FREQUÊNCIA


print("\n===== TABELA DE FREQUÊNCIA - GÊNERO =====\n")

freq_genero = dados["gender"].value_counts()

print(freq_genero)


# b) GRÁFICOS PARA VARIÁVEIS QUALITATIVAS

# Gráfico 1 - Gênero

dados["gender"].value_counts().plot(kind="bar")

plt.title("Distribuição por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade")

plt.show()


# Gráfico 2 - Plataforma Principal

dados["primary_platform"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.title("Plataforma Principal")

plt.ylabel("")

plt.show()


# c) GRÁFICOS PARA VARIÁVEIS QUANTITATIVAS

# Gráfico 1 - Horas de Uso Diário

dados["daily_usage_hours"].plot(kind="hist", bins=10)

plt.title("Horas de Uso Diário")
plt.xlabel("Horas")
plt.ylabel("Frequência")

plt.show()


# Gráfico 2 - Score de Saúde Mental

dados["mental_health_score"].plot(kind="box")

plt.title("Score de Saúde Mental")

plt.show()


# d) MEDIDAS DE TENDÊNCIA CENTRAL

print("\n===== MEDIDAS DE TENDÊNCIA CENTRAL =====\n")

# Variável 1
print("Daily Usage Hours")

print("Média:", dados["daily_usage_hours"].mean())
print("Mediana:", dados["daily_usage_hours"].median())
print("Moda:", dados["daily_usage_hours"].mode()[0])

print("\n")

# Variável 2
print("Mental Health Score")

print("Média:", dados["mental_health_score"].mean())
print("Mediana:", dados["mental_health_score"].median())
print("Moda:", dados["mental_health_score"].mode()[0])


# e) MEDIDAS DE DISPERSÃO

print("\n===== MEDIDAS DE DISPERSÃO =====\n")

# Variável 1
print("Daily Usage Hours")

print("Amplitude:", dados["daily_usage_hours"].max() - dados["daily_usage_hours"].min())
print("Variância:", dados["daily_usage_hours"].var())
print("Desvio Padrão:", dados["daily_usage_hours"].std())

print("\n")

# Variável 2
print("Mental Health Score")

print("Amplitude:", dados["mental_health_score"].max() - dados["mental_health_score"].min())
print("Variância:", dados["mental_health_score"].var())
print("Desvio Padrão:", dados["mental_health_score"].std())


# f) MEDIDAS SEPARATRIZES

print("\n===== MEDIDAS SEPARATRIZES =====\n")

# Quartis - Variável 1

print("Daily Usage Hours")

print("Q1:")
print(dados["daily_usage_hours"].quantile(0.25))

print("Q2:")
print(dados["daily_usage_hours"].quantile(0.50))

print("Q3:")
print(dados["daily_usage_hours"].quantile(0.75))

print("\n")

# Quartis - Variável 2

print("Mental Health Score")

print("Q1:")
print(dados["mental_health_score"].quantile(0.25))

print("Q2:")
print(dados["mental_health_score"].quantile(0.50))

print("Q3:")
print(dados["mental_health_score"].quantile(0.75))