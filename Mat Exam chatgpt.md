---
tags:
  - Notes
links: 
creation date: 2025-02-17 08:01
modification date: Monday 17th February 2025 08:01:39
semester: 4
year: 2025
---


---
# [[Mat Exam chatgpt]]

---

# Opgave 1

## a) Anvend Gauss-elimination til at løse følgende ligningssystem:

$$2x+y-z=5,\quad x-2y+3x=-2,\quad 3x+y+z=4$$



$$\left[\begin{array}{rrr|r}2&1&-1&5\\1&-2&3&-2\\3&1&1&4\end{array}\right]$$


$$\frac{R_1}{2}\rightarrow R_1$$

$$\left[\begin{array}{rrr|r}1&\frac{1}{2}&-\frac{1}{2}&\frac{5}{2}\\1&-2&3&-2\\3&1&1&4\end{array}\right]$$

$$R_2-1 \cdot R_1$$


$$\left[\begin{array}{rrr|r}1&\frac{1}{2}&-\frac{1}{2}&\frac{5}{2}\\0&-2.5&3.5&-4.5\\3&1&1&4\end{array}\right]$$


$$R_3-3 \cdot R_1$$
$$\left[\begin{array}{rrr|r}1&\frac{1}{2}&-\frac{1}{2}&\frac{5}{2}\\0&-2.5&3.5&-4.5\\0&-0.5&2.5&-3.5\end{array}\right]$$

$$R_1-0.5\cdot R_2$$



## b Givet vektorerne:

$$\vec{a}=\begin{bmatrix}2\\1\\-1\end{bmatrix}, \quad \vec{b}=\begin{bmatrix}1\\-3\\2\end{bmatrix}$$

Find en $\vec{c}, der er vinkelret på vektorerne, som har en positiv z-komponent.



![[Pasted image 20250217081905.png]]


$$1\cdot2-(-1)\cdot (-3)=2-3=-1$$
$$-1\cdot1-2\cdot2=-5$$
$$2\cdot(-3)-1\cdot1=-7$$

$$\vec{v}=\begin{bmatrix}-1\\-5\\-7\end{bmatrix}$$
$$-1\cdot\vec{v}=\begin{bmatrix}1\\5\\7\end{bmatrix}$$

## **c)** Bestem vinklen mellem vektorerne a og bb, der blev introduceret i opgave 1b. Angiv vinklen i grader.


![[Pasted image 20250217083346.png]]






$$\vec{a}=\begin{bmatrix}2\\1\\-1\end{bmatrix}, \quad \vec{b}=\begin{bmatrix}1\\-3\\2\end{bmatrix}$$


$$\vec{a}\cdot\vec{b}=2\cdot1+1\cdot(-3)-1\cdot2=3-3-2=-2$$

$$|\vec{a}|=\sqrt{x^2+y^2+z^2}$$
$$=\sqrt{2^2+1^2-1^2}$$
$$=\sqrt{4+1-1}$$
$$=\sqrt{4}$$
$$=2$$


$$|\vec{b}| = \sqrt{1^2 + (-3)^2 + 2^2} = \sqrt{1 + 9 + 4} = \sqrt{14}$$

$$cos(\theta)=arccos(\frac{-2}{2\cdot\sqrt{14}})\cdot\frac{180}{\pi}=105.50$$


# Opgave 2

