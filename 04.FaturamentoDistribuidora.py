#Abrimos o elemento faturamento e os atribuímos os valores abaixo

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#Variavel total mensal é a soma dos valore de faturamento

total_mensal = sum(faturamento.values())

#Para cada estado e valor nos items de faturamento é realizada a seguinte conta: Porcentual = Valor / Total Mensal * 100

for estado, valor in faturamento.items():
    percentual = valor / total_mensal * 100

#Printa o resultado percentual da representação de cada estado que a distribuidora atua.
    
    print(estado, "-", percentual, "%")