import networkx as nx
import matplotlib.pyplot as plt

def equivalent_resistance(graph):
    # Keep simplifying the graph until only one node remains
    while len(graph.nodes) > 1:
        # Find series connections and simplify
        series_edges = find_series_edges(graph)
        for edge in series_edges:
            simplify_series(graph, edge)
        
        # Find parallel connections and simplify
        parallel_edges = find_parallel_edges(graph)
        for edge in parallel_edges:
            simplify_parallel(graph, edge)

        # Plot the current graph after each iteration
        plot_graph(graph)

    # After simplification, only one node remains; return its resistance
    return graph.nodes[next(iter(graph.nodes))]['resistance']

def find_series_edges(graph):
    # Detect edges in series
    series_edges = []
    for edge in graph.edges(data=True):
        u, v, data = edge
        if data.get('type') == 'series':  # Check if edge type is series
            series_edges.append((u, v))
    return series_edges

def find_parallel_edges(graph):
    # Detect edges in parallel
    parallel_edges = []
    for edge in graph.edges(data=True):
        u, v, data = edge
        if data.get('type') == 'parallel':  # Check if edge type is parallel
            parallel_edges.append((u, v))
    return parallel_edges

def simplify_series(graph, edge):
    u, v = edge
    # Get the resistances of both nodes
    resistance_u = graph.nodes[u].get('resistance', 0)
    resistance_v = graph.nodes[v].get('resistance', 0)

    # Combine resistances for series connection
    equivalent_resistance = resistance_u + resistance_v
    print(f"Simplifying Series: {resistance_u} + {resistance_v} = {equivalent_resistance}")
    
    # Replace nodes u and v with a new node that has the equivalent resistance
    new_node = f"{u}-{v}"  # Create a new node name
    graph.add_node(new_node, resistance=equivalent_resistance)
    
    # Remove the original series edge
    graph.remove_edge(u, v)
    
    # Add new edges from the new node
    for neighbor in list(graph.neighbors(u)):
        if neighbor != v:
            graph.add_edge(new_node, neighbor, type='series')
    
    for neighbor in list(graph.neighbors(v)):
        if neighbor != u:
            graph.add_edge(new_node, neighbor, type='series')

    # Remove the old nodes from the graph
    graph.remove_node(u)
    graph.remove_node(v)

def simplify_parallel(graph, edge):
    u, v = edge
    # Get the resistances of both nodes
    resistance_u = graph.nodes[u].get('resistance', 0)
    resistance_v = graph.nodes[v].get('resistance', 0)

    # Combine resistances for parallel connection
    equivalent_resistance = 1 / (1 / resistance_u + 1 / resistance_v)
    print(f"Simplifying Parallel: 1/({1/resistance_u} + {1/resistance_v}) = {equivalent_resistance}")
    
    # Replace nodes u and v with a new node that has the equivalent resistance
    new_node = f"{u}|{v}"  # Create a new node name
    graph.add_node(new_node, resistance=equivalent_resistance)
    
    # Remove the original parallel edge
    graph.remove_edge(u, v)
    
    # Add new edges from the new node
    for neighbor in list(graph.neighbors(u)):
        if neighbor != v:
            graph.add_edge(new_node, neighbor, type='parallel')
    
    for neighbor in list(graph.neighbors(v)):
        if neighbor != u:
            graph.add_edge(new_node, neighbor, type='parallel')

    # Remove the old nodes from the graph
    graph.remove_node(u)
    graph.remove_node(v)

def plot_graph(graph):
    # Use matplotlib to plot the current graph state
    pos = nx.spring_layout(graph)  # positions for all nodes
    labels = nx.get_edge_attributes(graph, 'type')
    
    # Draw nodes and edges
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight="bold", font_color="black")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    
    plt.title("Circuit Graph (Current State)")
    plt.show()

# Example usage
G = nx.Graph()

# Add nodes with resistance values
G.add_node(1, resistance=5)
G.add_node(2, resistance=10)
G.add_node(3, resistance=15)

# Add edges with types (series or parallel)
G.add_edge(1, 2, type='series')
G.add_edge(2, 3, type='parallel')

# Print the final equivalent resistance
print("Final Equivalent Resistance:", equivalent_resistance(G))
