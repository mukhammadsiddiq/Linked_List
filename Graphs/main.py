from function import *

g = generate_random(30, 30)
pos = nx.spring_layout(g)
visualize(bfs_order(g, 0), 'dfs_search', g, pos)


