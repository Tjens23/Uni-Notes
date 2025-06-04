---
creation date: 2024-11-27 12:37
modification date: Wednesday 27th November 2024 12:37:10
tags:
  - Assignments
year: 2024
semester: 3
links: "[[Math Lecture 9]]"
---

---
# [[Math Lecture 9 Assignments]]


# Opgave 1 

## a) Løs de to ligninger vist herunder vha. Gauss elimination.


$$\left(\begin{array}{rr|r}5&3&12\\2&5&1\end{array}\right)$$



$$2\cdot(R_1-R_2)\rightarrow R_1$$

$$\left(\begin{array}{rr|r}5-2&3-5&12-1\\2&5&1\end{array}\right) \leftrightarrow \left(\begin{array}{rr|r}3&-2&11\\2&5&1\end{array}\right) \leftrightarrow \left(\begin{array}{rr|r}3-2&-2-5&11-1\\2&5&1\end{array}\right) \leftrightarrow \left(\begin{array}{rr|r}1&-7&10\\2&5&1\end{array}\right)$$



$$\left(\begin{array}{rr|r}1&-7&10\\2&5&1\end{array}\right)$$


$$2\cdot(R_2-R_1)\rightarrow R_1$$

$$\left(\begin{array}{rr|r}1&-7&10\\0&19&-19\end{array}\right)$$

$$\frac{R_2}{19}\rightarrow R_2$$


$$\left(\begin{array}{rr|r}1&-7&10\\0&1&-1\end{array}\right)$$


$$7\cdot(R_1+R_2)\rightarrow R_1$$

$$\left(\begin{array}{rr|r}1&0&3\\0&1&-1\end{array}\right)$$


$x=3$ $y=-1$









## b) Beregn værdien af udtrykket herunder:

$$\begin{pmatrix}5&-1\\3&2\end{pmatrix}\cdot \begin{pmatrix}2&3\\3&2\end{pmatrix}$$

$$\vec{a_{r_1}}=\begin{pmatrix}5\cdot2-1\cdot3\\3\cdot2+2\cdot3\end{pmatrix}\leftrightarrow\begin{pmatrix}7\\12\end{pmatrix}$$


$$\vec{a_{r_2}}=\begin{pmatrix}5\cdot3-1\cdot2\\3\cdot3+2\cdot2\end{pmatrix}\leftrightarrow\begin{pmatrix}13\\13\end{pmatrix}$$
$$\vec{a}\cdot\vec{b}=\begin{pmatrix}7&13\\12&13\end{pmatrix}$$



# Opgave 2

Betragt funktionen $f(x)=ln(x)$

## a) Bestem en tangentlinje for funktionen $f(x)$ omkring punktet $x=1$


tangentes ligning er givet ved:

$$L(x)=f'(x_0)\cdot(x-x_0)+f(x_0)$$

vi ved at: 

$$x_0=1$$
$$f(x)=ln(x)$$
$$f'(x)=\frac{1}{x}$$
$$f'(x_0)= 1$$
Da ln(1) giver 0 får vi:

$$L(x)=1\cdot(x-1)$$
$$=x-1$$

## b) Benyt forskriften for tangentlinjen fra opgave a til at estimere værdien af $f (1.3)$. Beregn fejlen mellem den estimerede værdi og den rigtige værdi $(ln(1.3))$?


$$ln(1.3)=0.2623$$
$$L(1.3)=1\cdot(1.3-1)$$
$$=0.3$$
$$0.3-2623=0,0377$$

## c) Estimer worst case fejlen for estimatet i b).


$$\frac{f''(c)}{2}\cdot(t-x_0)^2$$


hvor c er et punkt mellem $x_0$​ og $x$

Først beregner vi den anden afledte af $f(x)=ln(x)$

$$f'(x)=\frac{1}{x}$$
$$f''(x)=\frac{1}{x^2}$$

For worst case skal vi bruge den maksimale værdi af $|f''(x)|$ ved $x=1$, hvor $|f''(x)|=1$


$$e(t)=\frac{f''(1)}{2}\cdot(1.3-1)^2$$
$$=\frac{1}{2}\cdot(0.3)^2$$
$$=\frac{1}{2}\cdot0.09$$
$$=0.045$$
 $$interval=[0.3-0.045,0.3+0.045]$$

