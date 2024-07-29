import queue
import time
import matplotlib.pyplot as plt
import networkx as nx


def bfs_order(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order


def dfs_order(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    order = []
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(dfs_order(graph, node, visited))
    return order


def visualize(order, title, g, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(g, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in g.nodes])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)


def generate_random(n, m):
    while True:
        g = nx.gnm_random_graph(n, m)
        if nx.is_connected(g):
            return g



