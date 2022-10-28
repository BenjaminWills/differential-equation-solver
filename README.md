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

$$y= \int^{x}_{a}f(x)dx + b$$

The first type of equations I will focus on is ODEs, these are differential equations of **one** variable. These equations can have an `order` and a `linearity`. The order of an ODE is the highest order derivative within the equation - $\frac{d^ny}{dx^n} = x$ has order n. An ODE is linear if the `coefficients` of the dependent variable are scalars, further if the dependent variable is not in an `affine` function. $(\frac{dy}{dx})^2 = f(x)$ is non linear. Further an ODE can be `homogenous` meaning that an equation that is only a function of the dependent variable is `homogenous` such as $\frac{dy}{dx} - y = 0$, whereas $\frac{dy}{dx} = x$ is not.

## Euler's Method

Euler's method is a way of numerically solving first order ODES. It takes its approximation from `Taylor Series` (functions that approximate more complex functions using derivatives), where the first order approximation, centered around a, is given by $f(x;a) = f(a) + \left .\frac{df}{dx} \right|_{x=a} (x-a)$, so for values of $|x-a| << 1$ we can actually approximate $f(x)$ using $f(x) \approx f(a) + \left .\frac{df}{dx} \right|_{x=a} (x-a)$ (the tangent line at the point x = a).

Say we are given an ODE:

$$
\begin{align}
\frac{dy}{dx} = f(x,y) \\
y(x_0) = y_0
\end{align}
$$

then we can begin at $x = a$ and approximate to the right.

$$
\begin{align}
\left .\frac{dy}{dx} \right|_{x=x_0} = f(x_0,y_0) \\
y_1 = y_0 + f(x_0,y_0) (x_1-x_0)
\end{align}
$$

This is supposing that $|x_{i+1} - x_i|$ is sufficiently small, thus small interval sizes will lead to more exact solutions. Now we are equipped to write the iterative method.

$$
\begin{align}
y_{i+1} = y_i + f(x_i,y_i) (x_{i+1}-x_i)
\end{align}
$$

Keep in mind that we will keep step sizes constant to simplify the problem, thus $x_{i+1} - x_i = h \ \forall i$. Thus we can state the solution as follows

$$
\begin{align}
y_{i+1} = y_i + f(x_i,y_i) h \\
(x_0,y_0) = (x_0,y(x_0))
\end{align}
$$

One can intuitively see this as drawing multiple tangent lines at even intervals and connecting them at their intersection, when the distance between intervals shrinks the lines become shorter and mirror the shape of the curve more and more.
