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
\begin{bmatrix}\color{lime}p&q\\\color{lime}r&s\end{bmatrix}
$$

$$
\begin{bmatrix}\color{red}a&\color{red}b\\c&d\end{bmatrix}
\quad
\begin{bmatrix}p&\color{lime}q\\r&\color{lime}s\end{bmatrix}
$$


$$
\begin{bmatrix}a&b\\\color{red}c&\color{red}d\end{bmatrix}
\quad
\begin{bmatrix}\color{lime}p&q\\\color{lime}r&s\end{bmatrix}
$$

$$
\begin{bmatrix}a&b\\\color{red}c&\color{red}d\end{bmatrix}
\quad
\begin{bmatrix}p&\color{lime}q\\r&\color{lime}s\end{bmatrix}
$$


$$C=\begin{bmatrix}a\cdot p+b\cdot r&a\cdot q+b\cdot s\\c\cdot p + d\cdot r & c\cdot q +d\cdot s\end{bmatrix}$$


## Determinanten til matrisser $det(S) / |S|$

- Når man arbejder med algortmers stabilitet i machine learning. ønskes der en stabilitet blandt dataene
- Når man laver analyse på stabillitet, så ønskes det at determinanten skal $\textbf{ IKKE}$ være 0.


### Udregning af determinant i 2D

Når man har to vektorer kan man finde deres determinant. Man får determinanten ved at hatte den første vektor og prikke med den anden.

$$det(\vec{a}, \vec{b})=\vec{a} \cdot \vec{b} = a_{1}\cdot b_2-a_{2}\cdot b_1$$

Der findes to måder at notere determinanten på. Enten ved at skrive _det_ eller også ved at skrive de to vektorers koordinater op i et skema som vist nedenfor. Her betyder de lodrette streger altså hverken "længde" eller "numerisk værdi" men i stedet "determinant".

$$det(\vec{a}, \vec{b})=\begin{bmatrix}a_1&a_2\\b_1&b_2\end{bmatrix}$$
Hvis man skriver determinanten op på den sidste måde, er den let at regne ud. Man skal nemlig bare gange over kryds.

Først ganger man øverste venstre med nederste højre, hvorfra man trækker nederste venstre ganget med øverste højre.

$$\begin{bmatrix}\color{red}a_1&\color{lime}a_2\\\color{lime}b_1&\color{red}b_2\end{bmatrix}=\color{red}a_{1}\color{white}\cdot \color{red}b_2\color{white}-\color{lime}a_2\color{white}\cdot\color{lime}b_1$$
#### F.eks. 

$$\vec{a}=\begin{pmatrix}3\\2\end{pmatrix}\quad \vec{b}=\begin{pmatrix}1\\5\end{pmatrix}$$

$$det(\vec{a}, \vec{b})=\begin{bmatrix}3&1\\2&5\end{bmatrix}=3\cdot5-2\cdot1=15-2=13$$







### Udregning af determinant i 3D

$$det(\begin{bmatrix}x_1&y_1&z_1\\x_2&y_2&z_2\\x_3&y_3&z_3\end{bmatrix})=x_1\cdot\begin{bmatrix}y_2&z_2\\y_3&z_3\end{bmatrix}-y_1\cdot\begin{bmatrix}x_2&z_2\\x_3&z_3\end{bmatrix}+z_1\cdot\begin{bmatrix}x_2&y_2\\x_3&y_3\end{bmatrix}$$

#### F.eks.

$$\vec{a}=\begin{bmatrix}2&4&-3\\5&7&6\\-8&1&9\end{bmatrix}$$

$$det(\vec{a})=2\cdot\begin{bmatrix}7&6\\1&9\end{bmatrix}-4\cdot\begin{bmatrix}5&6\\-8&9\end{bmatrix}-3\begin{bmatrix}5&7\\-8&1\end{bmatrix}$$

$$=2[7\cdot9-6\cdot1]-4[5\cdot9-6\cdot(-8)]-3[5\cdot1+8\cdot7]$$
$$=2[63-6]-4[45+48]-3[61]$$
$$=2\cdot57-4\cdot93-183$$
$$=114-372-183$$
$$=441$$
#### Life hack

Steps:
- Repeat first and second column
- Take the product
- take the sum
- concider the anti diagonal terms
- take the sum
- subtract the two numbers


$$\vec{a}=\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}\quad\begin{array}{cc}j&k\\l&m\\n&o\end{array}$$

Take the product

 $$\begin{bmatrix}\color{lime}a&\color{yellow}b&\color{cyan}c\\d&\color{lime}e&\color{yellow}f\\g&h&\color{lime}i\end{bmatrix}\quad\begin{array}{cc}j&k\\\color{cyan}l&m\\\color{yellow}n&\color{cyan}o\end{array}$$

take the sum
$$x=a+e+i + b+f+n + c+l+o$$



concider the anti diagonal terms

$$\begin{bmatrix}a&b&\color{lime}c\\d&\color{lime}e&\color{yellow}f\\\color{lime}g&\color{yellow}h&\color{cyan}i\end{bmatrix}\quad\begin{array}{cc}\color{yellow}j&\color{cyan}k\\\color{cyan}l&m\\n&o\end{array}$$
take the sum:

$$y=c+e+g+j+f+h+k+l+i$$


subtract the two numbers

$$x-y=z$$

#### F.eks:

$$\vec{a}=\begin{bmatrix}2&4&-3\\5&7&6\\-8&1&9\end{bmatrix}$$

Repeat first and second column:

$$\vec{a}=\begin{bmatrix}2&4&-3\\5&7&6\\-8&1&9\end{bmatrix}\quad\begin{array}{cc}2&4\\5&7\\-8&1\end{array}$$

Take the product:

$$2\cdot7\cdot9=126$$
$$4\cdot6\cdot(-8)=-192$$
$$-3\cdot5\cdot1=-15$$

take the sum:

$$126-192-15=-81$$

concider the anti diagonal terms:

$$-3\cdot7\cdot(-8)=168$$
$$2\cdot6\cdot1=12$$
$$4\cdot5\cdot9=180$$
take the sum:
$$168+12+180=360$$

subtract the two numbers:
$$-81-360 = -441$$

[lifehack](https://www.youtube.com/watch?v=HRiANm61i0s)

 