import os

data = []
valores = []

with open('Desafio01\dados_financeiro.txt') as dados:
  dados.readline()
  for linha in dados:
    data.append(linha.split(',')[0])
    valores.append(int(linha.split(',')[1]))

total_meses = len(data)
valor_total = sum(valores)
media = valor_total/total_meses
maior_lucro = max(valores)
menor_lucro = min(valores)

# descobrindo o indice de cada valor (maior e menor) para saber a data correspondente
a = valores.index(maior_lucro)
mes_maior = data[a]
b = valores.index(menor_lucro)
mes_menor = data[b]

if not os.path.exists('Desafio01\\relatorio.txt'):
  with open('Desafio01\\relatorio.txt', 'w') as arquivo:
    arquivo.write('Análise Financeira\n------------------------------\n')
    arquivo.write(f'Total de meses: {total_meses}\n')
    arquivo.write(f'Total: $ {valor_total}\n')
    arquivo.write(f'Média: $ {media:.2f}\n')
    arquivo.write(f'Maior aumento dos lucros: {mes_maior} ($ {maior_lucro})\n')
    arquivo.write(f'Maior redução dos lucros: {mes_menor} ($ {menor_lucro})\n')
else:
  print('Relatório existente.')