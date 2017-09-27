from graph import *
from node import *

names = ['Arad', "Zerid", "Oradea", "Sibiu", "Timisoara", "Lugoj", "Mehadia", "Drobeta",
         "Craiova", "Rimnicu Vilcea", "Pitesti", "Fagaras", "Bucharest", "Giurgiu", "Urziceni",
        "Vaslui", "Iasi", "Neamt", "Hirsova", "Eforie"]

graph = DistanceGraph()
for name in names:
    node = Node(name)
    graph.addNode(node)


graph.connect("Arad", "Zerid", 75);
graph.connect("Arad", "Timisoara", 118);
graph.connect("Arad", "Sibiu", 140);

graph.connect("Zerid", "Oradea", 71);

graph.connect("Oradea", "Sibiu", 151);

graph.connect("Sibiu", "Fagaras", 99);
graph.connect("Sibiu", "Rimnicu Vilcea", 80);

graph.connect("Timisoara", "Lugoj", 111);

graph.connect("Lugoj", "Mehadia", 70);

graph.connect("Mehadia", "Drobeta", 75);

graph.connect("Drobeta", "Craiova", 120);

graph.connect("Craiova", "Rimnicu Vilcea", 146);
graph.connect("Craiova", "Pitesti", 138);

graph.connect("Rimnicu Vilcea", "Pitesti", 97);

graph.connect("Pitesti", "Bucharest", 101);

graph.connect("Bucharest", "Giurgiu", 90);
graph.connect("Bucharest", "Urziceni", 85);

graph.connect("Urziceni", "Hirsova", 98);
graph.connect("Urziceni", "Vaslui", 142);

graph.connect("Vaslui", "Iasi", 142);
graph.connect("Iasi", "Neamt", 87);

graph.connect("Hirsova", "Eforie", 86);

print(graph)
