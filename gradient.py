import numpy as np
import math

def gradient_function(x, y):
    m_curr = b_current = 0
    iteration = 10000
    learning_rate = 0.08
    n = len(x)
    cost2 = 0
    for i in range(iteration):
        y_predicted = m_curr * x + b_current
        cost = (1/n)*sum(val**2 for val in (y-y_predicted))
        dm = (-2 / n) * sum(x * (y - y_predicted))
        db = (-2 / n) * sum((y - y_predicted))

        m_curr = m_curr - learning_rate * dm
        b_current = b_current - learning_rate * db

        if math.isclose(cost,cost2):
            print(f"m : {m_curr}    b : {b_current}   cost : {cost}  i : {i}")
            break
        cost2 = cost
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_function(x, y)
