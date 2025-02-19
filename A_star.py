# import heapq
# from timeit import default_timer as timer

# def a_star_search(graph, start, goal, heuristic):
#     start_time = timer()
    
#     open_set = []  
#     heapq.heappush(open_set, (0, start, [start], 0))  # (estimated_cost, node, path, current_cost)
    
#     visited = set()
#     explored_nodes = 0  # Compteur pour le nombre de nœuds explorés

#     while open_set:
#         _, current_node, path, current_cost = heapq.heappop(open_set)
#         explored_nodes += 1  # Incrémenter le compteur pour chaque nœud exploré

#         if current_node == goal:
#             end_time = timer()
#             elapsed_time = end_time - start_time
#             print(f"A* - Chemin trouvé: {path}")
#             print(f" Coût total: {current_cost}")
#             print(f" Nœuds explorés: {explored_nodes}")
#             print(f" Temps d'exécution: {elapsed_time:.6f} secondes")
#             return path, current_cost

#         if current_node not in visited:
#             visited.add(current_node)
#             for neighbor, weight in graph.get(current_node, []):
#                 if neighbor not in visited:
#                     estimated_cost = current_cost + weight + heuristic(neighbor, goal)
#                     heapq.heappush(open_set, (estimated_cost, neighbor, path + [neighbor], current_cost + weight))

#     end_time = timer()
#     elapsed_time = end_time - start_time
#     print(f"A* - Aucun chemin trouvé.")
#     print(f" Nœuds explorés: {explored_nodes}")
#     print(f" Temps d'exécution: {elapsed_time:.6f} secondes")
#     return None, float('inf')

# #Graphe d'exemple
# graph = {
#     'A': [('B', 5), ('C', 2), ('D', 8)],
#     'B': [('A', 5), ('E', 10), ('F', 3)],
#     'C': [('A', 2), ('G', 4), ('H', 7)],
#     'D': [('A', 8), ('I', 6), ('J', 12)],
#     'E': [('B', 10), ('K', 3)],
#     'F': [('B', 3), ('L', 6)],
#     'G': [('C', 4), ('M', 2)],
#     'H': [('C', 7), ('N', 5)],
#     'I': [('D', 6), ('O', 8)],
#     'J': [('D', 12), ('P', 15)],
#     'K': [('E', 3)],
#     'L': [('F', 6)],
#     'M': [('G', 2)],
#     'N': [('H', 5)],
#     'O': [('I', 8)],
#     'P': [('J', 15)]
# }



# # Fonction heuristique
# def heuristic(node, goal):
#     heuristic_values = {
#         'A': 10, 'B': 8, 'C': 7, 'D': 9,
#         'E': 6, 'F': 7, 'G': 6, 'H': 5,
#         'I': 5, 'J': 4, 'K': 3, 'L': 2,
#         'M': 4, 'N': 5, 'O': 1, 'P': 0
#     }
#     return heuristic_values[node]

# # Appel de la fonction
# path, cost = a_star_search(graph, 'A', 'P', heuristic)
#         (A)
#        / | \
#       /  |  \
#      B   C   D
#     /|   |   |\
#    E F   G   I J
#    | |   |   |  \
#    K L   M   O   P
#        H   N  

import heapq
from timeit import default_timer as timer

def a_star_search(graph, start, goal, heuristic):
    start_time = timer()
    
    open_set = []  
    heapq.heappush(open_set, (0, start, [start], 0))  # (estimated_cost, node, path, current_cost)
    
    visited = set()
    explored_nodes = 0  

    while open_set:
        _, current_node, path, current_cost = heapq.heappop(open_set)
        explored_nodes += 1  

        if current_node == goal:
            end_time = timer()
            elapsed_time = end_time - start_time
            print(f"A* - Chemin trouvé: {path}")
            print(f" Coût total: {current_cost}")
            print(f" Nœuds explorés: {explored_nodes}")
            print(f" Temps d'exécution: {elapsed_time:.6f} secondes")
            return path, current_cost

        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph.get(current_node, []):
                if neighbor not in visited:
                    estimated_cost = current_cost + weight + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (estimated_cost, neighbor, path + [neighbor], current_cost + weight))

    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"A* - Aucun chemin trouvé.")
    print(f" Nœuds explorés: {explored_nodes}")
    print(f" Temps d'exécution: {elapsed_time:.6f} secondes")
    return None, float('inf')

# Graphe
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('G', 1)],
    'B': [('G', 2)]
}

# Heuristique
def heuristic(node, goal):
    heuristic_values = {'S': 2, 'A': 1, 'B': 2, 'G': 0}
    return heuristic_values[node]

# Exécution
print("\n--- A* ---")
a_star_search(graph, 'S', 'G', heuristic)




#        S
#       / \
#     (1) (4)
#     /     \
#    A       B
#     \     /
#     (1)  (2)
#       \ /
#        G
