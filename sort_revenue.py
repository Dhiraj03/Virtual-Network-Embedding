import numpy as np

def sort_revenue(graphs):
    rev = []
    for i in range(len(graphs)):
        edges = graphs[i]["edges"]
        nodes = graphs[i]["nodes"]
        cpu_total = sum(nodes)
        bw_total = sum(sum(edges,[]))
        graphs[i]["revenue"] = cpu_total + bw_total
        rev.append(graphs[i])
    return sorted(rev, key = lambda i: i['revenue'], reverse=True)