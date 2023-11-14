from combine import getValue
from pylab import *
import networkx as nx
# B-->D

# 计算的为自身节点影响力
a = {}
def getH(G):
    N = G.number_of_nodes()
    for i in G.nodes:
        influ = 0
        degreeI = G.degree(i)    # 某个节点的度
        assemble = getValue(degreeI, 1)
        k_shell = nx.core_number(G)
        for ks in k_shell:
            p = (1/degreeI) * (2 ** (ks/N))
        influ += assemble * (math.pow(p, 1)) * (math.pow((1 - p), degreeI-1))
        a.setdefault(i, influ)
    return a

