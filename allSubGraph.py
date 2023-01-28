import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations 

   
node=[]
subGraphs=[]

class GraphVisualization:
   
    def __init__(self):
        self.visual = []
          
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def getEdgeList(self,a):
        for i in a:
            self.visual.append(i)
    
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.title(self.visual)
        plt.show()

    def subgraphplot(self):
        S=nx.path_graph(4)
        H=S.subgraph(self.visual)
        nx.draw_networkx(H)
        plt.show()
        
## get input of edge and set node list and inputgraph list
"""
            simple input:
            1 2
            2 3
            1 3
            1 4
            END
"""
def getListOfEdgeGraph():
    print("enter enge num like \"0 1\" at the end enter \"END\"")
    edgelist=[]
    input1=input()
    
    while input1!="END":
        
        z=list(map(int,input1.split(" ")))
        if z[0] not in node:
            node.append(z[0])
        if z[1] not in node:
            node.append(z[1])
        edgelist.append(z)
        input1=input()
    E=GraphVisualization()
    E.getEdgeList(edgelist)
    E.visualize()
    return edgelist


inputGraph=getListOfEdgeGraph()
nubmerNode=len(node)

#extract all subgraph of the given graph
for i in range(len(node),0,-1):
    coms=combinations(inputGraph,i)
    for com in coms:
        if com not in subGraphs:
            subGraphs.append(com)


# print matrix of subgraph which exist in graphs
count=1
for subgraph in subGraphs:
    print (count ,"th subgraph \n")
    l=[]
    for i in range(len(node)):
        l.append([])
        for j in range(len(node)):
            l[i].append(0)

    
    for edge in subgraph:
        
        l[edge[0]-1][edge[1]-1]=1
        l[edge[1]-1][edge[0]-1]=1
        
    for i in range(len(node)):
        print(l[i])
    print("\n")
    count+=1            


#show the subgraph which exist in subgraphs
for subgraph in subGraphs:
    sub=GraphVisualization()
    sub.getEdgeList(subgraph)
    sub.visualize()