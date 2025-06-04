---
creation date: 2024-12-07 13:41
modification date: Saturday 7th December 2024 13:41:27
tags:
  - Assignments
year: 2024
semester: 3
links: "[[Matematik og Indledende Programmering 2 maj 2024]]"
---

---
# [[Matematik og Indledende Programmering Assignment]]


# Opgave 1 (15 point)

## a) Beregn værdien af udtrykket herunder:

$$\begin{bmatrix}7&1&-2\\4&4&-2\\-8&7&7\end{bmatrix}\cdot\begin{bmatrix}2\\2\\-1\end{bmatrix}$$ 

$$7\cdot2+1\cdot2-2\cdot(-1)=18$$
$$4\cdot2+4\cdot2-2\cdot(-1)=18$$
$$-8\cdot2+7\cdot2+7\cdot(-1)=-9$$

$$\begin{bmatrix}7&1&-2\\4&4&-2\\-8&7&7\end{bmatrix}\cdot\begin{bmatrix}2\\2\\-1\end{bmatrix}=\begin{bmatrix}18\\18\\-9\end{bmatrix}$$


##  b) Bestem determinanten af følgende matrice

$$A=\begin{bmatrix}6&2&1\\4&-2&2\\0&4&-4\end{bmatrix}$$


For at beregne determinanten af en 3×33 \times 33×3-matrix, bruger man **udvikling efter første række**. Formlen for determinanten ser sådan ud:
Hvis $A$ er en $3\times3$ matrix:

$$\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}$$

så beregnes determinanten $\det(A)$ som:

$$det(A)=a(ei−fh)−b(di−fg)+c(dh−eg)$$

### Trinvis metode

1. **Udvikling efter første række**: Tag elementerne fra første række $(a,b,c)$, og beregn hver determinanteffekt ved at fjerne den række og søjle, hvor elementet sidder, og tage determinanten af den tilbageværende $2\times2$ matrix.
    
2. **Bestem $2\times2$ determinanter**: For hver $2\times2$-matrix, brug formlen:

$$det(\begin{bmatrix}x&y\\z&w\end{bmatrix})=x\cdot w - y \cdot z$$




Udvikling efter første række:

$$A=\begin{bmatrix}6&2&1\\4&-2&2\\0&4&-4\end{bmatrix}$$


$$det(A)=a(ei−fh)−b(di−fg)+c(dh−eg)$$



$$det(A)=6\begin{bmatrix}-2&2\\4&-4\end{bmatrix}-2\begin{bmatrix}4&2\\0&-4\end{bmatrix}+1\begin{bmatrix}4&-2\\0&4\end{bmatrix}$$


### Beregning af $2\times2$ determinanter

- $\begin{bmatrix}-2&2\\4&-4\end{bmatrix}=$ $-2\cdot(-4)-2\cdot4\leftrightarrow 8-8=0$
- $\begin{bmatrix}4&2\\0&-4\end{bmatrix}=$ $4\cdot(-4)-2\cdot0\leftrightarrow -16-0=-16$
- $\begin{bmatrix}4&-2\\0&4\end{bmatrix}=$$4\cdot4-2\cdot0\leftrightarrow 16-0=16$


$$det(A)=6\cdot0-2\cdot(-16)+1\cdot16\leftrightarrow32+16=48$$


$$det(A)=48$$





## c) Anvend Gauss elimination til at løse ligningssystemet:


$$6x+2y+z=22$$

$$4x-2y+2z=14$$
$$0x+4y-4z=-4$$

$$\left[\begin{array}{rrr|r}6&2&1&22\\4&-2&2&14\\0&4&-4&-4\end{array}\right]$$

### Step 1: $\frac{R_1}{6}\rightarrow R_1$


$$\left[\begin{array}{rrr|r}1&\frac{2}{6}&\frac{1}{6}&\frac{22}{6}\\4&-2&2&14\\0&4&-4&-4\end{array}\right]$$


da $\frac{2}{6}$ og $\frac{22}{6}$ kan divideres med 2 kan vi forkorte brøkerne:




$$\left[\begin{array}{rrr|r}1&\frac{1}{3}&\frac{1}{6}&\frac{11}{3}\\4&-2&2&14\\0&4&-4&-4\end{array}\right]$$


### Step 2: $R_2-4\cdot R_1$


$$R_{2,1}=4-4\cdot1\leftrightarrow4-4=0$$
$$R_{2,2}=-2-4\cdot\frac{1}{3}$$


#### Trin 1 $R_{2,2}$: Beregn multiplikationen
$$=-\frac{4\cdot1}{3}\leftrightarrow-\frac{4}{3}$$

#### Trin 2 $R_{2,2}$: Indsæt resultatet i udtrykket

$$=-2-\frac{4}{3}$$
#### Trin 3 $R_{2,2}$: Omskriv til fælles nævner
Omskriv $-2$ som en brøk med nævner 3

$$-2=\frac{-6}{3}$$

alså:

$$-2=\frac{-6}{3}-\frac{4}{3}$$


#### Trin 4 $R_{2,2}$: Udfør subtraktionen

$$R_{2,2}=\frac{-6}{3}-\frac{4}{3}\leftrightarrow\frac{-6-4}{3}=\frac{-10}{3}$$




$$R_{2,3}=2-4\cdot\frac{1}{6}$$

#### Trin 1 $R_{2,3}$: Beregn multiplikationen

$$-4\cdot\frac{1}{6}=\frac{-4\cdot1}{6}=-\frac{4}{6}$$


Vi kan forekle brøkerne ved at dividere med 2, så for vi:

$$\frac{4}{6}=\frac{2}{3}$$


#### Trin 2 $R_{2,3}$: Indsæt resultatet i udtrykket

$$R_{2,3}=2-\frac{2}{3}$$

#### Trin 3 $R_{2,3}$: Omskriv til fælles nævner

Omskriv 2 som en brøk med nævner 3 $$\frac{6}{3}$$
alså:

$$\frac{6}{3}-\frac{2}{3}$$



#### Trin 4 $R_{2,3}$: Udfør subtraktionen

$$R_{2,3}=\frac{6}{3}-\frac{2}{3}\leftrightarrow\frac{6-2}{3}=\frac{4}{3}$$





























#### $R_{2,4}$
$$R_{2,4}=14-4\cdot \frac{11}{3}\leftrightarrow14-14.66=-0.66=-\frac{2}{3}$$



$$\left[\begin{array}{rrr|r}1&\frac{1}{3}&\frac{1}{6}&\frac{11}{3}\\0&\frac{-10}{3}&\frac{4}{3}&-\frac{2}{3}\\0&4&-4&-4\end{array}\right]$$






### Step 3: $\frac{R_2}{-\frac{10}{3}}\rightarrow R_2$




$$R_{2,3}=​\frac{4}{3}÷\frac{-10}{3}$$

Brug $KCF$ som betyder:

- K: Keep
- C: Change
- F: Flip




$$R_{2,3}=\frac{4}{3}÷\frac{-10}{3}\leftrightarrow\frac{4}{3}\cdot\frac{3}{-10}=\frac{4\cdot3}{3\cdot(-10)}=\frac{12}{-30}$$


brøken kan forkortes da $12$ og $30$ begge kan dividres med 6


$$R_{2,3}=\frac{12}{-30}=-\frac{2}{5}=-0.4$$




$$R_{2,4}=-\frac{2}{3}÷\frac{-10}{3}$$


Bruger KCF igen:

- K: Keep
- C: Change
- F: Flip


$$R_{2,4}=-\frac{2}{3}\cdot(-\frac{3}{10})\leftrightarrow\frac{2\cdot3}{3\cdot10}=\frac{6}{30}$$


Kan forkortes da $6$ og $30$ kan dividres med $3$


$$\frac{6}{30}=\frac{2}{10}=0.2$$



$$
\left[\begin{array}{rrr|r}1&\frac{1}{3}&\frac{1}{6}&\frac{11}{3}\\0&1&-0.4&0.2\\0&4&-4&-4\end{array}\right]$$



### Step 4: $R_{3}-4\cdot R_{2}\rightarrow R_3$


$$0-4\cdot0\leftrightarrow0-0=0$$
$$4-4\cdot1\leftrightarrow4-4=0$$
$$-4-4\cdot(-0.4)\leftrightarrow-4-1.6=-2.4$$

$$-4-4\cdot0.2\leftrightarrow-4-0.8=-4.8$$



$$
\left[\begin{array}{rrr|r}1&\frac{1}{3}&\frac{1}{6}&\frac{11}{3}\\0&1&-0.4&0.2\\0&0&-2.4&-4.8\end{array}\right]$$








### Step 5: $R_{1}-\frac{1}{3}\cdot R_{2}\rightarrow R_1$


 $$1-\frac{1}{3}\cdot0\leftrightarrow1-0=1$$



$$\frac{1}{3}-\frac{1}{3}\cdot1\leftrightarrow\frac{1}{3}-\frac{1}{3}=0$$



$$\frac{1}{6}-\frac{1}{3}\cdot(-0.4) = 0.3$$


$$\frac{11}{3}-\frac{1}{3}\cdot0.2=3.6$$

$$
\left[\begin{array}{rrr|r}1&1&0.3&3.6\\0&1&-0.4&0.2\\0&0&-2.4&-4.8\end{array}\right]$$



### Step 6: $\frac{R_3}{-2.4}\rightarrow R_3$


$$R_{2,3}=\frac{-2.4}{-2.4}=1$$


$$R_{2,4}=\frac{-4.8}{-2.4}=2$$


$$
\left[\begin{array}{rrr|r}1&\frac{1}{3}&\frac{1}{6}&\frac{11}{3}\\0&1&-0.4&0.2\\0&0&1&2\end{array}\right]$$
### Step 7: $R_{2}+0.4\cdot R_{3}\rightarrow R_2$



$$-0.4+0.4\cdot1\leftrightarrow-0.4+0.4=0$$

$$0.2+0.4\cdot2\leftrightarrow0.2+0.8=1$$


$$
\left[\begin{array}{rrr|r}1&0&0.3&3.6\\0&1&0&1\\0&0&1&2\end{array}\right]$$






### Step 8: $R_{1}-0.3\cdot R_{3}\rightarrow R_1$


$$0.3-0.3\cdot1\leftrightarrow0.3-0.3=0$$

$$3.6-0.3\cdot2\leftrightarrow3.6-0.6=3$$


$$
\left[\begin{array}{rrr|r}1&0&0&3\\0&1&0&1\\0&0&1&2\end{array}\right]$$






$x=3$
$y=1$
$z=2$

# Opgave 2 (10 point)

## a) Bestem værdien af udtrykket herunder


$$\lim_{x\rightarrow2} \frac{x^3-3x^2+4}{x^3-2x^2-4x+8}$$


### Step 1 insæt 2 på x plads

$$\frac{2^3-3\cdot2^2+4}{2^3-2\cdot2^2-4\cdot2+8}\leftrightarrow \frac{8-12+4}{8-8-8+8}=\frac{0}{0}$$

både tæller og nævner bliver $0$, så vi har en $\frac{0}{0}$​-ubestemt grænseværdi. Vi skal derfor faktorisere eller bruge L’Hôpitals regel.



$$\lim_{x\rightarrow C} \frac{f(x)}{g(x)}=\lim_{x\rightarrow C}\frac{f'(x)}{g'(x)}$$



$$f(x)=x^3-3x^2+4$$
$$g(x)=x^3-2x^2-4x+8$$


$$f'(x)=3x^2-3\cdot2x\leftrightarrow3x^2-6x$$
$$g'(x)=3x^2-2\cdot2x-4\leftrightarrow3x^2-4x-4$$


sæt 2 ind på x plads igen, hvis det giver $\frac{0}{0}$



$$f'(2)=3\cdot2^2-6\cdot2\leftrightarrow12-12=0$$



$$g'(2)=3\cdot2^2-4\cdot2-4\leftrightarrow12-8-4=0$$



Vi differentiere igen da det stadigvæk giver $\frac{0}{0}$


$$f''(x)=3\cdot2x-6\leftrightarrow6x-6$$

$$g''(x)=3\cdot2x-4\leftrightarrow6x-4$$



Sæt $2$ på $x$ plads igen


$$f''(2)=6\cdot2-6=6$$
$$g''(2)=6\cdot2-4\leftrightarrow12-4=8$$

$$\lim_{x\rightarrow2} \frac{6}{8}$$

brøken kan forkortes da begge tal går op i 2:

$$\frac{6}{8}=\frac{3}{4}$$


svaret er:

$$\lim_{x\rightarrow2} \frac{3}{4}$$




## b) Bestem den generelle løsning til differentialligningen


$$\frac{dy}{dx}-y=e^x$$



# Opgave 3



## a) Beregn værdien af det bestemte integrale


$$\int_{-2}^{3}\frac{2}{3+x}dx$$


use subsitution


$$u=3+x$$
$$du=dx$$

$$x=-2\rightarrow u=1$$
$$x=3 \rightarrow u = 6$$


$$2\int_{1}^{6}\frac{1}{u} du$$


$$2[ln|u|]_{1}^{6}$$
$$=2(ln(6)-ln(1))$$
$$=2ln(6)+C$$


## b) Bestem udtrykket for det ubestemte integrale

$$\int x\cdot e^{-x}dx$$


use integration by parts:


$$\int u\quad dv=u\cdot v-\int v\quad du$$
 

$$u=x$$
$$du=1dx$$
$$v=-e^{-x}$$
$$dv=e^{-x} dx$$

$$x\cdot(-e^{-x})-\int -e^{-x} (1dx)$$

$$x\cdot(-e^{-x})+e^{-x}+C$$

## c) Opdel udtrykket herunder i partial brøker

$$\frac{4x+13}{(x+3)\cdot(x+4)}$$


# Opgave 4


## a) Bestem den reelle og imaginære del af tallet z


$$z= (1+2i)\cdot(2-i)\cdot(1+i)$$

### Trin 1: Multiplicér de første to faktorer

Reglen for multiplikation af komplekse tal:

 $$(a+bi)\cdot(c+di)=(a\cdot c-b\cdot d)+(a\cdot d + b\cdot c)i$$

For $(1+2i)\cdot(2-i)$:
- $a=1$
- $b=2$
- $c=2$
- $d=-1$

$$\mathbb{R} : a\cdot c−b\cdot d = 1\cdot 2-2\cdot(-1)=2+2=4$$
$$Im: a\cdot d + b \cdot c=1\cdot(-1)+2\cdot2=-1+4=3$$

Så:

$$(1+2i)(2-i)=4+3i$$


### Trin 2: Multiplicér resultatet med $(1+i)$



Nu beregner vi $(4+3i)(1+i)$:

- $a=4$
- $b=3$
- $c=1$
- $d=1$


$$\mathbb{R}: a\cdot c - b\cdot d = 4\cdot1-3\cdot1\leftrightarrow4-3=1$$
$$Im: a\cdot d + b\cdot c = 4\cdot1-3\cdot1\leftrightarrow4+3=7$$


$$z=1+7i$$

hvor $\mathbb{R} = 1$ og den imaginær er $7$




## b) Indtegn følgende værdier i et Argand diagram



$$z_1=1+2i$$
$$z_2=2-i$$
$$z_3=3\cdot e^{i\frac{\pi}{4}}$$

$$z_4=3\cdot e^{i\frac{5\cdot\pi}{4}}$$

for at løse $z_3$ skal vi bruge Euler's formula:


$$e^{j\theta}=cos(\theta)+i\cdot sin(\theta)$$


hvor:

- $j=i$
- $\theta=\frac{\pi}{4}$



plugging in the values:

$$e^{i\frac{\pi}{4}}=cos(\frac{\pi}{4})+i\cdot sin(\frac{\pi}{4})$$


$$cos(\frac{\pi}{4})=\frac{\sqrt{2}}{2}$$

$$sin(\frac{\pi}{4})=\frac{\sqrt{2}}{2}$$


we get:

$$3\cdot(\frac{\sqrt{2}}{2}+i\cdot\frac{\sqrt{2}}{2})$$

simplify:


$$\frac{3\cdot\sqrt{2}}{2}+i\cdot\frac{3\cdot\sqrt{2}}{2}$$



same thing for $z_4$


$$e^{j\theta}=cos(\frac{5\cdot\pi}{4})+i\cdot sin(\frac{5\cdot\pi}{4})$$



we get:

$$cos(\frac{5\cdot\pi}{4})=-\frac{\sqrt{2}}{2}$$
$$sin(\frac{5\cdot\pi}{4})=-\frac{\sqrt{2}}{2}$$


$$3\cdot(-\frac{\sqrt{2}}{2}+i\cdot(-\frac{\sqrt{2}}{2}))$$

Simplifying the expression:


$$-\frac{3\cdot\sqrt{2}}{2}-i\cdot\frac{3\cdot\sqrt{2}}{2}$$


# Opgave 5


## a) Bestemxogykoordinater til alle de steder p ̊a figuren fra opgave 5, hvor der er skæringer mellemto af de tre funktioner $f(x)$, $g(x)$ og $h(x)$

$$f(x)=(x^2-1)\cdot e^{-0.5x}$$
$$g(x)=1.6$$
$$h(x)=2\cdot e^{-0.5x}$$


### skæring med $f(x)$ og $h(x)$


$$f(x)=h(x)$$


$$\frac{(x^2-1)\cdot e^{-0.5x}}{e^{-0.5x}}=\frac{2\cdot e^{-0.5x}}{e^{-0.5x}}$$


$$x^2-1=2$$
$$x^2-1+1=2+1\leftrightarrow x^2=3$$
$$x=\pm \sqrt{3}$$


### skæring med $g(x)$ og $h(x)$


$$1.6=2\cdot e^{-0.5x}$$

$$\frac{1.6}{2}=\frac{e^{-0.5x}}{2}$$

$$0.8=e^{-0.5x}$$


$$ln(0.8)=ln(e^{-0.5x})$$


Use the property of logarithms

$$ln(e^a)=a$$

$$ln(0.8)=-0.5x$$

multiply both sides by $-2$ to isolate $x$:


$$x=-\frac{2ln(0.8)}{1}$$

$$=\frac{2ln(0.8)}{1}$$



