class DirectedGraph:
	"""DirectedGraph class has GetEdges, GetNodes, Connect
	FindPath, FindAllPath, Find_Shortest_Path methods.
	Implemented by dictionary."""
	def __init__(self, graph = {}):
		self.graph = graph
		
	def GetEdges(self):
		edges = []
		for node in self.graph: # it's the same: for node in self.graph.keys()
			for neighbor in self.graph[node]:
				edges.append((node, neighbor))
		return edges

	def GetNodes(self):
		vertice = []
		for node in self.graph:
			if node not in vertice:
				vertice.append(node)
			for neighbor in self.graph[node]:
				if neighbor not in vertice:
					vertice.append(neighbor)
		return vertice

	def Connect(self, start, end):
		if start not in self.graph:
			self.graph[start] = [end]
		else:
			self.graph[start].append(end)

	def FindPath(self, start, end, path = []):	# DFS
		path = path + [start]
		if start == end:  # exit 
			return path
		if start not in self.graph: # dead end
			return 
		for node in self.graph[start]:
			if node not in path:  # path itself marked the visited nodes.
				return self.FindPath(node, end, path)
		
	def FindAllPath(self, start, end):
		path = []
		self.paths = []
		self.DFS(start, end, path)
		return self.paths
	def DFS(self, start, end, path):
		path = path + [start]
		if start == end:  # exit 
			self.paths.append(path)
			return
		if start not in self.graph: # dead end
			return 
		for node in self.graph[start]:
			if node not in path:
				self.DFS(node, end, path)

	def Find_Shortest_Path(self, start, end):
		all_paths = self.FindAllPath(start, end)
		shortest_path = all_paths[0]
		for path in all_paths:
			if len(path) < len(shortest_path):
				shortest_path = path
		return shortest_path
				
graph = {'A':['B', 'C'],
		'B': ['C', 'D'],
		'C': ['CD'],
		'CD': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C', 'G']}
g = DirectedGraph(graph)
g.Connect('K', 'E')
# print g.GetEdges()
# print g.GetNodes()
print g.FindPath('A', 'D')
# print g.FindAllPath('A', 'D')
# print g.Find_Shortest_Path('A', 'D')
		