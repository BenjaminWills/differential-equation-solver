from typing import Callable
import numpy as np

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

def second_order_euler(function:Callable,position_initial_values:list,velocity_initial_value:float,endpoint:float,num_steps:int,) -> tuple:
    """Solves linear second order ODEs

    Parameters
    ----------
    function : Callable
        RHS of the differential equation (of the form f(x,y,v))
    position_initial_values : list
        a list of position and time.
    velocity_initial_value : float
        a list of velocity and time
    endpoint : float
        Endpoint to plot to
    num_steps : int
        Number of steps

    Returns
    -------
    tuple
        A tuple of the intervals and the y co ordinates of the functions.
    """
    x_0,y_0 = position_initial_values
    v_0 = velocity_initial_value
    step_size = (endpoint - x_0) / num_steps
    x_intervals = np.arange(x_0,endpoint,step_size)
    y_values = [y_0]
    v_values = [v_0]
    for i in range(1,num_steps):
        new_y = y_values[i-1] + v_values[i-1] * step_size
        new_v = v_values[i-1] + function(x_intervals[i-1],y_values[i-1],v_values[i-1]) * step_size
        y_values.append(new_y)
        v_values.append(new_v)
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

