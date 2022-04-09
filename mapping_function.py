from re import sub

#Maps the virtual nodes to the substrate nodes
#Calculates the SRR (Substrate node residual resources) for each substrate node
#And sorts the substrates nodes in descending order of SRR, it also removes the Content server node from the network
# Then, each virtual node is mapped to the substrate nodes 
def mapping_nodes(vrr, substrate):
    node_mapping = {}
    
    for substrate_node in substrate:
        srr_i = pow(0.1, substrate_node['hops']) * substrate_node['cpu'] * sum(substrate_node['bw'])
        substrate_node["srr"] = srr_i
        if(substrate_node['hops'] == 0):
            cdn_node = substrate_node
       
    substrate.remove(cdn_node)
    substrate_net = sorted(substrate, key = lambda i: i['srr'], reverse=True)
    
    for virtual_node in vrr:
        biggest_node = substrate_net.pop(0)
        node_mapping[virtual_node['node']] = biggest_node['node']
    return node_mapping

    
