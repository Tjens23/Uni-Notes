---
tags:
  - Notes
links: "[[Math Lecture 3]]"
creation date: 2024-11-27 16:03
modification date: Wednesday 27th November 2024 16:03:45
semester: 3
year: 2024
---


---
# [[Math Lecture 3 Notes]]

---



# Introduktion til Vektor 2D $\vec{v}$
- Vektorer er en pil, der har en retning og er bestående af Matrisser.
	- (En) Vektor i 2D strækker sig mellem to punkter.
	- (En) Vektor har en længde, defineret udefra strækningen mellem de to vektorer.
	- Vektorer annoteres med en pil over bogstavet, som fx: $\vec{v}$


## Længden af Vektoren $|\vec{v}|$

- Vi ved på forhånd, at en Vektor har en Retning, og består af Matrisser.
- Vi kan se, at ved en tredimensionel vektor har vi 3 værdier.

$$\vec{v}=\begin{bmatrix}x\\y\\z\end{bmatrix}$$

- Vi kan se, at ved en todimensionel vektor har vi 2 værdier.

$$\vec{v}=\begin{bmatrix}x\\y\end{bmatrix}\in R^2$$

- Hvis vi skal udregne længden af en vektor, skal vi bare tage kvadratroden af en vektor, derved fås længden.


| Længden af Vektor 3D                                                                                                                                    | Længden af vektor 2D                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| $\|\vec{v}\|=\sqrt{\begin{bmatrix}x\\y\\z \end{bmatrix}}=\sqrt{\begin{bmatrix}a\\b\\c \end{bmatrix}}=\sqrt{\begin{bmatrix}v_1\\v_2\\v_3 \end{bmatrix}}$ | $\|\vec{v}\|=\sqrt{\begin{bmatrix}x\\y\end{bmatrix}}=\sqrt{\begin{bmatrix}a\\b\end{bmatrix}}=\sqrt{\begin{bmatrix}v_1\\v_2\end{bmatrix}}$ |

- Når vi skal udregne det i en formel, kan vi skrive følgende.



$$|\vec{v}|=\sqrt{x^{2}+y^{2}+z^{2}+\dots n^2}$$

$$||\vec{v}||=\sqrt{v_{1}^{2}+v_{2}^{2}+v_{2}^{2}}+v_{i}^{2}$$


## Addition $(\vec{𝒗} + \vec{𝒖})$ og Skalering $(a\cdot \vec{𝒗})$

- Når vi lægger to Vektorer sammen er det defineret på følgende måde:

$$\begin{bmatrix}a_1\\a_2\\a_3\end{bmatrix}^{R^{n}}+\begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}^{R^{n}}$$


- Når vi skalerer en Vektor, ganger vi en skaleringsværdi på følgende:

$$a\cdot \vec{v}=\begin{bmatrix}a\cdot v_{1}\\a\cdot v_{2}\\ a\cdot v_3 \end{bmatrix}$$

## Vektor Space

- Det er vigtigt, at have et startpunkt eller orgin.
- Hvis man tager et eller andet Vektor Space, så skal den have 3 assumptioner.
- Det betyder, at additionen af Vektor skal ligge inden for en defineret Vektor Space.



## Lineære Vektorer

- Når vi snakker om Skalering af Vektorer, plejer vi at skrive på følgende måde:


$$a_{1}\cdot u_{1} + a_{2} \cdot u_{1}+ a_{1}+u_{1}$$

- Hvad er Lineære Independence?
	- Eksempelvis hvis en Linære Kombination er 0, så skal alle Linære Kombinationer være 0.
	- Men hvis man har (en enkelt) Linære Kombination er 0, og de andre
	- Kombination er eksempelvis 1, så er der snak om at ligningen er IKKE Lineare Independent ved Summen.



## Prikproduktet & Multiplikation i Vektor Space

$$
u= \begin{bmatrix}3\\5\\6\end{bmatrix}
\quad
v= \begin{bmatrix}1\\-1\\2\end{bmatrix}
$$




- Nu udregnes Prikproduktet:

$$u \cdot v = 3\cdot 1 + 5 \cdot (-1) + 6 \cdot 2 = 10$$
- Som det kan ses, så er Resultat 10 kaldt for en Skalar.




