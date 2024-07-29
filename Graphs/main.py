from function import *

g = generate_random(10, 10)
pos = nx.spring_layout(g)
visualize(dfs_order(g, 0), 'dfs_search', g, pos)
visualize(bfs_order(g, 0), 'bfs_search', g, pos)


