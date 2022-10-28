from typing import Callable
import numpy as np

import matplotlib.pyplot as plt

def euler_method(function:Callable,initial_values:list,endpoint:float,num_steps:int,) -> list:
    x_0, y_0 = initial_values
    step_size = (endpoint - x_0) / num_steps
    x_intervals = np.arange(x_0,endpoint,step_size)
    y_values = [y_0]
    for i in range(1,num_steps):
        new_y = y_values[i-1] + function(x_intervals[i-1],y_values[i-1]) * step_size
        y_values.append(new_y)
    return x_intervals,y_values






