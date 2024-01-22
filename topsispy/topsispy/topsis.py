import pandas as pd
import numpy as np

def topsis(matrix,weights,impacts):
    # Convert input to NumPy array for easier manipulation
    matrix=np.array(matrix,dtype=float)
    
    # Normalize the decision matrix
    normalized_matrix=matrix/np.linalg.norm(matrix,axis=0)
    
    # Multiply the normalized matrix with weight
    weighted_matrix = normalized_matrix * weights

    # Ideal and negative-ideal solutions (considering impacts)
    ideal_best = np.max(weighted_matrix, axis=0) * (1 if impact == '+' else -1 for impact in impacts)
    ideal_worst = np.min(weighted_matrix, axis=0) * (1 if impact == '-' else -1 for impact in impacts)

    # Calculate Euclidean distances to ideal and negative-ideal solutions
    distance_to_best = np.linalg.norm(weighted_matrix - ideal_best, axis=1)
    distance_to_worst = np.linalg.norm(weighted_matrix - ideal_worst, axis=1)

    # Relative closeness to the ideal solution
    closeness = distance_to_worst / (distance_to_best + distance_to_worst)

    return closeness.tolist()