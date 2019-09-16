def bfs(g, start_node):
  
  import math
  graph = g.copy()
  visited = []
  queue = deque()
  rs_dict = dict()

  for node in graph:
    rs_dict[node] = math.inf
  rs_dict[start_node] = 0

  queue.append(start_node)
  while queue:
    parent_node = queue.popleft()
    visited.append(parent_node)
 
    for child_node in graph[parent_node]:
      if child_node not in visited and child_node not in queue:
        rs_dict[child_node] = rs_dict[parent_node] + 1
        queue.append(child_node)

  return rs_dict

def in_degree(graph):
  rs_dict = dict()
  
  for node in graph:
    rs_dict[node] = 0
  
  for parent_node in graph:
    for child_node in graph[parent_node]:
      rs_dict[child_node] += 1
  
  return rs_dict

def top_sort(graph):
  
  rs_queue = deque()
  g_dict = in_degree(graph)

  for node in g_dict:
    if g_dict[node] == 0:
      rs_queue.append(node)
  
  while rs_queue:

    parent_node = rs_queue.popleft()
    print(parent_node)

    for child_node in graph[parent_node]:
      g_dict[child_node] -= 1
      if g_dict[child_node] == 0:
        rs_queue.append(child_node)

from collections import deque

g = {
  "A": ["B"],
  "B": ["E"],
  "E": [],
  "C": ["B", "D"],
  "D": ["B"]
}

# g = {
#   "A": ["B", "E"],
#   "B": ["C", "F", "A"],
#   "E": ["A", "F", "K"],
#   "C": ["B", "F", "G"],
#   "F": ["B", "E", "C"],
#   "K": ["E", "G", "L"],
#   "G": ["C", "K", "J"],
#   "L": ["K"],
#   "J": ["G"]
# }

# print(bfs(g, "A"))

print(in_degree(g))
top_sort(g)




# l = dict()
# for parent_node in g:
#   b = bfs(g, parent_node)
#   max = 0
#   for node in b:
#     if b[node] > max:
#       max = b[node]
#   l[parent_node] = max

# max = 0

# for node in l:
#     if l[node] > max:
#       max = l[node]


# print(max)

# saved = l.copy()

# min = max

# for node in l:
#     if l[node] < min:
#       min = l[node]

# print(min)

# rs = set()
# for node in saved:
#   if saved[node] == min:
#     rs.add(node)

# print(rs)