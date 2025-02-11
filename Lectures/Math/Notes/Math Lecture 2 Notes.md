---
tags:
  - Notes
links: "[[Math Lecture 2]]"
creation date: 2024-11-13 16:18
modification date: Wednesday 13th November 2024 16:18:10
semester: 3
year: 2024
---


---
# [[Math Lecture 2 Notes]]

---


# Intro til Matrisser

- Matrisser eller matrix er et sæt af tal som er arrangeret i rækker og kolonner som er med til at denne en rektangulært array
	- Tallene som er placeret inde i matrissen er kaldt for elementer eller "entries" af matrissen.
- Størrlsen af matrissen kan ses på forholdet mellem rækker og kolonner som følgende $|r\quad x \quad c|$


## Transpose af matrisser $M^T$

- Transpose af matrisser betyder at konvertere rækkerne om til kolonnerne på den samme matrisse.


### Eksempel

$$A=\begin{bmatrix}a&b\\c&d\\e&f\end{bmatrix}$$

$$A^T=\begin{bmatrix}a&c&e\\b&d&f\end{bmatrix}$$



$$B=\begin{bmatrix}3&4&6\\8&7&5\end{bmatrix}$$


$$B^T=\begin{bmatrix}3&8\\4&7\\6&5\end{bmatrix}$$

$$C=\begin{bmatrix}3\\7\\8\end{bmatrix}$$


$$C^T=\begin{bmatrix}3&7&8\end{bmatrix}$$



## Addition mellem matrisser

- **OPS: ADDITION MELLEM MATRISSERNE ER KUN MUGLIGT BLANDT MATRISSER SOM ER LIGE I BÅDE ANTALL RÆKKER OG KOLONNER**


## Eksempel

$$A=\begin{bmatrix}-3&-4\\5&6\end{bmatrix}$$
$$B=\begin{bmatrix}4&-4\\-5&2\end{bmatrix}$$


$$A+B=\begin{bmatrix}-3&-4\\5&6\end{bmatrix}+\begin{bmatrix}4&-4\\-5&2\end{bmatrix}=\begin{bmatrix}-3+4&-4+(-4)\\5+(-5)&6+2\end{bmatrix}=\begin{bmatrix}1&-8\\0&8\end{bmatrix}$$


## Produkt mellem matrisser

$$
\begin{bmatrix}\color{red}a&\color{red}b\\c&d\end{bmatrix}
\quad
\begin{bmatrix}\color{green}p&q\\\color{green}r&s\end{bmatrix}
$$

$$
\begin{bmatrix}\color{red}a&\color{red}b\\c&d\end{bmatrix}
\quad
\begin{bmatrix}p&\color{green}q\\r&\color{green}s\end{bmatrix}
$$


$$
\begin{bmatrix}a&b\\\color{red}c&\color{red}d\end{bmatrix}
\quad
\begin{bmatrix}\color{green}p&q\\\color{green}r&s\end{bmatrix}
$$

$$
\begin{bmatrix}a&b\\\color{red}c&\color{red}d\end{bmatrix}
\quad
\begin{bmatrix}p&\color{green}q\\r&\color{green}s\end{bmatrix}
$$


$$C=\begin{bmatrix}a\cdot p+b\cdot r&a\cdot q+b\cdot s\\c\cdot p + d\cdot r & c\cdot q +d\cdot s\end{bmatrix}$$


## Determinanten til matrisser $det(S) / |S|$

- Når man arbejder med algortmers stabilitet i machine learning. ønskes der en stabilitet blandt dataene
- Når man laver analyse på stabillitet, så ønskes det at determinanten skal $\textbf{ IKKE}$ være 0.


### Steps til udregning af determinant i 2D

- Co-factor
- Ignorere de samme kolonner og rækker
- find endelige determinant


### Step 1: Find  Co-factor

- Co-factoren beyder at finde  foretegn, baseret på de elementer som kan står i række 1 i matrissen. 
- Co-fac












## Inserse for 2D matrisser

