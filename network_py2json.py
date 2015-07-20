# Python network generator for NetworkViewer 
#
# Requires numpy and networkx
#

from __future__ import absolute_import
import numpy as np
import argparse
import sys
import itertools as it
import networkx as nx
from networkx.readwrite import json_graph

def list_binary(length):
    """ List all binary strings with given length. """
    return sorted(["".join(seq) for seq in it.product("01", repeat=length)])
    
def binary_neighbors(genotype):
    """ Returns binary genotypes that differ by a site in binary sequence space."""
    dim = len(genotype)
    chars = list(genotype)

    neighbors = list()
    for c in range(0,dim):
        nb = list(genotype)
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
    
    G = nx.Graph()
    
    # Add edges
    sequences = list_binary(n_sites)
    edges = []
    for s in sequences:
        edges += [(s, n) for n in binary_neighbors(s)]
    
    G.add_edges_from(edges)
    # Add nodes
    node2value = dict()
    for i, seq in enumerate(G.nodes()):
        value = round(np.random.rand(), 3)
        G.node[seq]["name"] = i
        G.node[seq]["value"] = value
        node2value[seq] = value
        
    # Build edges
    for edge in G.edges():
        G.edge[edge[0]][edge[1]]["ssize"] = node2value[edge[0]]
        G.edge[edge[0]][edge[1]]["tsize"] = node2value[edge[1]]

    return G

def to_json(G, filename=None):
    """ Take dictionary of nodes and edges and format for networkviewer. 
    
        nodes = {"<node_label>": value}
        edges = {index: (source, target)}
        edges_sizes = {index: (source_size, target_size)}
    """
    s = json_graph.node_link_data(G)
        
    if filename is None:
        return s
    else:
        import json
        with open(filename, 'w') as f:
            json.dump(s, f)
            
def main(argv=None):
    """ Run main script. """
    
    if argv is None:
        argv = sys.argv[:]
          
    parser = argparse.ArgumentParser(description='Create a JSON serialized network for NetworkViewer.')
    
    parser.add_argument("n_sites", help="number of sites in sequence space.")   
    parser.add_argument("filename", help="filename")
    
    args = parser.parse_args(argv[1:])
    
    G = binary_graph(int(args.n_sites))
    to_json(G, filename=args.filename)

if __name__ == "__main__":
    main()
