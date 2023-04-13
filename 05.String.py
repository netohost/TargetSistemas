#Declaramos duas variáveis, uma para a string em si e a outra a que queremos inverter, porém, a invertida passaremos como branco, pois é uma atribuição que ainda será coletada.

string = "A Target Sistemas é a melhor empresa do segmento."
string_invertida = ""

#Para i no alcance da quantidade de letras na variavel string subtraidas aos valores

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

#Exibe a String invertida

print(string_invertida)