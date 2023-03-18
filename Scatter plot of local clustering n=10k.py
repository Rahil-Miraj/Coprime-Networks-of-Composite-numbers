#Scatter Plot of Local Clustering coefficients:
#n=10k

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
n=10000
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
f=plt.figure()
f.set_figheight(2)
f.set_figwidth(10)
plt.xlabel('k')
plt.ylabel('c(k)')
plt.plot(nx.clustering(P).values(),'.',color='black')
plt.show()
#plt.savefig('Local_clustering_n=10k.png')