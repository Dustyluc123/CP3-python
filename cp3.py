temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
sala = []
for i in range(len(temperaturas)):
    x = 0
    
    for j in range(i+1, len(temperaturas)):
        if temperaturas[i][j] >= 33:
            x+= 1
    soma_das_temperaturas = sum(temperaturas[i])
    media_das_temperaturas = soma_das_temperaturas / 4
    sala.append(x)
   
   
    print(f"Sala {i+1}")
    print(f"Temperatura média da sala de aula {i+1}: {media_das_temperaturas}")
    print(f"Quantidade de dias com temperatura acima de 33°C na sala de aula {i+1}: {x}")
    print()
for i in range(len(sala)):
    if sala[i] > sala[1] and sala[i] > sala[2] and sala[i] > sala[3]:
        print(f"A sala de aula {i+1} tem a maior quantidade de dias com temperatura acima de 33°C, com {sala[i]} dias.")
    
    