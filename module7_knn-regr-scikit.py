import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid real number.")

def main():
    print("k-NN Regression Program")
    print("=" * 25)
    
    # Get input parameters
    N = get_positive_integer("Enter the number of training points (N): ")
    k = get_positive_integer("Enter the number of neighbors (k): ")
    
    # Validate k <= N for k-NN to work
    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N})")
        return
    
    # Initialize training data arrays using NumPy
    X_train = np.zeros((N, 1))  # 2D array for features (required by sklearn)
    y_train = np.zeros(N)       # 1D array for labels
    
    print(f"\nPlease enter {N} training points:")
    
    # Collect training data points
    for i in range(N):
        print(f"Point {i + 1}:")
        x = get_real_number(f"  Enter x value: ")
        y = get_real_number(f"  Enter y value: ")
        
        X_train[i, 0] = x
        y_train[i] = y
    
    # Calculate variance of training labels
    variance = np.var(y_train)
    print(f"\nVariance of labels in training dataset: {variance:.6f}")
    
    # Create and train k-NN regressor
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)
    
    # Get test point and make prediction
    print(f"\nNow enter a test point for prediction:")
    X_test = get_real_number("Enter X value for prediction: ")
    
    # Convert to 2D array format expected by sklearn
    X_test_array = np.array([[X_test]])
    y_predicted = knn_regressor.predict(X_test_array)
    
    print(f"\nResult:")
    print(f"Predicted Y using {k}-NN Regression: {y_predicted[0]:.6f}")

if __name__ == "__main__":
    main()
