import sys


def shortest_link(updated_substrate_net, substrate_net, vrr, node_mapping):

    # This takes the updated_substrate_net (all physical links to CDN have been made 0)
    # and for all the edges that exist ('bw'), it creates a new entry in the node of that map
    # called 'edges' and adds that node number

    #Removing all the substrate links directly connected to the content server
    for node in substrate_net:
        node['bw'][0] = 0

    
    temp = []
    for substrate_node in substrate_net:
        temp.append(substrate_node['bw'])
    print("temp")
    print(temp)
    for j in temp:
        j.pop(0)
        for i in range(len(j)):
            if j[i] > 0:
                j[i] = 1
    g= Graph()
    virtual_links = []
    temp_path = []
    count = 0
    #print(len(node_mapping))
    for i in node_mapping:
        if len(temp_path)!=0:
            virtual_links.append({
                'path':[x+1 for x in temp_path[(node_mapping[i]-1)]],
                'source':prev_node, 'destination':i, 'link_no': count})
        else:
            first = node_mapping[i]-1
            v_first = i
        prev_node = i
        path = g.dijkstra(temp,node_mapping[i]-1)
        temp_path = path
        count += 1
    virtual_links.append({
        'path':[x+1 for x in temp_path[first]],
        'source':prev_node,'destination':v_first,'link_no': count})
    return virtual_links
    
                
class Graph:
 
    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
         
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    def printPath(self, parent):
        path = []
        for j in range(0,len(parent)):
            p1 = []
            while(parent[j] != -1):
                p1.append(j)
                j = parent[j]
            p1.append(j)
            path.append(p1)
        return path

        
        
         
 
    def printSolution(self, dist, parent):
        src = 0
        #for i in range(1, len(dist)):
        return self.printPath(parent)
 
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
 
 
        return self.printSolution(dist,parent)

