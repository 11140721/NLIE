import networkx as nx
# nums = G.number_of_nodes()  # 节点数
# 邻居贡献
a = {}
def getC(G):
    N = G.number_of_nodes()
    for i in G.nodes():
        totalDegree = 0     # 节点的度
        Contri = 0          # ？
        neighbors = G.neighbors(i)    # 节点i的所有邻居
        degreeI = G.degree(i)         # 节点i的度
        for neighbor in neighbors:
            k_shell = nx.core_number(G)      # 所有节点的k_shell值
            count = G.degree(neighbor)
            for ks in k_shell:
                p = (1/count) * (2 ** (ks/N))            # 邻居贡献概率p ：邻居节点度数的倒数 * k_shell值
            totalDegree = totalDegree + count  # 计算所有节点的度之和
            Contri += p * (count / (G.number_of_nodes()-1))   # G.number_of_nodes() 求节点数目
            pNeighbors = totalDegree * Contri * degreeI     # 节点的邻居和
        a.setdefault(i, pNeighbors)
    return a