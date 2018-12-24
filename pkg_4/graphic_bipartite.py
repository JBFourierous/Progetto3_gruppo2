import networkx as nx
import matplotlib.pyplot as plt


def graphic_from_partition(C, D, edges, title):
    G = nx.Graph()
    input = list()
    for i in edges:
        input.append((i._origin.element(), i._destination.element(), i._element))
    G.add_weighted_edges_from(input)
    pos = dict()
    pos.update((n, (2, invert(i, C))) for i, n in enumerate(C))  # put nodes from X at x=1
    pos.update((n, (1, invert(i, D))) for i, n in enumerate(D))  # put nodes from Y at x=2

    plt.title(title)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=900, node_color='w', edgecolors='r', linewidths=1)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    # edges
    nx.draw_networkx_edges(G, pos, width=1, edge_color='b')
    nx.draw_networkx_edge_labels(G, pos, font_color='b')

    plt.axis('off')
    plt.savefig(title+".png")
    plt.show()


def invert(i, C) -> int:
    return i+len(C) - (2*i) - 1
