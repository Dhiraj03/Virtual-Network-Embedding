import sys


def shortest_link(updated_substrate_net, substrate_net, vrr, node_mapping):

    # This takes the updated_substrate_net (all physical links to CDN have been made 0)
    # and for all the edges that exist ('bw'), it creates a new entry in the node of that map
    # called 'edges' and adds that node number 
    for node in updated_substrate_net:
        node['edges'] = []
        for i in range(len(node['bw'])):
            if(node['bw'][i] > 0):
                node['edges'].append(i)
        

    list(shortest_dist(updated_substrate_net, node['node'], 0))
            


        

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

    # Search not nearest vertex not in the
    # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

# Function that implements Dijkstra's single source
# shortest path algorithm for a graph represented
# using adjacency matrix representation

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shortest path tree
            sptSet[x] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        return dist
        #self.printSolution(dist)

#Calculates the shortest distance (in terms of links) from a given source to destination


def shortest_dist(graph, S, D):
    queue = [(S, [S])]
    while queue:
      
        (vertex, path) = queue.pop(0)
        print(set(path))
        print(set(graph[0]['edges']))
        for next in (set(graph[vertex]["edges"])) - set(path):
            if next == D:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
