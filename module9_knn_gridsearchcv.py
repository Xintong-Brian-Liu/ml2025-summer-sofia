#!/usr/bin/env python3

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

def read_dataset(dataset_name, size):
    print(f"\nEntering {dataset_name} data:")
    
    X = np.zeros(size, dtype=np.float64)
    y = np.zeros(size, dtype=np.int32)
    
    for i in range(size):
        print(f"Pair {i+1}:")
        x_val = float(input(f"  Enter x value: "))
        y_val = int(input(f"  Enter y value (class label): "))
        
        if y_val < 0:
            raise ValueError("Class label (y) must be a non-negative integer")
        
        X[i] = x_val
        y[i] = y_val
    
    X = X.reshape(-1, 1)
    return X, y

def find_optimal_k_with_gridsearch(X_train, y_train):
    param_grid = {'n_neighbors': list(range(1, 11))}
    knn = KNeighborsClassifier()
    cv_folds = min(5, len(X_train))
    
    grid_search = GridSearchCV(
        estimator=knn,
        param_grid=param_grid,
        cv=cv_folds,
        scoring='accuracy',
        n_jobs=-1,
        verbose=0
    )
    
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_['n_neighbors'], grid_search.best_estimator_

def main():
    print("k-NN Classification with Grid Search Cross-Validation")
    print("=" * 55)
    
    try:
        print("\n1. Reading Training Set")
        N = int(input("Enter the number of training samples (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer")
        
        X_train, y_train = read_dataset("training set", N)
        
        print("\n2. Reading Test Set")
        M = int(input("Enter the number of test samples (M): "))
        if M <= 0:
            raise ValueError("M must be a positive integer")
        
        X_test, y_test = read_dataset("test set", M)
        
        print("\n3. Finding Optimal k using Grid Search Cross-Validation")
        print("   Testing k values from 1 to 10...")
        
        best_k, best_estimator = find_optimal_k_with_gridsearch(X_train, y_train)
        
        y_pred = best_estimator.predict(X_test)
        test_accuracy = accuracy_score(y_test, y_pred)
        
        print("\n" + "=" * 55)
        print("RESULTS:")
        print("=" * 55)
        print(f"Best k value: {best_k}")
        print(f"Test accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
        print("=" * 55)
        
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
