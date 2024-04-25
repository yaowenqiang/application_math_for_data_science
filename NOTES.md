Why Learn Calculus and Functions

+ Understanding functions, including their derivatives and integrals, are fundamental to machine learning, probability, and statics.
+ Deep learning and neural networks are often trained by backpropagation and gradient descent, both of which are Calculus-driven
+ Having a grasp of numeric systems will make it easier to interpret and scrutinize models and graphs
+

derivative and partial derivative(导数和偏导数)
gradient descent(梯度下降)
integral(积分)
number theory(数论)
rational number(有理数)
irrational number(无理数)
real number(实数)
complex/imaginary number(虚数)

# variable

In mathematics, a variable is a named placeholder for an unspecified or unknown number.


# Functions

Functions are expressions that define relationships between two or more variables

More specifically a function takes independent variables (also called domain variables or input variables), plugs them into an expression, and then result in a dependent variable(also called an output variable)


# 3d functions and Beyond

f(x,y) = 2x + 3y


# Exponential and Logarithmic Functions(指数函数和对数函数)

Euler's Number(欧拉数)

# Derivatives(导数)

A derivative tells the slop of a function, and it is useful to measure the rate of change at any point in a function.

## partial derivative(偏导数)
## Gradient Descent(梯度下降)
## multivariable gradient descent(多变量梯度下降)

## Saddle point(鞍点)

## Integral(积分)

## reimann sum(黎曼和)


# Linear Algebra(线性代数)

## Why learn linear algebra

+ Linear algebra can be found in many areas of science, technology, engineering, and data science.
+ Computers can more effciently model data as vectors and matrices and perform operations more effectively
+ It is also the backbone of machine learning, data management, graphical modeling, and other computer science areas.
+ If you want to advance your knowledge in machine, statistical modeling, or other areas in computer science then linear algebra is a must!

## Vector(向量)

What Are Vectors? 

Vectors are an arrow in space, with a specific direction and length

This can mean different things in different disciplines.

+ Physics - Direction and magnitude
+ Computer science - An array of numbers storing data
+ Math - a direction and scale on an XY plane.


We can think of a two-dimensional vector as a pair of numbers.

$$ \vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix} $$

we specify a vector with the name  $$ \vec{v}$$ and from the origin(0,0) we make 3 steps along the x-axis and 4 steps up the y-axis.

Think of vectors as more than a data point, it's a movement hence its representation as an arrow

Vectors must start at the origin(0,0) and cannot arbitrarily start at any point in space.

## 3D vectors and Beyond

$$
\vec{v} = \begin{bmatrix}
4 \\
1\\
2
\end{bmatrix}
$$

## Adding/Combining Vectors

$$
\vec{v} + \vec{w} = \begin{bmatrix}
3\\
2\\
\end{bmatrix} +  \begin{bmatrix}
2\\
-1\\
\end{bmatrix} = \begin{bmatrix}
4\\
1\\
\end{bmatrix}
$$

## Subtracting Vectors

$$
\vec{v} - \vec{w} = \begin{bmatrix}
3\\
2\\
\end{bmatrix} -  \begin{bmatrix}
1\\
3\\
\end{bmatrix} = \begin{bmatrix}
2\\
-1\\
\end{bmatrix}
$$

## Multiplying/Scaling vectors

$$
\vec{v}  = \begin{bmatrix}
3\\
1\\
\end{bmatrix} 
$$
$$
2\vec{v} = 2\begin{bmatrix}
3\\
1\\
\end{bmatrix} = 
 \begin{bmatrix}
6\\
2\\
\end{bmatrix}
$$

$$
.5\vec{v} = .5\begin{bmatrix}
3\\
1\\
\end{bmatrix} = 
 \begin{bmatrix} 1.5\\ .5\\ \end{bmatrix}
$$

When you multipy/scale a vector with a negative number, it will flip the vector in the opposite direction.

> Note that multipying/scaling a vector only grows or shrinks a vector
>
> Scaling does not change a vector's direction except for a negative scalar which flips its direction

$$
\vec{v} = \begin{bmatrix} 3\\2\end{bmatrix}
$$

$$
-1.5\vec{v} = -1.5\begin{bmatrix} 3\\2\end{bmatrix} = \begin{bmatrix} -4.5\\-3\end{bmatrix}
$$


$$
\begin{bmatrix} x\\y\end{bmatrix} = \begin{bmatrix}
2&0\\0&3
    \end{bmatrix} \begin{bmatrix} 2\\1\end{bmatrix}
$$

$$
\begin{bmatrix} x\\y\end{bmatrix} = \begin{bmatrix}
(2)(2)+(0)(1)\\(2)(0)+(3)(1)
    \end{bmatrix} 
$$
$$
\begin{bmatrix} x\\y\end{bmatrix} = \begin{bmatrix} 4\\3\end{bmatrix}
$$


## Matrix vector multiplication formula:

$$
\begin{bmatrix} x_new\\ y_new \end{bmatrix}  =  \begin{bmatrix} a & b \\ c & d \\ \end{bmatrix}  \begin{bmatrix} x \\ y\end{bmatrix}
$$

$$
\begin{bmatrix} x_new\\ y_new \end{bmatrix}  =  \begin{bmatrix} ax + by \\ cx + dy \\ \end{bmatrix} 
$$

$$
\vec{w} = \begin{bmatrix} -.25 & 0 \\0 & -1 \end{bmatrix} \begin{bmatrix} 4\\2\end{bmatrix} =  \begin{bmatrix} (-.25)(4) + (0)(2) \\ (4)(0) + (-1)(2) \\ \end{bmatrix}  $$
$$
\vec{w} = \begin{bmatrix} -1 \\ -2 \end{bmatrix}
$$


## Matrix Multiplication(矩阵乘法)

$$
\vec{v} = \begin{bmatrix} 3\\2\end{bmatrix}
$$

$$
$$


## The Determinant(行列式)

The determinant of a matrix is a scalar value that can be computed by multiplying the elements in a particular way.

The determinant of a 2x2 matrix is a small number that can be computed by multiplying the elements in a particular way.

The determinant of a 3x3 matrix is a small number that can be computed by multiplying the elements in a particular way.

The determinant of a 4x4 matrix is a small number that can be computed by multiplying the elements in a particular way.


Determinants describe how much a sampled area in a vector space changes in scale with linear transformations, and this can help provide helpful information about the transformation.


## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)

## Matrix Determinant(矩阵行列式)
$$

## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)

## Matrix Determinant(矩阵行列式)
$$

## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)
$$

## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)
$$
## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)
$$


## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)

## Vector Norm(向量范数)

A vector norm is a function that maps a vector to a scalar value.

The most common vector norms are the Euclidean norm, the Manhattan norm, and the Minkowski norm.

## Vector Space(向量空间)

## Matrix(矩阵)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)

## Matrix Determinant(矩阵行列式)

## Matrix Trace(矩阵迹)

## Matrix Rank(矩阵秩)

## Matrix Diagonalization(矩阵对角化)

## Matrix Eigenvalue(矩阵特征值)

## Matrix Eigenvector(矩阵特征向量)

## Vector Space(向量空间)

## Vector Norm(向量范数)

## Matrix(矩阵)

## Vector(向量)

## Matrix Multiplication(矩阵乘法)

## Matrix Inverse(矩阵求逆)

## Matrix Transpose(矩阵转置)

## Matrix Determinant(矩阵行列式)

## Matrix Trace(矩阵迹)

## Matrix Rank(矩阵秩)

## Matrix Diagonalization(矩阵对角化)

## Matrix Eigenvalue(矩阵特征值)

## Matrix Eigenvector(矩阵特征向量)

# Probability

Why learn probability


Probability is the building block to statistics, machine learning, data science, engineering, and several other  disciplines.

It is common to have to make decisions with limitted information, as a matter of act, this is most decisions we make.

Probability anables us to measure how certain we are in an outcome occuring and while this is an imperfect art, it can be immensely valuable.


## Monty Hall Problem(蒙提霍尔问题)



$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

$$
P(P1|D2) = \frac{P(D1|P1)P(P1)}{P(D2)} = \frac{(.5)(.33)}{(.5)}
$$

$$
P(P2|D2) = \frac{P(D2|P2)P(P2)}{P(D2)} = \frac{(1)(.33)}{.5} = .66
$$




## joint probabilities(联合概率)


## bayes theorem (贝叶斯定理)

## Binomial Distribution(二项分布) and Beta Distribution(和贝塔分布)

# statistics and hypothesis testing(统计学和假设检验)

## descriptive statistics(描述性统计学)
## inferential statistics(推论统计学)

+ Population(总体)
+ Parameter(参数)
+ Sample(样本)