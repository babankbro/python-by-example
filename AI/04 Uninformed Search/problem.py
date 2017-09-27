from graph import *
from node import *

names = ['Arad', "Zerid", "Oradea", "Sibiu", "Timisoara", "Lugoj", "Mehadia", "Drobeta",
         "Craiova", "Rimnicu Vilcea", "Pitesti", "Fagaras", "Bucharest", "Giurgiu", "Urziceni",
        "Vaslui", "Iasi", "Neamt", "Hirsova", "Eforie"]

graph = Graph()
for name in names:
    node = Node(name)
    graph.addNode(node)


graph.connect("Arad", "Zerid");
graph.connect("Arad", "Timisoara");
graph.connect("Arad", "Sibiu");

graph.connect("Zerid", "Oradea");

graph.connect("Oradea", "Sibiu");

graph.connect("Sibiu", "Fagaras");
graph.connect("Sibiu", "Rimnicu Vilcea");

graph.connect("Timisoara", "Lugoj");

graph.connect("Lugoj", "Mehadia");

graph.connect("Mehadia", "Drobeta");

graph.connect("Drobeta", "Craiova");

graph.connect("Craiova", "Rimnicu Vilcea");
graph.connect("Craiova", "Pitesti");

graph.connect("Rimnicu Vilcea", "Pitesti");

graph.connect("Pitesti", "Bucharest");

graph.connect("Bucharest", "Giurgiu");
graph.connect("Bucharest", "Urziceni");

graph.connect("Urziceni", "Hirsova");
graph.connect("Urziceni", "Vaslui");

graph.connect("Vaslui", "Iasi");
graph.connect("Iasi", "Neamt");

graph.connect("Hirsova", "Eforie");

print(graph)
