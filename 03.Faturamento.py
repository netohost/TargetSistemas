#Exercício 03 - Faturamento

#Começamos o código importando a biblioteca json
import json

#abrindo o arquivo faturamento.json
with open('faturamento.json') as file:
    faturamento_diario = json.load(file)

#A variável Média mensal é atribuida a soma dos valores do faturamento diarios divididos pela quantidade de caracteres do faturamento diario

media_mensal = sum(faturamento_diario.values()) / len(faturamento_diario)

#As variaveis de menor e maior valor recebem a mesma atribuição, porém, max e min são inseridos para coletarem o maior valor e o menor.

menor_valor = min(faturamento_diario.values())
maior_valor = max(faturamento_diario.values())
dias_acima_media = sum(1 for valor in faturamento_diario.values() if valor > media_mensal)

print("Menor valor diário:", menor_valor)
print("Maior valor diário:", maior_valor)
print("Dias acima da média mensal:", dias_acima_media)