from TdP_collections.graphs.graph import Graph
from TdP_collections.graphs.dfs import DFS, DFS_complete


def bipartite(G: Graph):
    """
    La funzione verifica se G è bipartito e restituisce una partizione (X, Y) dei vertici di G tale che
    tutti gli archi del grafo collegano un vertice di X ad un vertice di Y. Nel caso in cui il grafo non
    sia bipartito la funzione deve restituire None.
    :param G: grafo non diretto da ispezionare
    :return: None se il grafo non è bipartito, altrimenti una sua partizione

    Il problema corrisponde alla verifica della k-colorabilità di un grafo, cioè verificare se è possibile,
    dato un grafo non diretto, colorarlo con al più k colori in modo che non esistano due vertici adiacenti
    dello stesso colore. Nel caso il problema si riduce alla 2-colorabilità.
    """
    forest = {}                                 # spanning forest del grafo G
    discovered = {}                             # dizionario per tenere traccia dei nodi visitati
    color = {}                                  # dizionario per tenere traccia dei colori dei nodi
    X = []                                      # partizioni del grafo
    Y = []
    # verifica se il grafo è connesso e ne definisce le componenti connesse
    forest = DFS_complete(G)
    for node in G.vertices():                   # inizializza i colori dei nodi
        color[node] = False
    start_node = color.keys()[0]                # prendi un nodo del grafo da cui partire per una visita DFS
    # applica la DFS modificata per verificare se il grafo è bipartito
    partition = dfs(G, start_node, discovered, color)
    if partition is not None:                   # popola le due partizioni del grafo
        for x in partition.items():
            if x[1] is True:
                X.append(x[0])
            else:
                Y.append(x[0])
        return X,Y
    else:
        return partition


def dfs(g, u, discovered, color):
    """
    Sovrascrive l'algoritmo della DFS per aggiungere la logica di controllo della 2-colorabilità
    Colora i nodi visitati in maniera alternata, se trova due nodi consecutivi con lo stesso colore
    allora non è valida la condizione di 2-colorabiltà, cioè il grafo non è bipartito
    :param g: grafo da analizzare
    :param u: nodo di partenza della visita
    :param discovered: dizionario che mappa ogni nodo agli archi usati per visitarlo
    :param color: dizionario che mappa ogni nodo al suo colore
    :return: dizionario che mappa i nodi con il loro colore, None se il grafo non è bipartito

    ATTENZIONE: QUESTA IMPLEMENTAZIONE SUPPONE CHE IL GRAFO SIA CONNESSO
    """
    for e in g.incident_edges(u):                           # per ogni arco uscente da u
        v = e.opposite(u)
        if v not in discovered:                             # v è un nodo non visitato
            color[v] = not color[u]                         # assegagli il colore opposto del nodo padre
            discovered[v] = e                               # aggiorna gli archi discovey
            if dfs(g, v, discovered, color) is None:        # riapplica ricorsivamente verificando che il sottoinsieme è bipartito
                return None
        elif color[v] == color[u]:                          # nodo già visitato, 2 nodi consecutivi con lo stesso colore viola la 2-colorabilità
            return None
    return color

