import cmnr as cmnr
import sort_revenue as sr
import vrr as vrr
import shortest_distance as sd
import mapping_function as mp
import shortest_link as sp
# Upper-level function


def main():
    # Take input for virtual network request (VNR)

    # 1. Create graphs for both substrate and virtual networks (VNR)

    # Substrate network = physical network
    substrate_network = cmnr.create_graph()
    # Substrate network
    substrate_nodes = [10, 10, 10, 10, 10, 10]
    substrate_edges = [
        [0, 10, 0, 10, 0, 0],
        [10, 0, 10, 0, 10, 0],
        [0, 10, 0, 0, 0, 10],
        [10, 0, 0, 0, 10, 0],
        [0, 10, 0, 10, 0, 10],
        [0, 0, 10, 0, 10, 0]
    ]

    unweighted_substrate_edges = [
        [0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0]
    ]

    

    # Virtual network
    input_nodes = [5, 5, 5]
    input_edges = [
        [0, 3, 3],
        [3, 0, 4],
        [3, 4, 0],
    ]

    virtual_network = {"nodes": input_nodes, "edges": input_edges}

    # 2. Calculating the revenues of all the requests (1 in our case)
    revenues = sr.sort_revenue([virtual_network])

    # 3. Calculating the VRR (Virtual Residual Resources) for each VNR
    sorted_vrr_graph = vrr.vrr(virtual_network)
    #Storing the unsorted_vrr_graph in order to use in edge-mapping
    unsorted_vrr_graph = vrr.format_vrr(virtual_network)
    # print(vrr_graph)

    #Assuming CDN is at the 0th node (substrate network)
    substrate_net = sd.add_hops(substrate_network, 0, unweighted_substrate_edges)
    node_map = mp.mapping_nodes(sorted_vrr_graph, substrate_net)

    print('For the given Virtual network request the Node mapping i as follow:\n')
    for i in node_map:
        print("Virtual node",i,"is mapped to Substrate Node",node_map[i])
    #print(node_map)
    
    #Edge Mapping
    #CDN node (substrate network) = 0
    #1. Remove all links from substrate links
    old_substrate_net = substrate_net
    #for node in substrate_net:
    #    node['bw'][0] = 0
    #temp = []
    #for substrate_node in substrate_net:
    #    temp.append(substrate_node['bw'])
    #for j in temp:
    #    for i in range(len(j)):
    #        if j[i] > 0:
    #            j[i] = 1

    #print(temp)



    #2. For each virtual link, search k-shortest path
    #sp.shortest_link(substrate_net, old_substrate_net, unsorted_vrr_graph, node_map)    




if __name__ == "__main__":
    main()
