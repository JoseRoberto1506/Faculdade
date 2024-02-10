class Vertex:
  def __init__(self, data, color=None, d=None, parent=None):
    self.data = data
    self.color = color
    self.d = d
    self.parent = parent


class Graph:
  def __init__(self):
    self.vertices = {}


  def add_vertex(self, vertex):
    if vertex not in self.vertices:
      self.vertices[vertex] = []


  def add_edge(self, vertex_1, vertex_2):
    if vertex_1 in self.vertices and vertex_2 in self.vertices:
      self.vertices[vertex_1].append(vertex_2)
      self.vertices[vertex_2].append(vertex_1)


  def get_neighbors(self, vertex):
    return self.vertices[vertex]


  def bfs(self, s): # O(V + E)
    for u in self.vertices:
      u.color = "WHITE"
      u.d = 0
      u.parent = None
    s.color = "GRAY"
    s.d = 0
    s.parent = None
    q = []
    q.append(s)
    while q:
      u = q.pop(0)
      for v in self.vertices[u]:
        if v.color == "WHITE":
          v.color = "GRAY"
          v.d = u.d + 1
          v.parent = u
          q.append(v)
      u.color = "BLACK"


  def dfs_visit(self, u, time):
    time += 1
    u.d = time
    u.color = "GRAY"
    for v in self.vertices[u]:
      if v.color == "WHITE":
        v.parent = u
        self.dfs_visit(v, time)
    u.color = "BLACK"
    time += 1
    u.f = time


  def dfs(self): # Θ(V + E)
    for u in self.vertices:
      u.color = "WHITE"
      u.parent = None
    time = 0
    for u in self.vertices:
      if u.color == "WHITE":
        self.dfs_visit(u, time)


  def topo_sort(self): # Θ(V + E)
    self.dfs()
    sorted_vertices = sorted(self.vertices.keys(), key=lambda u: u.f, reverse=True)
    return sorted_vertices


if __name__ == "__main__":
  g = Graph()

  n1 = Vertex('you')
  n2 = Vertex('alice')
  n3 = Vertex('bob')
  n4 = Vertex('claire')
  n5 = Vertex('anuj')
  n6 = Vertex('peggy')
  n7 = Vertex('thom')
  n8 = Vertex('jonny')

  g.add_vertex(n1)
  g.add_vertex(n2)
  g.add_vertex(n3)
  g.add_vertex(n4)
  g.add_vertex(n5)
  g.add_vertex(n6)
  g.add_vertex(n7)
  g.add_vertex(n8)

  g.add_edge(n1,n2)
  g.add_edge(n1,n3)
  g.add_edge(n1,n4)
  g.add_edge(n2,n6)
  g.add_edge(n3,n5)
  g.add_edge(n3,n6)
  g.add_edge(n4,n7)
  g.add_edge(n4,n8)
  
  print(f"Breadth-First Search\n{'-' * 20}")
  g.bfs(n1)
  for vertex in g.vertices:
      print(f"Vertex {vertex.data}: color={vertex.color}, distance={vertex.d}, parent={vertex.parent.data if vertex.parent else None}")

  print(f"\nDepth-First Search\n{'-' * 20}")
  g.dfs()
  for vertex in g.vertices:
      print(f"Vertex {vertex.data}: color={vertex.color}, distance={vertex.d}, parent={vertex.parent.data if vertex.parent else None}")

  ordem_topologica = g.topo_sort()
  print(f"\nOrdenação topológica\n{'-' * 20}")
  for vertex in ordem_topologica:
    print(f"{vertex.data}, ", end="")
