#Scatter Plot of Differences of Local Clustering coefficients:
#n=10k

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def isprime(n):
    for t in range (2,int(np.sqrt(n))+2):
        if n%t==0:
            return 0
        elif t==int(np.sqrt(n))+1:
            return 1
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
v=8770    #n-pi(n)-1
a=np.zeros(shape=(v,1))
j=-1
for i in range (4,n):
    if isprime(i)==0:
        j+=1
        if isprime(i+1)==0:
            a[j]=nx.clustering(P,i+1)-nx.clustering(P,i)
        else:
            a[j]=nx.clustering(P,i+2)-nx.clustering(P,i)
plt.plot(a,'.',color='black')
plt.xlabel('k')
plt.ylabel('c(k+1)-c(k)')
plt.show()
plt.savefig('LC_n=10k.png')