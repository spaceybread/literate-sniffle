import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase
from collections import defaultdict

wds = []
with open("filtered_list.txt") as f:
    for line in f:
        w = line.strip()
        if w: wds.append(w)

G = nx.DiGraph()

starts = defaultdict(list)
for w in wds: starts[w[0]].append(w)

for w in wds:
    last_char = w[-1]
    for target in starts[last_char]: G.add_edge(w, target)

pos = nx.spring_layout(G, seed=1, k=0.1, iterations=50)
plt.figure(figsize=(12, 8))
nx.draw(G,
        pos,
        with_labels = True,
        node_color = 'lightblue',
        edge_color = 'gray',
        node_size = 500,
        font_size = 10,
        arrowsize = 10)
plt.show()
