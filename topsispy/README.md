# topsispy

**topsispy** is a Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on decision matrices.

## Installation

Install **topsispy** using `pip`:

```bash
pip install topsispy
```

## Usage
```
from topsispy.topsis import topsis

# Example decision matrix
matrix = [
    [250, 16, 12, 4],
    [200, 8, 15, 2],
    [300, 20, 10, 5],
    [275, 18, 18, 3]
]

weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '+', '-']

result = topsis(matrix, weights, impacts)

# Output the TOPSIS scores
print("TOPSIS Scores:", result)
```

Adjust the matrix, weights, and impacts based on your specific use case.


## Dependencies

Numpy:[Numpy Official Website](https://numpy.org/)
