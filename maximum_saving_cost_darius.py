##  https://github.com/AkanyijukaDarius
##  dariusakanyijuka3@gmail.com

def maximum_saving(input_network: str) -> int:

  nodes= ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  rows = [row.split(',') for row in input_network.strip().split('\n')]

  num_nodes = len(nodes)
  total_original_weight = 0
  edges = []


  ## calculating total weight of the original network

  for u  in range(num_nodes):
      for v in range(u + 1, num_nodes):
        weight_str = rows[u][v].strip()

        if weight_str and weight_str != '-' and weight_str != '':
            weight = int(weight_str)
            total_original_weight += weight
            edges.append((weight, nodes[u], nodes[v]))

  ##  sorting the edges based on their weights
  edges.sort()

  parent_network = { node : node for node in nodes }


  def find(w):
      if parent_network[w] != w:
        parent_network[w] = find(parent_network[w])
      return parent_network[w]

  def union(w, x):
    root_w = find(w)
    root_x = find(x)
    if root_w != root_x:
        parent_network[root_w] = root_x
        return True
    return False
 

  maximum_saving_network_cost = 0
  edges_in_maximum_saving_network = 0

  for weight , w, x in edges:

            ## cycle detection 
            if union(w, x):
                maximum_saving_network_cost += weight
                edges_in_maximum_saving_network += 1

                if edges_in_maximum_saving_network == num_nodes - 1:
                    break

  maximum_saving = total_original_weight - maximum_saving_network_cost
            
  return maximum_saving
  
  ## the input network 
  
input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''

result = maximum_saving(input_network)
print("Maximum saving cost is :", result)