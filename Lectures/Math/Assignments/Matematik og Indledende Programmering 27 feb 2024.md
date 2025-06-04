---
creation date: 2024-12-10 11:46
modification date: Tuesday 10th December 2024 11:46:41
tags:
  - Assignments
year: 2024
semester: 3
links:
---

---
# [[Matematik og Indledende Programmering 27 feb 2024]]


# Opgave 1

## a) Beregn determinanten af matricen $A$

$$A=\begin{bmatrix}1-\lambda & 2 & 3\\0&-\lambda&1\\1&0&2-\lambda\end{bmatrix}$$


Detaminant af $3\times3$ matrix $\begin{bmatrix}a&b&c\\ d&e&f\\ g&h&i\end{bmatrix}$:

$$det(A)=a(e\cdot i - f\cdot h)-b(d\cdot i - f\cdot g)+c(d\cdot h - e\cdot g)$$
hvor:

- $e=-\lambda$
- $i=2-\lambda$
- $f=1$
- $h=0$
- $d=0$
- $g=1$
- $a=1-\lambda$
- $b=2$
- $c=3$


sæt ind:

$$det(A)=(1-\lambda)[(-\lambda\cdot 2-\lambda-1\cdot0)]-2[(0\cdot 2-\lambda-1\cdot 1)]+3(0\cdot0-(-\lambda)\cdot1)$$


simplify: 

$$det(A)=(1-\lambda)(-\lambda^2+2\lambda)+2+3\lambda$$
$$=-\lambda^3+2\lambda^2+\lambda^2-2\lambda+2+3\lambda$$
$$=\lambda^3-3\lambda^2+5\lambda+2$$





## b) Anvend Gauss elimination til at løse ligningssystemet:


$$3x+2y-z=9$$
$$2x+3y+z=11$$
$$x+2y-3z=3$$


$$\left[\begin{array}{rrr|r}3&2&-1&9\\2&3&1&11\\1&2&-3&3\end{array}\right]$$


### step 1: byt $R_1$ med $R_3$


$$\left[\begin{array}{rrr|r}1&2&-3&3\\2&3&1&11\\3&2&-1&9\end{array}\right]$$


### step 2: $R_2-R_1\cdot2$


$$2-1\cdot2\leftrightarrow2-2=0$$
$$3-2\cdot2\leftrightarrow3-4=-1$$

$$1+3\cdot2\leftrightarrow1+6=7$$


$$11-3\cdot2\leftrightarrow11-6=5$$


### step 3: $R_3-3{\cdot}R_1\rightarrow R_3$


$$3-3\cdot1\leftrightarrow3-3=0$$
$$2-3\cdot2\leftrightarrow2-6=-4$$

$$-1-3\cdot(-3)\leftrightarrow-1+9=8$$

$$9-3\cdot3\leftrightarrow9-9=0$$


$$\left[\begin{array}{rrr|r}1&2&-3&3\\0&-1&7&5\\0&-4&8&0\end{array}\right]$$



### step 3: $\frac{R_2}{-1}$


$$\left[\begin{array}{rrr|r}1&2&-3&3\\0&1&-7&-5\\0&-4&8&0\end{array}\right]$$



### step 4: $R_3+4\cdot R_2$

$$-4+4\cdot1\leftrightarrow -4+4=0$$
$$8+4\cdot (-7)\leftrightarrow8-28=-20$$
$$0+4\cdot(-5)\leftrightarrow0-20=-20$$

$$\left[\begin{array}{rrr|r}1&2&-3&3\\0&1&-7&-5\\0&0&-20&-20\end{array}\right]$$



### Step 5: $\frac{R_3}{-20}$


$$\left[\begin{array}{rrr|r}1&2&-3&3\\0&1&-7&-5\\0&0&1&1\end{array}\right]$$





### Step 6 solve:

$$z=1$$

$$y-7=-5$$

$$y-7+7=-5+7$$
$$y=2$$

$$x+2\cdot(2)-3=3$$

$$x+4-3=3$$
$$x+1=3$$
$$x=2$$


$x=2$
$y=2$
$z=1$


# Opgave 2


## a) Bestem værdien af udtrykket herunder


$$\lim_{x\rightarrow5}\frac{x^2-10x+25}{(x-5)\cdot cos(x-5)}$$



sæt 5 ind på x's plads

$$\frac{5^2-10\cdot5+25}{5-5)\cdot cos(5-5)}\leftrightarrow\frac{25-50+25}{0\cdot1}=\frac{0}{0}$$


da vi får $\frac{0}{0}$ skal vi bruge  L'Hôpital's regl

$$\lim_{x\rightarrow C}\frac{f(x)}{g(x)}=\lim_{x\rightarrow C}\frac{f'(x)}{g'(x)}$$

$$f(x)=x^2-10x+25$$

$$g(x)=(x-5)\cdot cos(x-5)$$

$$f'(x)=2x-10$$

for at regne $g'(x)$ skal vi bruge product reglen:

$$(f\cdot g)'=f'(x)\cdot g(x)+f(x)\cdot g'(x)$$

hvor vores:
- $f(x)=(x-5)$
- $g(x)=cos(x-5)$


sæt ind:

$$(f\cdot g)' = 1\cdot cos(x-5)+(x-5)\cdot (-sin(x-5))$$
$$=1\cdot cos(x-5)-(x-5)\cdot sin(x-5)$$
$$=cos(x-5)-(x-5)\cdot sin(x-5)$$


da vi har vores $g'(x)$ kan vi sætte det ind:


$$\frac{2x-10}{cos(x-5)-(x-5)\cdot sin(x-5)}$$


sæt 5 ind på x's plads:


$$\frac{2\cdot5-10}{cos(5-5)-(5-5)\cdot sin(x-5)}\leftrightarrow \frac{10-10}{1-0\cdot0}=\frac{0}{1}$$


$\lim_{x\rightarrow5}\frac{x^2-10x+25}{(x-5)\cdot cos(x-5)}=0$


## b) Bestem den afledte af funktionen

$$f(x)=\frac{3}{e^{-x^2+1}}$$


brug Kvotientreglen:

$$h(x)=\frac{f(x)}{g(x)}\leftrightarrow h'(x)=\frac{f'(x) \cdot g(x)-f(x)\cdot g'(x)}{(g(x))^2}$$


hvor:
- $f(x)=3$
- $g(x)=e^{-x^{2}+1}$


sæt ind:


$$\frac{0\cdot e^{-x^{2}+1}-3\cdot (e^{-x^{2}+1}\cdot(-2x))}{(e^{-x^{2}+1})^2}$$


simplificer:

$$\frac{-3\cdot(-2x)\cdot e^{-x^{2}+1}}{(e^{-x^{2}+1})^2}$$

$$=\frac{6x\cdot e^{-x^{2}+1}}{(e^{-x^{2}+1})^2}$$

Forenkl nævneren ved at skrive som en potens:

$$6x\cdot \frac{e^{-x^{2}+1}}{(e^{-x^{2}+1})^{2}}\leftrightarrow 6x\cdot \frac{\cancel{e^{-x^{2}+1}}}{(e^{-x^{2}+1})^{\cancel{2}}}=6x\cdot e^{-x^{2}+1}$$






# Opgave 3



## a) Beregn værdien af det bestemte integrale

 $$\int_{-2}^{3}\frac{x}{1+x^2}dx$$



![[{AE7EA282-918B-4796-8F36-1C00CAE2CD27}.png]]


$$g(x)=1+x^2$$
$$u=1+x^2$$

$$du=2x\quad dx$$
$$\frac{1}{2}\cdot du = x \quad dx$$


 $$\int \frac{x}{1+x^{2}}dx= \int \frac{1}{u} \cdot  \frac{1}{2}du$$
$$=\frac{1}{2}\cdot\int \frac{1}{u} du$$

$$=\frac{1}{2}\cdot ln(u)+C$$

 $$=\frac{1}{2}\cdot ln(1+x^2)+C$$



sæt grænseværdierne ind på x's plads


$$\frac{1}{2}\cdot ln(7)=0.97$$

$$\frac{1}{2}\cdot ln(5)=0.80$$

$$0.97-0.80=0.17$$


## b) Find udtrykket for det ubestemte integrale

$$\int x\cdot sin(2x) dx$$


$$u=x$$
$$dv=sin(2x)dx$$

$$v=-\frac{1}{2}\cdot cos(2x) dx$$


$$\int u \cdot dv = u\cdot v-\int v du$$


$$x\cdot (-\frac{1}{2}\cdot cos(2x))-\int -\frac{1}{2} \cdot cos(2x) dx$$

$$-\frac{1}{2}\cdot x\cdot cos(2x)+\frac{1}{2}\int cos(2x)dx$$

$$\int cos(2x) dx = \frac{1}{2}\cdot sin(2x) dx$$

$$-\frac{1}{2}\cdot x\cdot cos(2x)+\frac{1}{4} \cdot sin(2x)+C$$

# Opgave 4


## a) Angiv den reelle og imaginære del af tallet Z



$$Z= \frac{2\cdot e^{i\frac{\pi}{2}}}{3\cdot e^{i\frac{\pi}{4}}}$$


euler's formel:

$$e^{i\theta}=cos(\theta)+i \cdot sin(\theta)$$
insæt:

$$e^{i\frac{\pi}{2}}=cos(\frac{\pi}{2})+i\cdot sin(\frac{\pi}{2})$$
$$=0+i\cdot 1$$
$$=i$$

$$e^{i\frac{\pi}{4}}=cos(\frac{\pi}{4})+i\cdot sin(\frac{\pi}{4})$$


$$=\frac{\sqrt{2}}{2}+i\cdot\frac{\sqrt{2}}{2}$$


$$Z= \frac{2\cdot i}{3\cdot (\frac{\sqrt{2}}{2}+i\cdot\frac{\sqrt{2}}{2})}$$

## b) Løs differentialligningen

$$\frac{dv}{dt}=g-k\cdot v$$


$$\frac{dv}{dt}=y'$$
$$a=k$$
$$y=v$$
$$b=g$$


$$\frac{dv}{dt}+k\cdot v=g$$


$$v=\frac{g}{k}+c\cdot e^{-kt}$$

![[Pasted image 20241210174923.png]]





# Opgave 5


## a) Bestem x og y koordinater til alle de steder på figuren fra opgave 5, hvor funktionen $g(x)$ skærer en af funktionerne $f(x)$ eller $h(x)$.


$$f(x)=2\cdot cos(3x)\cdot e^{-0.2x}$$
$$g(x)=0.95$$
$$h(x)=2\cdot e^{-0.2x}$$


### Løsning af $f(x)=g(x)$

$$2\cdot cos(3x)\cdot e^{-0.2x}=0.95$$


#### Del med 2 for at isolere cos(3x)

$$ cos(3x)\cdot e^{-0.2x}=0.475$$

#### Del med $e^{-0.2x}$ 

$$ cos(3x)=\frac{0.475}{e^{-0.2x}}$$

$$=0.475\cdot e^{-0.2x}$$


#### Løsning af $h(x)=g(x)$

$$2\cdot e^{-0.2x}=0.95$$


del med 2

$$e^{-0.2x}=\frac{0.95}{2}$$


tag ln på begge sider:

$$-0.2x=ln(\frac{0.95}{2})$$


## b) Bestem værdien af følgende bestemte integrale


$$\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} 2\cdot cos(3x)\cdot e^{-0.2x}dx$$



integration by parts:


$$\int u \cdot dv = u\cdot v-\int v du$$


$$u=e^{-0.2x}$$

$$du=-0.2\cdot e^{-0.2x}dx$$

$$dv = 2\cdot cos(3x)dx$$

$$v = \frac{2}{3} \cdot sin(3x) dx$$



$$e^{-0.2x}\cdot\frac{2}{3}\cdot sin(3x)-\int \frac{2}{3}\cdot sin(3x)\cdot(0.2e^{-0.2x})dx$$

$$e^{-0.2x}\cdot\frac{2}{3}\cdot sin(3x)- \frac{2}{3}\int  sin(3x)\cdot(0.2e^{-0.2x})dx$$

