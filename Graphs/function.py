import queue
import time
import matplotlib.pyplot as plt
import networkx as nx

# Function to perform Breadth-First Search (BFS) on a graph
def bfs_order(graph, start_node):
    visited = set()         # Set to keep track of visited nodes
    q = queue.Queue()       # Queue for BFS
    q.put(start_node)       # Start with the given start node
    order = []              # List to store the order of traversal

    while not q.empty():    # While there are nodes to process
        vertex = q.get()    # Get the next node from the queue
        if vertex not in visited:  # If the node has not been visited
            order.append(vertex)   # Add it to the traversal order
            visited.add(vertex)    # Mark it as visited
            for node in graph[vertex]:  # For each connected node
                if node not in visited: # If it hasn't been visited
                    q.put(node)         # Add it to the queue
    return order  # Return the order of nodes as visited by BFS

# Function to perform Depth-First Search (DFS) on a graph
def dfs_order(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set if not already

    order = []  # List to store the order of traversal
    if start_node not in visited:  # If the start node hasn't been visited
        order.append(start_node)   # Add it to the traversal order
        visited.add(start_node)    # Mark it as visited
        for node in graph[start_node]:  # For each connected node
            if node not in visited:     # If it hasn't been visited
                order.extend(dfs_order(graph, node, visited))  # Recur and extend the order
    return order  # Return the order of nodes as visited by DFS

# Function to visualize the traversal order on a graph
def visualize(order, title, g, pos):
    plt.figure()  # Create a new figure
    plt.title(title)  # Set the title of the figure
    for i, node in enumerate(order, start=1):  # Iterate through the order of nodes
        plt.clf()  # Clear the current figure
        plt.title(title)  # Set the title of the figure
        # Draw the graph, coloring the current node red and others green
        nx.draw(g, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in g.nodes])
        plt.draw()  # Draw the figure
        plt.pause(0.5)  # Pause to create an animation effect
    plt.show()  # Show the final figure
    time.sleep(0.5)  # Pause before closing


# Function to generate a random connected graph
def generate_random(n, m):
    while True:
        g = nx.gnm_random_graph(n, m)  # Generate a random graph with n nodes and m edges
        if nx.is_connected(g):  # Check if the graph is connected
            return g  # Return the graph if it is connected
