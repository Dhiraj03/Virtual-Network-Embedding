#Creates a graph to simulate the physical (substrate) network
def create_graph():
    nodes = [10, 10, 10, 10, 10, 10]
    edges = [
        [0, 10, 0, 10, 0, 0],
        [10, 0, 10, 0, 10, 0],
        [0, 10, 0, 0, 0, 10],
        [10, 0, 0, 0, 10, 0],
        [0, 10, 0, 10, 0, 10],
        [0, 0, 10, 0, 10, 0]
    ]

    graph = {"nodes": nodes, "edges": edges}
    new_graph = []
    for i in range(len(graph["nodes"])):
        new_graph.append({"node": i, "cpu": graph["nodes"][i], "bw": graph["edges"][i]})
    return new_graph