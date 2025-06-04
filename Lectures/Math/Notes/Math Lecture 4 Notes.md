---
tags:
  - Notes
links: "[[Math Lecture 4]]"
creation date: 2024-11-27 16:56
modification date: Wednesday 27th November 2024 16:56:25
semester: 3
year: 2024
---


---
# [[Math Lecture 4 Notes]]

---



# Introduktion til Lineære Ligninger

- Hensigten med Lineære Ligninger er, at kunne bruge dem i sammenhæng med analyse og fortolkning af variabler.
	- Lineære Ligninger der defineret udefra følgende formel:


$$a\cdot x + b  = c$$

- Udefra denne ligning, kan disse værdier omdannes til en samlet Matrisse.
- Den samlede Matrisse er kaldt for en Augmented Matrix 



## Introduktion til Lineære Ligninger


-  vi kan omdanne Lineære Ligninger om til Matrisser på følgende måde:

$$\begin{bmatrix} a_{1,1} & a_{1,2} & a_{1,3}\\ a_{2,1} &a_{2,2}&a_{2,3}\\a_{3,1}&a_{3,2}& a_{3,3}\\a_{n+1}&a_{n+2} & a_{n+3}\end{bmatrix}\cdot\begin{bmatrix}x_1\\x_2\\x_3\\x_n\end{bmatrix}=\begin{bmatrix}b_1\\b_2\\b_3\\b_n\end{bmatrix}$$

- Vi kan se, at værdierne skrives vertikalt i matrisserne og derved er
omskrevet på følgende måde i Lineære Ligninger:


$$A\cdot x = b$$


## Invers af Matrix i Lineære Ligninger

- Vi kan se, at vi skal gange invers af A med både A og B.
	- DET SKAL ALTID SKE BAG VED A-VÆRDIEN!
	- Vi viser her et eksempel:

$$Ax=b\rightarrow A^{-1}\cdot$$




## Back-Substitutionsmetoden

- Back-Substitutionsmetoden  er også kendt som Erstatningsmetoden
- Vi starter med, at arbejde fra 2 ligninger:

$$2y=x+7$$
$$x=y-4$$


- STEP 1: Indsæt x-værdien fra ligning 2 i ligning 1.

$$2y=(y-4)+7$$
$$2y=y-4+7$$
$$2y=y+3$$
$$2y-y=y+3-y \rightarrow y=3$$

- STEP 2: Indsæt den isolerede y-værdi fra ligning 1 i ligning 2.


$$x=y-4$$
$$x=3-4=-1$$

- STEP 3: Opsamle værdierne for Overblik.
$$y=3$$
$$x=-1$$


- STEP 4: Indsæt værdierne i de respektive ligninger.

	- Det betyder, at begge værdier indsættes i Ligning 1 og Ligning 2 således:


$$2y=x+7$$

$$2\cdot3=-1+7=6$$



$$x=y-4$$

$$-1=3-4$$







## Cramers Rule


- Den primære hensigt med Cramers Rule er, at kunne finde x,y,z værdier
- udefra den ”Augmenteret Matrisse”.
- Vi kommer her til at vise, hvordan udregningen foregår når man skal finde det i sammenhæng med inverse af matrisser.
- Vi tager udgangspunkt i det følgende ligning som står nedenfor:



$$3x+3y=1$$
$$4y+4z=3$$
$$2y+1z=0$$
Det er vigtigt, at gøre obs på, at der er ingen forskel i om ligning står ved siden af hinanden eller om på hinanden



### STEP 1: Lav Augmented Matrix

- Vi starter med, at opskrive ligningerne ned for at skabe overblik.

$$3x+3y=1$$
$$4y+4z=3$$
$$2y+1z=0$$


- Nu laver vi Augmented Matrix. X står i kolonne 1, Y står i kolonne 2, og z i kolonne 3.


$$\begin{bmatrix}3&3&0&\big|1\\0&4&4&\big|3\\0&2&1&\big|0\end{bmatrix}$$









## Gaussian Elimination

$$x+y-z=-2$$
$$2x-y+z=5$$
$$-x+2y+2z=1$$



$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
2 & -1 & 1 & \vert & 5 \\
-1 & 2 & 2 & \vert & 1
\end{bmatrix}$$



- Step 1:  få $R_{3,1}$ til at give 0

$$R_{1}+R_3$$

$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
2 & -1 & 1 & \vert & 5 \\
0 & 3 & 1 & \vert & -1
\end{bmatrix}$$



- Step 2: få $R_{2,1}$ til at give 0

$$R_{3} \cdot R_{2} \rightarrow R_2$$

$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
0 & -3 & 3 & \vert & 9 \\
0 & 3 & 1 & \vert & -1
\end{bmatrix}$$


- step 3: få $R_{3,2}$ til at give 0


$$R_3+R_{2} \rightarrow R_3$$

$R_3=(0,3,1,−1)+(0,−3,3,9)=(0+0,3+(−3),1+3,−1+9)$



$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
0 & -3 & 3 & \vert & 9 \\
0 & 0 & 4 & \vert & 8
\end{bmatrix}$$


- Step 4: få $R_{3,3}$ til at give 1


$$\frac{R_{3}}{4}\rightarrow R_3$$



$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
0 & -3 & 3 & \vert & 9 \\
0 & 0 & 1 & \vert & 2
\end{bmatrix}$$

- Step 5: få $R_{2,2}$ til at give 1



$$\frac{R_{2}}{-3}\rightarrow R_2$$


$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
0 & 1 & -1 & \vert & -3 \\
0 & 0 & 1 & \vert & 2
\end{bmatrix}$$


- Step 6: Få   $R_{2,3}$ til at give 0


$$R_2+R_3\rightarrow R_2$$

$$
\begin{bmatrix}
1 & 1 & -1 & \vert & -2 \\
0 & 1 & 0 & \vert & -1 \\
0 & 0 & 1 & \vert & 2
\end{bmatrix}$$


- Step 7: Få $R_{1,3}$ til at give 0
R1​←R1​+R3​



$$
\begin{bmatrix}
1 & 1 & 0 & \vert & 0 \\
0 & 1 & 0 & \vert & -1 \\
0 & 0 & 1 & \vert & 2
\end{bmatrix}$$


- Step 8: Få $R_{1,2}$ til at blive 0


$$R_{1}-R_{2}\rightarrow R_1$$


$$
\begin{bmatrix}
1 & 0 & 0 & \vert & 1 \\
0 & 1 & 0 & \vert & -1 \\
0 & 0 & 1 & \vert & 2
\end{bmatrix}$$

$x=1$, $y=−1$, $z=2$


