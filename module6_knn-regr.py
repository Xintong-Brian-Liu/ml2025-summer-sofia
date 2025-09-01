import numpy as np

class KNNRegressor:
    def __init__(self):
        self.x_data = None
        self.y_data = None
        
    def fit(self, x_data, y_data):
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
    
    def predict(self, x_query, k):
        if k > len(self.x_data):
            return None
            
        distances = np.abs(self.x_data - x_query)
        k_nearest_indices = np.argsort(distances)[:k]
        k_nearest_y = self.y_data[k_nearest_indices]
        
        return np.mean(k_nearest_y)

n = int(input("Enter N: "))
k = int(input("Enter k: "))

if k > n:
    print("Error: k cannot be greater than N")
else:
    x_points = np.zeros(n)
    y_points = np.zeros(n)
    
    for i in range(n):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        x_points[i] = x
        y_points[i] = y
    
    knn = KNNRegressor()
    knn.fit(x_points, y_points)
    
    x_query = float(input("Enter X for prediction: "))
    result = knn.predict(x_query, k)
    
    print(f"k-NN Regression result: {result}")
