temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
sala = []
for i in range(len(temperaturas)):
    x = 0
    soma_das_temperaturas = sum(temperaturas[i])
    media_das_temperaturas = soma_das_temperaturas / len(temperaturas[i])

    for k in range(len(temperaturas[i])):
        if temperaturas[i][k] >= 33:
            x += 1

    sala.append(x)

    print(f"Sala {i+1}")
    print(f"Temperatura média da sala de aula {i+1}: {media_das_temperaturas}")
    print(f"Quantidade de dias com temperatura acima de 33°C na sala de aula {i+1}: {x}")
    print()

maior_qtd = max(sala)
indice_sala = sala.index(maior_qtd)
print(f"A sala de aula {indice_sala + 1} tem a maior quantidade de dias com temperatura acima de 33°C, com {maior_qtd} dias.")
  
    
    