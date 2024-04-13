dicionario = {}

for i in range(3):
    Posicao = "Posicao" + str(i)
    dicionario[Posicao] = {
        'Indice': i,
        'Nome': 'nome' + str(i)
    }

for j in range(3):
    Posicao = "Posicao" + str(j)
    print(dicionario[Posicao])
