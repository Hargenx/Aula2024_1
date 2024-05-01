import networkx as nx
import matplotlib.pyplot as plt

# Dados de precedência
precedencia = {
    1: [7, 15],
    2: [1],
    3: [2],
    4: [],
    5: [2, 17],
    6: [11, 17],
    7: [],
    8: [10, 19],
    9: [7],
    10: [5, 9],
    11: [15],
    12: [15],
    13: [12],
    14: [13, 18],
    15: [],
    16: [1, 12],
    17: [16],
    18: [6],
    19: [1],
}

# Criar grafo direcionado
G = nx.DiGraph()

# Adicionar nós e arestas ao grafo
for atividade, predecessores in precedencia.items():
    G.add_node(atividade)
    for predecessor in predecessores:
        G.add_edge(predecessor, atividade)

# Adicionar nó inicial e conectar aos nós iniciais
G.add_node("I")
for node in G.nodes():
    if len(list(G.predecessors(node))) == 0:
        G.add_edge("I", node)

# Adicionar nó final e conectar aos nós finais
G.add_node("F")
for node in G.nodes():
    if len(list(G.successors(node))) == 0:
        G.add_edge(node, "F")

# Posicionamento dos nós no gráfico
pos = nx.spring_layout(G)

# Desenhar grafo
plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=12,
    font_weight="bold",
)
plt.title("Grafo de Precedência")
plt.show()
