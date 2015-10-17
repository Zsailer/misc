# Quick hack to generate trajectory json for NetworkViewer 
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

def counter2json(counter):
    """ Convert trajectory counter to json object. 
    
        counter = {"trajectory string": count}
    """
    
    

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
          
    parser = argparse.ArgumentParser(description='Create a JSON serialized trajectory dataset for NetworkViewer.')
    
    parser.add_argument("n_sites", help="number of sites in sequence space.")   
    parser.add_argument("filename", help="filename")
    
    args = parser.parse_args(argv[1:])
    
    G = binary_graph(int(args.n_sites))
    to_json(G, filename=args.filename)

if __name__ == "__main__":
    main()
