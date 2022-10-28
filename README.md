# Differential Equation Solver

In this repository I am going to explore some techniques to solve some differential equations, first `Ordinary Differential Equations` (ODEs) and then `Partial Differential Equations` (PDEs).

## What is a differential equation?

A differential equation is any equation that involves derivatives and functions, the simplest example is the equation:

$$
\begin{align*}
\frac{dy}{dx} = f(x) \ \ \ x \in \R
\\ y(a) = b \ \ \ a \in \R
\end{align*}
$$

which has the solution:

$$y-b = \int^{x}_{a} f(x)dx$$

The first type of equations I will focus on is ODEs, these are differential equations of **one** variable. These equations can have an `order` and a `linearity`. The order of an ODE is the highest order derivative within the equation - $\frac{d^ny}{dx^n} = x$ has order n. An ODE is linear if the `coefficients` of the dependent variable are scalars, further if the dependent variable is not in an `affine` function. $(\frac{dy}{dx})^2 = f(x)$ is non linear. Further an ODE can be `homogenous` meaning that an equation that is only a function of the dependent variable is `homogenous` such as $\frac{dy}{dx} - y = 0$, whereas $\frac{dy}{dx} = x$ is not.
