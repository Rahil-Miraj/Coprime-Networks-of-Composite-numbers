#Av_clustering for n=10k,20k,30k,40k,50k

import numpy as np
import networkx as nx
f = open('Av_clustering outputs.txt', 'w')
def av_clustering(n):
    P = nx.Graph()
    for i in range (4,n+1):
        for t in range (2,int(np.sqrt(i))+1):
            if i%t==0:
                P.add_nodes_from([i])
                for j in range (1,i):
                    for s in range (2,int(np.sqrt(j))+1):
                        if j%s==0:
                            if np.gcd(i,j)==1:
                                P.add_edges_from ([(j,i)])
                                break
                break
    return nx.average_clustering(P)
for i in range (1,6):
    print('Av_clustering for n=',i*10000,'=',av_clustering(i*10000), file = f)