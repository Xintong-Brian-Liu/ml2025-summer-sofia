import numpy as np
from sklearn.metrics import precision_score, recall_score

n = int(input("Enter N: "))

x_vals = np.zeros(n, dtype=int)
y_vals = np.zeros(n, dtype=int)

for i in range(n):
    x = int(input(f"Enter x value for point {i+1}: "))
    y = int(input(f"Enter y value for point {i+1}: "))
    x_vals[i] = x
    y_vals[i] = y

precision = precision_score(x_vals, y_vals)
recall = recall_score(x_vals, y_vals)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
