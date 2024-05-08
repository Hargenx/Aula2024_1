cores_calcas = ['azul', 'preta', 'marrom']
cores_camisetas = ['branca', 'verde', 'rosa', 'amarela', 'preta']
i = 0
for calca in cores_calcas:
    for camiseta in cores_camisetas:
        i += 1
        print("{}: Calça {} com camiseta {}".format(i, calca, camiseta))
