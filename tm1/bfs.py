# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict
import queue

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):
         print(max(self.graph)+1)
         visited = [False] * (max(self.graph) + 1)
         queue=[s]
         visited[s]=True

         while queue:

            s=queue.pop(0)
            print(s,end=' ')
            
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

	

# Driver code


# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is BFS from (starting from vertex 2)")
g.BFS(2)

# This code is contributed by Neelam Yadav
