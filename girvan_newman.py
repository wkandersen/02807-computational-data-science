"""
Girvan-Newman community detection algorithm
Optimized version with efficient edge betweenness calculation
"""
import networkx as nx


def all_edge_betweeness(G):
    """
    Calculate betweenness for all edges using NetworkX's optimized implementation
    Much faster than custom implementation, especially for dense graphs
    """
    betweenness = nx.edge_betweenness_centrality(G)
    result = []
    for edge, score in betweenness.items():
        result.append([list(edge), score])
    return result


def bfs(graph):
    """Perform BFS from each node to find connected components"""
    result = {}
    for node in list(graph.nodes()):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        result[node] = set(visited)
    return result


def counting_clusters(bfs_result):
    """Find distinct connected components from BFS result"""
    distinct_sets = []
    for aSet in list(bfs_result.values()):
        if not aSet in distinct_sets:
            distinct_sets.append(aSet)
    return distinct_sets


def clustering(G_original, max_iterations=None):
    """
    Run Girvan-Newman algorithm to find all possible community structures
    """
    communities = {}
    nb_iterations = 0
    
    # Create a copy of the graph
    G = nx.Graph()
    G.add_nodes_from(G_original.nodes())
    G.add_edges_from(G_original.edges())
    G = G.to_undirected()
    
    total_edges = len(list(G.edges()))
    print(f"Starting Girvan-Newman with {total_edges} edges...")
    
    while len(list(G.edges())) > 0:      
        # Compute betweenness centrality for all edges
        b_c_edges = all_edge_betweeness(G)
        b_c_edges.sort(key=lambda x: x[1], reverse=True)
        
        # Remove the edge with highest centrality
        G.remove_edge(b_c_edges[0][0][0], b_c_edges[0][0][1])
        
        # Check the number of sub graphs in G
        clusters_result = bfs(G)
        distinct_sets = counting_clusters(clusters_result)
        
        # Save sets
        communities[nb_iterations] = distinct_sets
        nb_iterations += 1
        
        # Stop early if max_iterations reached
        if max_iterations and nb_iterations >= max_iterations:
            print(f"Stopped at max_iterations: {max_iterations}")
            break
    
    return communities


def compute_modularity_for_all_communities(G, all_communities):
    """Compute modularity for all community structures found using NetworkX"""
    result = []
    for clusters in all_communities.values():
        Q = nx.community.modularity(G, clusters)
        result.append([clusters, Q])
    return result



def girvan_newman(G, max_iterations=None):
    """Main function to run Girvan-Newman and find best communities"""
    # Run clustering algorithm
    communities = clustering(G, max_iterations=max_iterations)
    print("Computing modularity for all partitions...")
    
    # Compute modularity for all structures
    all_clusters_with_modularity = compute_modularity_for_all_communities(G, communities)
    all_clusters_with_modularity.sort(key=lambda x: x[1], reverse=True)
        
    # Extract best result
    best_communities = [list(s) for s in all_clusters_with_modularity[0][0]]
    best_modularity = all_clusters_with_modularity[0][1]
    print(f"\nBest partition: {len(best_communities)} communities")
    print(f"Best modularity: {best_modularity:.4f}")
    
    return best_communities, best_modularity