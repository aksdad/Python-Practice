class Status(object):
    UNVISITED = 1
    VISITING = 2
    VISITED = 3

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.edges = dict()
        self.status = Status.UNVISITED

    def add_edge(self, v, w = 0):
        self.edges[v] = w

    def __str__(self):
        return str(self.key) + ' connected: ' + str([x.key for x in self.edges])

    def get_edges(self):
        return self.edges.keys()

    def get_key(self):
        return self.key

    def get_weigth(self, v):
        return self.edges[v]

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

class Graph(object):
    def __init__(self, digraph = False):
        self.vertices = dict()
        self.v = 0
        self.digraph = digraph

    def add_vertex(self, key):
        self.v += 1
        self.vertices[key] = Vertex(key)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def __contains__(self, v):
        return v in self.vertices

    def add_edge(self, f, t, w = 0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_edge(self.vertices[t], w)
        if not self.digraph:
            self.vertices[t].add_edge(self.vertices[f], w)

    def __iter__(self):
        return iter(self.vertices.values())

    def reset_visits(self):
        for v in iter(self):
            v.set_status = Status.UNVISITED