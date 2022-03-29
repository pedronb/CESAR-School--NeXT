id_eleitor = []
municipio = []
candidato = []
#candidato_result = []
cont_k = 0
cont_c = 0
cont_l = 0
cont_o = 0

def percent(votos, total):
  return (votos*100)/total

with open('dados\dados_elecao.txt') as arq:
  arq.readline()
  for linha in arq:
    id_eleitor.append(linha.split(',')[0])
    municipio.append(linha.split(',')[1].strip())
    candidato.append(linha.split(',')[2].strip())

for i in candidato:
  if i == 'Khan':
    cont_k += 1
  elif i == 'Correy':
    cont_c += 1
  elif i == 'Li':
    cont_l += 1
  elif i == "O'Tooley":
    cont_o += 1

total_votos = len(id_eleitor)
porcent_khan = percent(cont_k, total_votos)
porcent_correy = percent(cont_c, total_votos)
porcent_li = percent(cont_l, total_votos)
porcent_otooley = percent(cont_o, total_votos)

with open('resultado.txt', 'w') as result:
  result.write('Resultados eleitorais\n'+'-'*30 + '\n')
  result.write(f'Total de votos: {total_votos}\n' + '-'*30 + '\n')
  result.write(f'Khan: {porcent_khan:.2f}% ({cont_k})\nCorrey: {porcent_correy:.2f}% ({cont_c})\nLi: {porcent_li:.2f}% ({cont_l})\nOTooley: {porcent_otooley:.2f}% ({cont_o})\n' + '-'*30 + '\n')

  lista_vencedor = [cont_k, cont_c, cont_l, cont_o]
  vencedor = max(lista_vencedor)

  if vencedor == cont_k:
    result.write(f'Vencedor: Khan\n' + '-'*30)
  elif vencedor == cont_c:
    result.write(f'Vencedor: Correy\n' + '-'*30)
  elif vencedor == cont_l:
    result.write(f'Vencedor: Li\n' + '-'*30)
  elif vencedor == cont_o:
    result.write(f'Vencedor: OTooley\n' + '-'*30)


# Para elminar as duplicatas dentro da lista candidato e formar uma lista com os candidatos que receberam votos.
#for i in candidato:
#    if i not in candidato_result:
#        candidato_result.append(i)



