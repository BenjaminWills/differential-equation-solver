from typing import Callable
import numpy as np

import matplotlib.pyplot as plt

def euler_method(function:Callable,initial_values:list,endpoint:float,num_steps:int,) -> tuple:
    """Solves linear first order ODEs.

    Parameters
    ----------
    function : Callable
        Function on the RHS of the dy/dx
    initial_values : list
        Boundary values for the function
    endpoint : float
        X co ordinate of the end point
    num_steps : int
        Number of steps to take, more = more exact

    Returns
    -------
    tuple
        A tuple of y_values and x_values that have a 1 to 1 correspondence
    """
    x_0, y_0 = initial_values
    step_size = (endpoint - x_0) / num_steps
    x_intervals = np.arange(x_0,endpoint,step_size)
    y_values = [y_0]
    for i in range(1,num_steps):
        new_y = y_values[i-1] + function(x_intervals[i-1],y_values[i-1]) * step_size
        y_values.append(new_y)
    return x_intervals,y_values


def euler_method_error(solution:Callable,function:Callable,initial_values:list,endpoint:float,num_steps:int,) -> tuple:
    """Will calculate the error at each step of the euler method vs the true solution.

    Parameters
    ----------
    solution : Callable
        True solution to ODE
    function : Callable
        Function on the RHS of the dy/dx
    initial_values : list
        Boundary values for the function
    endpoint : float
        X co ordinate of the end point
    num_steps : int
        Number of steps to take, more = more exact.

    Returns
    -------
    tuple
        A tuple of x co-ordinates, and the error at each step
    """
    x_range,numerical_solution = euler_method(function,initial_values,endpoint,num_steps)
    true_solution = [solution(x) for x in x_range]
    error = [abs(true_solution[i] - numerical_solution[i])/true_solution[i] * 100.0 for i in range(num_steps)]
    return x_range,error



