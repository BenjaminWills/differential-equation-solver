# Euler's Method

## First Order Equations

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
h = x_{i+1} - x_i\\
(x_0,y_0) = (x_0,y(x_0)) \\
\end{align}
$$

One can intuitively see this as drawing multiple tangent lines at even intervals and connecting them at their intersection, when the distance between intervals shrinks the lines become shorter and mirror the shape of the curve more and more.

NOTE: say that we want to approximate a function on the interval $[x_0,b]$ for some constant $b$, in $n$ intervals, then we can calculate our interval width, $h$ as $h = \frac{b-x_0}{n}$.

## Second Order Equations

This is an equation of the form

$$
\begin{align}
\frac{d^2 y}{d x^2} = f(x,\frac{dy}{dx},y) \\
\left . \frac{dy}{dx} \right|_{x_0} = v_0, \ y(x_0) = y_0
\end{align}
$$

We can reduce the order of this system, by splitting up the derivatives into $v = \frac{dy}{dx}$ then we cab write $(9)$ as the following system of `coupled differential equations`

$$
\begin{align}
\frac{dv}{dx} = f(x,v,y) \\
v = \frac{dy}{dx}
\end{align}
$$

In this case we can simply apply eulers method to both $(11)$ and $(12)$ simultaneously.

$$
\begin{align}
y_{i+1} = y_{i} + v_{i} * h \\
v_{i+1} = v_{i} + f(x_i,y_i,v_i) * h
\end{align}
$$

Eulers method will work for any linear ODE.
