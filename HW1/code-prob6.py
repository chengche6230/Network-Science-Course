from igraph import *

def createGraph():
    g = Graph()
    nodes = []
    max_vertex_id = 0
    with open('tvshow_edges.csv') as f:
        f.readline()
        for line in f:
            nodes.append([int(s) for s in f.readline().split(',')])
            for n in nodes[len(nodes) - 1]:
                max_vertex_id = max(max_vertex_id, n)
    g.add_vertices(max_vertex_id + 1)
    for i in range(len(nodes)):
        g.add_edge(nodes[i][0], nodes[i][1])
    return g

def output(g):
    summary(g)
    print(f'Number of nodes: {g.vcount()}')
    print(f'Number of edges: {g.ecount()}')
    print(f'Mean degree: {sum(g.degree())/g.vcount()}')
    print(f'Maximum degree: {max(g.degree())}')
    print(f'Diameter: {g.diameter()}')

if __name__ == "__main__":
    g = createGraph()
    output(g)
