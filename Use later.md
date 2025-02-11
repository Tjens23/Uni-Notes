
## Matrix Multiplication

$\vec{a} = \begin{pmatrix} 2 & 5 & 6 \end{pmatrix}$ 

$\vec{b} = \begin{pmatrix} 3 \\ 4 \\ -5 \end{pmatrix}$

- Order matters when dealing with matrices 
	- $\vec{a} \neq \vec{b}$
- AB tells us that $\vec{a} \cdot \vec{b}$ 
	- BA tells us that: $\vec{b} \cdot \vec{a}$
- Order of a matrix:
	- start with counting rows then columns
		- Fx: $\vec{a}$ has 1 row and 3 columns so it's a 1x3  matrix
		- and $\vec{b}$ has 3 rows and 1 column so it's a 3x1 matrix
	- The number of columns in the first matrix must equal the number of rows in the second matrix
		-  in order to multiply vector a with vector b, vector b must have 3 rows
		- the order of the matrix is going to be the product of row of vector a and column of vector b, which do not have to be the same
			- Order of the matrix $\vec{a} \cdot \vec{b}$ is going to be a 1x1 matrix
			- Order of the matrix $\vec{b} \cdot \vec{a}$ is going to be a 3x3 matrix


### Calculation

- row $\cdot$ column


$\vec{a} \cdot \vec{b} = \begin{pmatrix}2(3)+5(4)+6(-5)\end{pmatrix} \leftrightarrow \begin{pmatrix}6+20-30\end{pmatrix} \leftrightarrow \begin{pmatrix}26-30\end{pmatrix}\leftrightarrow \begin{pmatrix}-4\end{pmatrix}$

$\vec{b_{row1}}\cdot\vec{a_{row1}} = \begin{pmatrix}3(2)+3(5)+3(6)\end{pmatrix} \leftrightarrow \begin{pmatrix}6 & 15 & 18\end{pmatrix}$

$\vec{b_{row2}}\cdot\vec{a_{row2}} = \begin{pmatrix}4(2)+4(5)+4(6)\end{pmatrix} \leftrightarrow \begin{pmatrix}8 & 20 & 24\end{pmatrix}$

$\vec{b_{row3}}\cdot\vec{a_{row3}} = \begin{pmatrix}-5(2)-5(5)-5(6)\end{pmatrix} \leftrightarrow \begin{pmatrix}-10 & -25 & -30\end{pmatrix}$

$\vec{b}\cdot\vec{a}=\begin{pmatrix}6 & 15 & 18 \\ 8 & 20 & 24 \\ -10 & -25 & -30 \end{pmatrix}$



### Example

$\vec{a}=\begin{pmatrix}1 & 4 & -2 \\ 3 & 5 & -6\end{pmatrix} \rightarrow 2x3$


$\vec{b}=\begin{pmatrix}5 & 2 & 8 & -1 \\ 3 & 6 & 4 & 5 \\ -2 & 9 & 7 & -3\end{pmatrix} \rightarrow 3x4$


Since $\vec{a}$ is a 2x3 matrix and  $\vec{b}$ is a  3x4 matrix we cannot  multiply $\vec{b}\cdot\vec{a}$, however we can multiply $\vec{a} \cdot \vec{b}$ because the number of columns in $\vec{a}$ is equal to the number of rows in $\vec{b}$

$\vec{a_{row1}}\cdot\vec{b_{row1}}=\begin{pmatrix}1(5)+4(3)+(-2)(-2) & 1(2) + 4(6) + (-2)(9) & 1(8) + 4(4) + (-2)(7) & 1(-1) + 4(5) + (-2)(-3)\end{pmatrix} \leftrightarrow \begin{pmatrix}21 & 8 & 10 & 25\end{pmatrix}$
$\vec{a_{row2}}\cdot\vec{b_{row2}}=\begin{pmatrix}3(5)+5(3)+(-6)(-2) & 3(2) + 5(6) + (-6)(9) & 3(8) + 5(4) + (-6)(7) & 3(-1) + 5(5) + (-6)(-3)\end{pmatrix} \leftrightarrow \begin{pmatrix}42 & -18 & 2 & 40\end{pmatrix}$
$\vec{a}\cdot\vec{b}=\begin{pmatrix}21 & 8 & 10 & 25 \\ 42 & -18 &  2 & 40\end{pmatrix}$


## Fraction Addition

- multiply denominator
- multiply cross over (see example)
### Example

$\frac{3}{5} + \frac{4}{7} = \frac{7\cdot3+5\cdot4}{7\cdot5} \leftrightarrow \frac{21+20}{35}\leftrightarrow\frac{41}{35}$
