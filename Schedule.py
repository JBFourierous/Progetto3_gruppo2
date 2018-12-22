from TdP_collections.graphs.graph import Graph


class Schedule(Graph):
    class Airport(Graph.Vertex):
        """Airport is the new vertex of the graph"""
        __slots__ = '_name', '_c'

        def __init__(self, n, c):
            self._name = n
            self._c = c

        def coincidence(self):
            return self._c

        def name(self):
            return self._name

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(self._name)

        def __str__(self):
            return str(self._name) + str(self._c)

    class Flight(Graph.Edge):

        __slots__ = '_origin', '_destination', '_leave', '_arrive', '_seats'

        def __init__(self, u, v, leave, arrive, n):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._leave = leave
            self._arrive = arrive
            self._seats = n

        def origin(self):
            return self._origin

        def destination(self):
            return self._destination

        def leave(self):
            return self._leave

        def arrive(self):
            return self._arrive

        def seats(self):
            return self._seats

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination, self._leave, self._arrive, self._seats))

        def __str__(self):
            return '({0},{1},{2},{3},{4})'.format(self._origin, self._destination, self._leave, self._arrive, self._seats)

    def _validate_airport(self, a):
        """Verify that a is an Airport of this graph."""
        if not isinstance(a, self.Airport):
            raise TypeError('Airport expected')
        if a not in self._outgoing:
            raise ValueError('Airport does not belong to this graph.')

    def insert_airport(self, name, c):
        """Insert and return a new Airport with name name and coincidence time c"""
        a = self.Airport(name, c)
        self._outgoing[a] = {}
        if self.is_directed():
            self._incoming[a] = {}  # need distinct map for incoming edges
        return a

    def insert_flight(self, u, v, leave, arrive, seats):
        """Insert and return a new Flight from u to v.

        Raise a ValueError if u and v are not airports of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        f = self.Flight(u, v, leave, arrive, seats)
        self._outgoing[u][v] = f
        self._incoming[v][u] = f

