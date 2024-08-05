#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# Transition probability matrices for each stock
transition_matrices = {
    'TCS': np.array([
        [0.388889, 0.055556, 0.555556],
        [0.0, 0.0, 1.0],
        [0.647059, 0.0, 0.352941]
    ]),
    'INFOSYS': np.array([
        [0.5, 0.05, 0.45],
        [1.0, 0.0, 0.0],
        [0.571429, 0.071429, 0.357142]
    ]),
    'WIPRO': np.array([
        [0.428571, 0.428571, 0.142857],
        [0.583333, 0.166667, 0.25],
        [0.1, 0.4, 0.5]
    ]),
    'HCL': np.array([
        [0.375, 0.0625, 0.5625],
        [0.714286, 0.285714, 0.0],
        [0.384615, 0.307692, 0.307692]
    ])
}

# Initial state vectors
initial_states = {
    'TCS': np.array([0.5, 0.027778, 0.472222]),
    'INFOSYS': np.array([0.555556, 0.055556, 0.388889]),
    'WIPRO': np.array([0.388889, 0.333333, 0.277778]),
    'HCL': np.array([0.444444, 0.194444, 0.361111])
}

# Function to predict the next states using the Markov model
def predict_next_states(initial_state, transition_matrix, steps):
    current_state = np.array(initial_state)
    predictions = [current_state]
    for _ in range(steps):
        current_state = np.dot(current_state, transition_matrix)
        predictions.append(current_state)
    return predictions

# Number of steps to predict
steps = 6

# Predictions for each stock
for stock, transition_matrix in transition_matrices.items():
    initial_state = initial_states[stock]
    predictions = predict_next_states(initial_state, transition_matrix, steps)
    
    print(f"Predictions for {stock}:")
    for i, state in enumerate(predictions):
        print(f"Month {i+1}: Bull = {state[0]:.6f}, Stagnant = {state[1]:.6f}, Bear = {state[2]:.6f}")
    print()


# In[ ]:




