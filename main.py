from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      ###TODO
      new_node = frontier.pop()
      result.add(new_node)
      neighbors = graph[new_node]
      for i in neighbors:
        if i  in result:
          pass
        else:
          frontier.add(i)
      #print(new_node)
      #print(neighbors)
      #print(frontier)
      
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
    ### TODO
    print(graph.keys())
    for i in graph.keys():
      reachable_list = reachable(graph, i)
      #print(i)
      #print(reachable_list)
      
      for j in graph.keys():
        if j not in reachable_list:
          return False
    return True
        
         
      
      
      
      
  

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
  """
    Returns:
      the number of connected components in an undirected graph
    """
  ## This is not necessary  
  if connected(graph) == True:
    return 1
  else:
    count = 0
    ## this is total rest nodes in the beginning
    remainder = set(graph.keys())
    while len(remainder) != 0:
      # for i in remainder:
      i = remainder.pop() ## start with one node to reach out others
      ## this output is all nodes can be reached from i
      reachable_list = reachable(graph, i)
      ## The rest nodes??
      remainder = remainder - reachable_list
      print(remainder)
        # graph_set = set(graph.keys())
        # remainder = graph_set.difference(reachable_list)
      count +=1 
  return count

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2

# graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
#print(graph)
#print(sorted(reachable(graph, 'A')))
#print(test_reachable())
print(n_components(graph))
