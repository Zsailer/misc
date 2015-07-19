# Python network generator for NetworkViewer 
#
from __future__ import absolute_import
import numpy as np
import argparse
import sys
import itertools as it

def list_binary(length):
    """ List all binary strings with given length. """
    return sorted(["".join(seq) for seq in it.product("01", repeat=length)])
    

def binary_neighbors(genotypes):
    """ Returns binary genotypes that differ by a site in binary sequence space."""
    dim = len(genotypes)
    chars = list(genotypes)

    neighbors = list()
    for c in range(0,dim):
        nb = list(genotypes)
        # Create a neighbor
        if chars[c] == '0':
            nb[c] = '1'
        else:
            nb[c] = '0'
        seq = "".join(nb)
        
        neighbors.append(seq)
    return neighbors


def binary_graph(n_sites):
    """ Generate a random binary network with 2**n_sites nodes. """
    sequences = list_binary(n_sites)
    edges = binary_neighbors(sequences)
    
    # creates this data structure: nodes = {"<node_label>": value}
    vals = [round(np.random.rand(),2) for i in range(len(sequences))]
    nodes = dict(zip(sequences, vals))
    
    # creates this data structure: edges = {index: (source, target)}
    links = dict(zip(range(len(edges)), edges))
    
    # creates this data structure: edges_sizes = {index: (source_size, target_size)}
    sizes = [(round(np.random.rand()), round(np.random.rand())) for i in range(len(links))]
    link_sizes = dict(zip(range(len(edges)), sizes))
    
    return nodes, links, link_sizes
    

def to_json(nodes, links, link_sizes, filename=None):
    """ Take dictionary of nodes and edges and format for networkviewer. 
    
        nodes = {"<node_label>": value}
        edges = {index: (source, target)}
        edges_sizes = {index: (source_size, target_size)}
    """
    full_dict = {"nodes":[], "links":[]}
    
    for n in nodes:
        full_dict["nodes"].append({n:nodes[n]})
    
    # Build links
    for i in links:
        element = { "source": links[i][0], 
                    "ssize": link_sizes[i][0],
                    "target":links[i][1],
                    "tsize": link_sizes[i][1]}
                    
        full_dict["links"].append(element)
        
    if filename is None:
        return full_dict
    else:
        import json
        with open(filename, 'w') as f:
            json.dump(full_dict, f)

def main(argv=None):
    """ Run main script. """
    
    if argv is None:
        argv = sys.argv[:]
          
    parser = argparse.ArgumentParser(description='Create a JSON serialized network for NetworkViewer.')
    
    parser.add_argument("n_sites", help="number of sites in sequence space.")   
    parser.add_argument("filename", help="filename")
    
    args = parser.parse_args(argv[1:])
    
    nodes, links, link_sizes = binary_graph(int(args.n_sites))
    to_json(nodes, links, link_sizes, filename=args.filename)

if __name__ == "__main__":
    main()