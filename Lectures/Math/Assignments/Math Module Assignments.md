---
creation date: 2024-11-09 15:57
modification date: Saturday 9th November 2024 15:57:11
tags:
  - Assignments
year: 2024
semester: 3
links: "[[Math Lecture 1]]"
---

---
# Math Module Assignments

---


# Matricer, vektorer og ligningssystemer

## Opgave 1


### Opgave 1.1 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.

$$\begin{pmatrix}3&0&4\\-1&2&2\\6&5&-4\end{pmatrix}+\begin{pmatrix}0&2\\2&4\\1&3\end{pmatrix}-\begin{pmatrix}6&1\\-4&7\\-8&3\end{pmatrix}$$

Vi kan ikke lægge matricerne sammen eller trække dem fra hinanden da størrelsen ikke er den samme..



### Opgave 1.2 Skriv et linært ligningssystem, hvis koefficient matrice er

$$\begin{pmatrix}0 & -5 & -3\\ -5 & 2 & 4\\ -3 & 4 & 0\end{pmatrix}$$

$$0_{x}-5_{y}-3x_{z}=k_1$$
$$-5_{x}+2_{y}+4_{z}=k_{2}$$
$$-3_{x}+4_{y}+0_{z}=k_{3}$$

### Opgave 1.3 Differentier og forenkl udtrykket:

$$y=x\cdot e^{-x}-x$$

Produkt reglen:

$$f′(x)⋅g(x)+f(x)⋅g′(x)$$

$$f(x)=x$$
$$g(x)=e^{-x}$$
$$f'(x)=1$$
$$g'(x)=-e^{-x}$$
$$y'= 1 \cdot e^{-x} + x \cdot (-e^{-x}) -1  \leftrightarrow e^{-x}+x\cdot (-e^{-x})-1$$

### Opgave 1.4 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.




$$\begin{pmatrix}
 6& -2 & -2 \\
 10& -3 & 1 \\
 -10 & 5 &1 
\end{pmatrix} \cdot \begin{pmatrix}
 5\\
 1\\2
\end{pmatrix}=\begin{pmatrix}6\cdot5-2*1-2*2\\10*5-3*1+1*2\\-10*5+5*1+1*2\end{pmatrix}\leftrightarrow\begin{pmatrix}24&49&-43\end{pmatrix}$$




### Opgave 1.5 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.

$Row \cdot Column$


$$
\begin{pmatrix}
6 & -2 & -2 \\
10 & -3 & 1 \\
-10 & 5 & 1
\end{pmatrix} \cdot \begin{pmatrix}
9 & 4 & -4 \\
4 & 7 & 0 \\
-4 & 0 & 11 
\end{pmatrix} \leftrightarrow \begin{pmatrix}
 6\cdot  9 -2 \cdot 4 - 2\cdot (-4) & 6 \cdot 4 - 2\cdot 7 -2 \cdot 0 & 6 \cdot (-4) -2 \cdot 0 -2 \cdot 11 \\ 10 \cdot 4 - 3 \cdot 7 + 1 \cdot 0 &
 10 \cdot 9 -3 \cdot 4 + 1 \cdot (-4) & 10 \cdot (-4) -3 \cdot 0 + 1 \cdot 11 \\
 -10 \cdot 9 + 5 \cdot 4 + 1 \cdot (-4) & -10 \cdot 4 + 5 \cdot 7 + 1 \cdot 0 & -10 \cdot (-4) + 5 \cdot 0 + 1 \cdot 11
\end{pmatrix} \leftrightarrow \begin{pmatrix}
 54 & 10 & -46 \\
 74 & 19 & -29 \\
 -74 & -5 & 51
\end{pmatrix}
$$

### Opgave 1.6 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.

$$\begin{pmatrix}
0 & 2 \\
2 & 4 \\
1 & 3
\end{pmatrix}-\begin{pmatrix}
 6 & 1 \\
 -4 & 7 \\
 -8 & 3
\end{pmatrix}\leftrightarrow\begin{pmatrix}
 0-6& 2-1 \\
 2+4& 4-7 \\
 1+8&3-3 
\end{pmatrix}=\begin{pmatrix}
 -6& 1 \\
 6& -3 \\
 9& 0
\end{pmatrix}$$


### Opgave 1.7 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.

kan ikke  


### Opgave 1.8 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.


$$\begin{pmatrix}
6 & 1 \\
-4 & 7 \\
-8 & 3
\end{pmatrix}-\begin{pmatrix}
0 & 2 \\
2 & 4 \\
1 & 3
\end{pmatrix}\leftrightarrow\begin{pmatrix}
6-0 & 1-2 \\
-4-2 & 7-4 \\
-8-1 & 3-3
\end{pmatrix}=\begin{pmatrix}
6 & -1 \\
-6 & 3 \\
-9 & 0
\end{pmatrix}$$


### Opgave 1.9 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.


Kan man ijkke


### Opgave 1.10 Find værdien af følgende udtryk, eller forklar hvorfor de ikke er definerede.

$$\begin{pmatrix}
 6& -2 & -2 \\
 10& -3 & 1 \\
 -10 & 5 & 1
\end{pmatrix}\cdot\begin{pmatrix}
3 & 0 & 8
\end{pmatrix}^T$$

$$\downarrow$$

$$\begin{pmatrix}
 6& -2 & -2 \\
 10& -3 & 1 \\
 -10 & 5 & 1
\end{pmatrix}\cdot\begin{pmatrix}
3 \\
0\\
8
\end{pmatrix}\leftrightarrow\begin{pmatrix}6\cdot3-2\cdot0-2\cdot8\\10\cdot3-3\cdot0+1\cdot8\\-10\cdot3+5\cdot0+1\cdot8\end{pmatrix}=\begin{pmatrix}
 2\\
 38\\
-22
\end{pmatrix}$$

### Opgave 1.11 Løs ligningssystemet eller vis at der ikke findes en løsning til ligningssystemet.


$$2x − y + 3z = −1$$
$$−4x + 2y − 6z = 2$$
$$\left(\begin{array}{rrr|r}2&-1&3&-1\\-4&2&-6&2\end{array}\right)$$

Da matricen er af rang et vil der være uendeligt mange løsninger til lign-
ingssystemet. For at finde en af løsningerne kan man da den er af rang et,
give 2 af konstanterne en tilfældig værdi og løse for den sidste. y og z bliver
i dette tilfælde sat lig 0 hvorefter der løses for x

$$2x-0+3\cdot0=-1$$
$$2x=-1\leftrightarrow\frac{-2x}{2}=\frac{-1}{2}=-0.5$$

Til sidst sættes værdierne ind i ligningerne for at teste løsningen

$$−4 \cdot (-0.5) + 2\cdot 0 − 6 \cdot 0 = 2$$

$$−4 \cdot (-0.5) + 0  −  0 = 2$$


$$2 = 2$$
# Opgave 1.12 Bestem rangen af matricen

$$\left(\begin{array}{rrr|r}0&-2&1&3\\1&4&0&7\\5&5&5&5\end{array}\right)$$


$$\frac{R_{3}}{5}\leftrightarrow R_3$$
$$\left(\begin{array}{rrr|r}0&-2&1&3\\1&4&0&7\\\frac{5}{5}&\frac{5}{5}&\frac{5}{5}&\frac{5}{5}\end{array}\right)\leftrightarrow\left(\begin{array}{rrr|r}0&-2&1&3\\1&4&0&7\\1&1&1&1\end{array}\right)$$


$$R_1\leftrightarrow R_2$$


$$\left(\begin{array}{rrr|r}1&4&0&7\\0&-2&1&3\\1&1&1&1\end{array}\right)$$

$$R_3-R_{1} \leftrightarrow R_3$$

$$\left(\begin{array}{rrr|r}1&4&0&7\\0&-2&1&3\\1-1&1-4&1-0&1-7\end{array}\right) \leftrightarrow \left(\begin{array}{rrr|r}1&4&0&7\\0&-2&1&3\\0&-3&1&-6\end{array}\right)$$


$$R_2-R_{3}\leftrightarrow R_2$$

$$\left(\begin{array}{rrr|r}1&4&0&7\\0&1&0&9\\0&-3&1&-6\end{array}\right)$$


 $$R_{1} - 4\cdot R_{2} \leftrightarrow R_1$$

$$\left(\begin{array}{rrr|r}1&0&0&-29\\0&1&0&9\\0&-3&1&-6\end{array}\right)$$


$$R_{3} + R_{2} \cdot 3   \leftrightarrow R_3$$


$$\left(\begin{array}{rrr|r}1&0&0&-29\\0&1&0&9\\0&0&1&21\end{array}\right)$$









# Opgave 2.1 Bestem den afledte af



 $f(x) = 1 + x + x^2 + x^3 + x^4$

$$f'(x)= 1+2x+3x^2+4x^3$$


# Opgave 2.2 Find forskriften for den rette linje der tangerer ved $x  = 2$

 $f(x) = 1 + x + x^2 + x^3 + x^4$
 
 $y=f(x0)+f′(x0)⋅(x−x0)$


$$f(2)+f'(2)\cdot(x-2)$$
$$f(2) = 1 + 2 + 2^2 + 2^3 + 2^{4}\leftrightarrow3+4+8+16=31$$

$$f'(2)=1+4+12+32=49$$
 $$y=f(x0)+f′(x0)⋅(x−x0) \leftrightarrow  31+49\cdot(x-2)$$
 $$y=31+49\cdot(x-2) \leftrightarrow31+49x-98 \leftrightarrow -67+49x)$$



# Opgave 2.3 Beregn den afledte af

 $$f(x) = (1 + x)(1 + 2x)(1 + 3x)(1 + 4x)$$

$$f(x)=(1+x)\cdot(1+2x)\cdot(1+3x)\cdot(1+4x)$$

$$(1+x)\cdot(1+2x)=1\cdot1+1\cdot2x+x\cdot1+x\cdot2x=1+2x+x+2x^{2}=1+3x+2x^2$$

$$(1+3x)\cdot(1+4x)=1\cdot1+1\cdot4x+3x\cdot1+3x\cdot4x=1+4x+3x+12x^2=1+7x+12x^2$$

$$f(x)=(1+3x+2x^2)\cdot(1+7x+12x^2)=(1\cdot1+1\cdot7x+1\cdot12x^2+3x\cdot1+3x\cdot7x+3x\cdot12x^2+2x^2\cdot1+2x^{2}\cdot7x+2x^2\cdot12x^2)$$


$$f(x)=(1+3x+2x^2)\cdot(1+7x+12x^2)=1+7x+12x^2+3x+21x^2+36x^3+2x^2+14x^3+24x^4$$

$$f'(x)=1+10x+35x^2+50x^3+24x^4$$

$$f'(x)=10+35\cdot2\cdot x +50\cdot 3x^2+24\cdot4\cdot x^3=10+70x+150x^2+96x^3$$

















# 2.4 Lineariseringen er givet ved

Tangentens ligning: $L(x)=y'(x0)\cdot(x-x0)+y(x0)$

hvor $y=\sqrt{x+1}$ ved $x=3$


$x0=3$

Kæde reglen: $\frac{d}{dx}f(g(x))=f′(g(x))⋅g′(x)$

$g(x)=x+1$

$f(g(x))=\sqrt{g(x)}$

$g'(x)=1$

$f'(g(x))=\frac{1}{2\sqrt{g(x)}}$


$y'=\frac{1}{2\sqrt{x+1}}\cdot1$


$\frac{1}{2\sqrt{3+1}}\cdot(x-3)=\frac{1}{4}\cdot(x-3)=\frac{1}{4}x-\frac{3}{4}$


$y(3)=\sqrt{3+1}=\sqrt{4} = 2$


$L(x)=\frac{1}{4}x-\frac{3}{4}+2$










# 2.5 Beregn den afledte af

$$f(x)=\frac{(x^2+1)(x^3+2)}{(x^2+2)(x^3+1)}$$


$$f(x)=\frac{g(x)}{h(x)}$$

$$g(x)=x^5+2x^2+ x^3+2$$

$$h(x)=x^5+x^2+2x^3+2$$




Kvotientreglen:  $$\frac{g'(x)\cdot h(x)-g(x)\cdot h'(x)}{(h(x))^2}$$


$$g'(x)=5x^4+4x+3x^2$$
$$h'(x)=5x^4+2x+6x^2$$



$$\frac{(5x^4+4x+3x^2)\cdot(x^5+x^2+2x^3+2)-(x^5+2x^2+ x^3+2)\cdot(5x^4+2x+6x^2)}{(x^5+x^2+2x^3+2)^2}$$






# Vis at hvis f kan differentieres med $x$ og $f(x) > 0$, så gælder der


$$\frac{d}{dx}\sqrt{f(x)}=\frac{f'(x)}{2\sqrt{f(x)}}$$


Benyt derefter denne regel (Square Root Rule) til at bestemme den afledte
af

$$\sqrt{x^2+1}$$


kædereglen: $$\frac{d}{dx}h(g(x))=h′(g(x))⋅g′(x)$$

vi ved at følgende gælder:


$$\sqrt{f(x)}=f(x)^{\frac{1}{2}}$$


$$g(x)=f(x)$$

$$g'(x)=f'(x)$$

$$h(x)=\sqrt{x}$$

$$h'(x)=\frac{1}{2\sqrt{x}}$$

$$\frac{1}{2\sqrt{f(x)}}\cdot f'(x)$$


$$\frac{f'(x)}{2\sqrt{f(x)}}$$



Vi bruge den beviste regl på:

$$\sqrt{x^2+1}$$


$$g(x)=x^2+1$$

$$f(x)=\sqrt{x}$$


$$\frac{d}{dx}f(g(x))=f′(g(x))⋅g′(x)$$



$$g'(x)=2x$$
$$f'(x)=\frac{1}{2\sqrt{x}}$$

$$\frac{d}{dx}\sqrt{x^2+1}=\frac{1}{2\sqrt{x^2+1}}\cdot2x$$






# Opgave 2.8: Beregn et antal afledte af funktionen


$$f(x)=cos(ax)$$
Beregn s˚a mange at du kan gætte formlen for den n’te afledte $f^{(n)}(x)$
Verificer derefter gættet vha. induktion

$$f'(x)=a\cdot -sin(ax)$$

$$f''(x)=a\cdot a \cdot -cos(ax)=a^{2} \cdot -cos(ax)$$
$$f'''(x)=a\cdot a \cdot a \cdot sin(ax)=a^{3}\cdot sin(ax)$$
$$f''''(x)=a^{4} \cdot cos(ax)$$
$$f'''''(x)=a^{5}\cdot -sin(ax)$$

## formel for ulige:


$$f^{n}(x)=sin(ax)\cdot a^{n} \cdot (-1)^{\frac{n+1}{2}}$$

## Formel for lige tal


$$f^{n}(x)=cos(ax)\cdot a^{n}\cdot (-1)^{\frac{n}{2}}$$


# Opgave 2.9 Med cirka hvor mange procent vil et volumen $V=\frac{4}{3}\cdot \pi \cdot r^3$ af en kugle med radius r øges, hvis radius stiger med 2%?


$$V=\frac{4}{3}\cdot \pi \cdot (1.02\cdot r)^3$$

$$\frac{4}{3}\cdot \pi \cdot r^{3}\cdot1.02^3=\frac{4}{3}\cdot \pi \cdot r^{3}\cdot1.0612$$
Når r øges med 2%, øges V med 6.12%


# Opgave 2.10: Hvis f og g er funktioner, der begge kan differentieres mindst to gange, vis at følgende gælder:



$$(fg)''=f''g+2f'g'+fg''$$


Produkt reglen:

$$h'(x)=f'(x)\cdot g(x)+f(x)\cdot g'(x)$$

$$(fg)'=f'g+fg'$$
$$(fg)''=(f''g+f'g')+(f'g'+f g'')$$

$$(fg)''=f''g+f'g'+f'g'+fg''=2f'g'+f''g+fg''$$



# Opgave 2.11 Benyt differentialer til at approksimere ændringen i funktionen



$$h(t)=cos(\frac{\pi \cdot t}{4})$$

fra $t=2$ til $t=2+\frac{\pi}{10}$


$$L(x)=h'(x_{0})\cdot(x-x_0)+h(x_0)$$

$$h'(x)=-\frac{\pi}{4}\cdot sin(\frac{\pi\cdot t}{4})$$


$$h'(2)=-\frac{\pi}{4}\cdot sin(\frac{\pi \cdot 2}{4})=-\frac{\pi}{4}\cdot sin(\frac{6.28}{4})$$

$$h(2)=cos(\frac{\pi \cdot 2}{4})=cos(\frac{6.28}{4})$$

$$L(2)=-\frac{\pi}{4}\cdot sin(\frac{6.28}{4})\cdot(x-2)+cos(\frac{6.28}{4})$$
$$L(2)=-0.785\cdot sin(1.57)\cdot(x-2)+cos(1.57)$$

$$L(2)=-0.785 \cdot sin(1.57)\cdot x - 2\cdot sin(1.57)+cos(1.57)$$


$$h'(2+\frac{\pi}{10})=-\frac{\pi}{4}\cdot sin(\frac{\pi \cdot 2+\frac{\pi}{10}}{4})$$

$$h(2+\frac{\pi}{10})=cos(\frac{\pi \cdot 2+\frac{\pi}{10}}{4})$$

$$L(2+\frac{\pi}{10})=-\frac{\pi}{4}\cdot sin(\frac{\pi \cdot 2+\frac{\pi}{10}}{4})+(x-2+\frac{\pi}{10})+cos(\frac{\pi \cdot 2+\frac{\pi}{10}}{4})$$

# Opgave 2.12 

(Poiseuille’s Law) Volumenflowet $F$ (i liter per minut) af en væske igennem
et rør er proportional til rørets radius i fjerde potens:

$$F=k\cdot r^4$$

$$F=k*r^4\cdot1.1$$

$$k\cdot(r\cdot(1.1)^\frac{1}{4})^4$$
  $$k\cdot(r\cdot 1.024)^4$$
r skal øges med 0.024% elller 2.4%


# Opgave 3.1 Lineariser nedenst˚aende funktion omkring punktet $x_0=\pi$

$$f=sin(x)$$

$$L(x)=f'(x_0)\cdot(x-x_0)+f(x_0)$$

$$f'(sin(x))=cos(x)$$

$$cos(\pi)\cdot(x-\pi)+sin(\pi)$$

$$cos(\pi)\cdot x - cos(\pi)\cdot \pi+sin(\pi)$$

$$-1\cdot x - (-1) \cdot \pi =-x\cdot 1\cdot \pi=-x+\pi$$



# Opgave 3.2 Benyt en passende linearisering til at approksimere den angivne værdi.


$$f(x) = cos(x)$$

$$x_0=49^{\circ}\approx\frac{\pi}{4}$$
$$L(x)=f'(x_0)\cdot(x-x_0)+f(x_0)$$

$$f'(x)=-sin(x)$$
$$f'(x_0)=-sin(\frac{\pi}{4})$$


$$-sin(x_0)\cdot(x-x_0)=$$


$$L(x)=-sin(\frac{\pi}{4})\cdot x + sin(\frac{\pi}{4})\cdot\frac{\pi}{4}+cos(\frac{\pi}{4})$$



$$L(49\cdot\frac{\pi}{180})=-sin(\frac{\pi}{4})\cdot 49\cdot\frac{\pi}{180} + sin(\frac{\pi}{4})\cdot\frac{\pi}{4}+cos(\frac{\pi}{4})=0.6580675788$$


formeln for fejlen i linearisering


$$e(t)=\frac{f''(c)}{2}\cdot(t-x_0)^2$$

hvor $c=x_0=45$



$$e(t)=\frac{-cos(\frac{\pi}{4})}{2}\cdot(t-\frac{\pi}{4})^2$$


$$e(t)=\frac{-cos(\frac{\pi}{4})}{2}\cdot(49\cdot\frac{\pi}{4}-\frac{\pi}{4})^2=-0.0017233$$



$$[0.6580675788-0.0017233;0.65]=[]$$