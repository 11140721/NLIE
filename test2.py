from H import getH     #
import networkx as nx
from pylab import *
from C import getC         #
from E import Entropy
import sys
from combine import getValue

startTime = datetime.datetime.now()
G = nx.Graph()
with open('ca-astroph.txt', encoding='utf-8') as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head, tail)
G = G.to_undirected()
G.remove_edges_from(nx.selfloop_edges(G))
file.close()

c = getC(G)      #
h = getH(G)      #
e = Entropy(G)
print(c)
print(h)
print("各节点信息熵值：\n", e)
# print(c)
# print(h)
# print(e)

# assemble = getValue(degreeI, 1)
# 节点编号排序，文件名称为xk_1
f = []
s = []
for key in c.keys():     #
    res = h[key] * c[key] * e[key]   #
    f.append((key, res))
sortNum = sorted(f, key=lambda x: x[0], reverse=False)
nodelist = []
for key in sortNum:
    nodelist.append(key.__getitem__(0))
# print(nodelist)

f = open('xk_1ca-astroph.txt', "w+")
for key, val in sortNum:
    f.write(str(key)+'\t'+str(val)+"\n")
f.close()
"""
# 按照节点编号排序
f = []
for key in h.keys():
    res = c[key] * h[key] * e[key]    #
    f.append((key, res))

sortNum1 = sorted(f, key=lambda x: x[0], reverse=False)
# print(sortNum1)
nodelist1 = []
for key in sortNum1:
    nodelist1.append(key.__getitem__(0))
print(nodelist)
f = open('xk_1ca-astroph.txt', "w+")
for key, val in sortNum1:
    f.write(str(key)+'\t'+str(val)+"\n")
f.close()
"""
# 按照数值排序，节点编号名称为xk_
f = []
for key in h.keys():
    res = h[key] * c[key] * e[key]
    f.append((key, res))

sortNum1 = sorted(f, key=lambda x: x[1], reverse=True)
# print(sortNum)
nodelist1 = []
for key in sortNum1:
    nodelist1.append(key.__getitem__(0))
# print(nodelist)

f = open('xk_ca-astroph.txt', "w+")
for key, val in sortNum1:
    f.write(str(key)+'\t'+str(val)+"\n")
f.close()

"""    
# 将结果保存到文件中
for key in sortNum:
    # print(sortNum.__getitem__(key))
    with open("lnc_1karate.txt", "a") as g:
        g.write(str(key.__getitem__(0))+'\n')
    g.close()

endTime = datetime.datetime.now()
print(endTime - startTime)
"""

