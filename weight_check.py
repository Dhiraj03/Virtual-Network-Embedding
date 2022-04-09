import sys
def w_check(virtual_links, substrate_network, vrr):
    #print(virtual_links)
    #print(substrate_network)
    #print(vrr)
    for link in virtual_links:
        for node in vrr:
            if link['source'] == node['node']:
                v_bw = node['bw'][link['destination']] 
                link['min_bw'] = v_bw
        
        for i in range(len(link['path'])-1):
            for p_node in substrate_network:
                if p_node['node'] == link['path'][i]:
                    
                    if p_node['bw'][link['path'][i+1]] < link['min_bw']:
                        print("VNR not fulfilled as bandwidth provided was not sufficint")
                        return 0
    
    return 1

                
            