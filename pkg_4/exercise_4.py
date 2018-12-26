from TdP_collections.graphs.graph import Graph


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
    La complessità computazionale è la stessa della DFS completa, e cioè O(n+m), siccome la classe Graph
    rappresenta il grafo utilizzando liste di adiacenza, in cui n è il numero di vertici ed m il numero di archi.
    """
    discovered = {}  # dizionario per tenere traccia dei nodi visitati
    color = {}  # dizionario per tenere traccia dei colori dei nodi
    X = set()  # partizioni del grafo
    Y = set()
    partition = None

    # verifica se il grafo è connesso e ne definisce le componenti connesse
    for node in G.vertices():  # inizializza i colori dei nodi
        if node not in color:
            color[node] = False
    for v in G.vertices():
        if v not in discovered:
            partition = color_dfs(G, v, discovered, color)
            if partition is None:
                return partition
    if partition is not None:
        # popola le due partizioni del grafo
        for x in partition.items():
            if x[1] is True:
                X.add(x[0])
            else:
                Y.add(x[0])
        return X, Y
    else:
        return partition


def color_dfs(g, u, discovered, color):
    """
    Sovrascrive l'algoritmo della DFS per aggiungere la logica di controllo della 2-colorabilità
    Colora i nodi visitati in maniera alternata, se trova due nodi consecutivi con lo stesso colore
    allora non è valida la condizione di 2-colorabiltà, cioè il grafo non è bipartito
    :param g: grafo da analizzare
    :param u: nodo di partenza della visita
    :param discovered: dizionario che mappa ogni nodo agli archi usati per visitarlo
    :param color: dizionario che mappa ogni nodo al suo colore
    :return: dizionario che mappa i nodi con il loro colore, None se il grafo non è bipartito
    Complessità computazionale O(n+m)

    NB: Questa funzione considera il grafo in ingresso g connesso
    """
    for e in g.incident_edges(u):  # per ogni arco uscente da u
        v = e.opposite(u)
        if v not in discovered:  # v è un nodo non visitato
            color[v] = not color[u]  # assegagli il colore opposto del nodo padre
            discovered[v] = e  # aggiorna gli archi discovey
            if color_dfs(g, v, discovered,
                         color) is None:  # riapplica ricorsivamente verificando che il sottoinsieme è bipartito
                return None
        elif color[v] == color[u]:  # nodo già visitato, 2 nodi consecutivi con lo stesso colore viola la 2-colorabilità
            return None
    return color
