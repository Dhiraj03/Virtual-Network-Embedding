import cmnr as cmnr
import sort_revenue as sr
import vrr as vrr
import shortest_distance as sd
import mapping_function as mp

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
    vrr_graph = vrr.vrr(virtual_network)
    # print(vrr_graph)

    #Assuming CDN is at the 0th node (substrate network)
    substrate_net = sd.add_hops(substrate_network, 0, unweighted_substrate_edges)
    node_map = mp.mapping_nodes(vrr_graph, substrate_net)
    print(node_map)
    #Edge Mapping





if __name__ == "__main__":
    main()
