import sys


def shortest_link(updated_substrate_net, substrate_net, vrr, node_mapping):

    # This takes the updated_substrate_net (all physical links to CDN have been made 0)
    # and for all the edges that exist ('bw'), it creates a new entry in the node of that map
    # called 'edges' and adds that node number 
    #print((updated_substrate_net))
    for node in substrate_net:
        node['bw'][0] = 0
    temp = []
    for substrate_node in substrate_net:
        temp.append(substrate_node['bw'])
    for j in temp:
        j.pop(0)
        for i in range(len(j)):
            if j[i] > 0:
                j[i] = 1
    g= Graph()
    #print(len(node_mapping))
    for i in node_mapping:
        g.dijkstra(temp,node_mapping[i]-1)
    
    

            #for node in updated_substrate_net:
            #    node['edges'] = []
            #    for i in range(len(node['bw'])):
            #        if(node['bw'][i] > 0):
            #            node['edges'].append(i)
            #    
#
    #list(shortest_dist(updated_substrate_net, node['node'], 0))
            
class Graph:
 
    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
         
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    def printPath(self, parent, j):
        path = []
        for j in range(1,len(parent)):
            p1 = []
            while(parent[j] != -1):
                p1.append(j)
                j = parent[j]
            path.append(p1)
        print(path)

        
        
         
 
    def printSolution(self, dist, parent):
        src = 0
        for i in range(1, len(dist)):
            print("\n")
            self.printPath(parent,i)
 
    def dijkstra(self, graph, src):
 
        row = len(graph)
        col = len(graph[0])
 
        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row
 
        #Parent array to store
        # shortest path tree
        parent = [-1] * row
 
        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
             
        #Find shortest path for all vertices
        while queue:
 
            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)
    
            queue.remove(u)
 
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
 
 
        self.printSolution(dist,parent)


        

#class Graph():
#
#    def __init__(self, vertices):
#        self.V = vertices
#        self.graph = [[0 for column in range(vertices)]
#                      for row in range(vertices)]
#
#    def printSolution(self, dist):
#        print("Vertex \tDistance from Source")
#        for node in range(self.V):
#            print(node, "\t", dist[node])
#
## A utility function to find the vertex with
## minimum distance value, from the set of vertices
## not yet included in shortest path tree
#
#    def minDistance(self, dist, sptSet):
#
#        # Initialize minimum distance for next node
#        min = sys.maxsize
#
#    # Search not nearest vertex not in the
#    # shortest path tree
#        for u in range(self.V):
#            if dist[u] < min and sptSet[u] == False:
#                min = dist[u]
#                min_index = u
#
#        return min_index
#
## Function that implements Dijkstra's single source
## shortest path algorithm for a graph represented
## using adjacency matrix representation
#
#    def dijkstra(self, src):
#
#        dist = [sys.maxsize] * self.V
#        dist[src] = 0
#        sptSet = [False] * self.V
#
#        for cout in range(self.V):
#
#            # Pick the minimum distance vertex from
#            # the set of vertices not yet processed.
#            # x is always equal to src in first iteration
#            x = self.minDistance(dist, sptSet)
#
#        # Put the minimum distance vertex in the
#        # shortest path tree
#            sptSet[x] = True
#
#        # Update dist value of the adjacent vertices
#        # of the picked vertex only if the current
#        # distance is greater than new distance and
#        # the vertex in not in the shortest path tree
#            for y in range(self.V):
#                if self.graph[x][y] > 0 and sptSet[y] == False and \
#                        dist[y] > dist[x] + self.graph[x][y]:
#                    dist[y] = dist[x] + self.graph[x][y]
#        return dist
#        #self.printSolution(dist)
#
##Calculates the shortest distance (in terms of links) from a given source to destination
#
#
#def shortest_dist(graph, S, D):
#    queue = [(S, [S])]
#    while queue:
#      
#        (vertex, path) = queue.pop(0)
#        print(set(path))
#        print(set(graph[0]['edges']))
#        for next in (set(graph[vertex]["edges"])) - set(path):
#            if next == D:
#                yield path + [next]
#            else:
#                queue.append((next, path + [next]))
