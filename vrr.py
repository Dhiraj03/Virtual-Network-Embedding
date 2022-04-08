#Calculating the centrality for all the virtual nodes
def nc(graph):
    nodes = graph["nodes"]
    edges = graph["edges"]
    nc = []
    for i in range(len(nodes)):
        nc.append(0)
        for edge in edges[i]:
            if edge != 0:
                nc[i] += 1
    return nc

#Calculating, sorting and returning the list of virtual nodes (by VRR)
def vrr(graph):
    nodes = graph["nodes"]
    edges = graph["edges"]
    vrr = []
    nc_graph = nc(graph)
    for i in range(len(nodes)):
        vrr_i = nc_graph[i] * nodes[i] * sum(edges[i])
        vrr.append({"node": i,"cpu" : nodes[i], "bw": edges[i], "vrr" : vrr_i})
    vrr_graph = sorted(vrr, key = lambda i: i['vrr'], reverse=True)
    return vrr_graph
    
def format_vrr(graph):
    nodes = graph["nodes"]
    edges = graph["edges"]
    vrr = []
    nc_graph = nc(graph)
    for i in range(len(nodes)):
        vrr_i = nc_graph[i] * nodes[i] * sum(edges[i])
        vrr.append({"node": i,"cpu" : nodes[i], "bw": edges[i], "vrr" : vrr_i})
    return vrr
