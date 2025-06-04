---
creation date: 2024-12-10 20:03
modification date: Tuesday 10th December 2024 20:03:12
tags:
  - Assignments
year: 2024
semester: 3
links:
---

---
# [[Matematik og Indledende Programmering 4. januar 2024]]



# Opgave 1


## a)


## b)



# Opgave 2)

Betragt funktiuonen:

$$f(x)=ln(x)$$


## a) Bestem anden ordens taylorpolynomie $P2(x)$ for funktionen $f(x)$ omkring punktet $x=1$



$$P_n(x)=f(c)+\frac{f'(c)\cdot(x-c)^1}{1!}+\frac{f''(c)\cdot(x-c)^2}{2!}$$




$$f(x)=ln(x)$$

$$f'(x)=\frac{1}{x}$$


$$f''(x)=\frac{-1}{x^2}$$


$$f(1)=0$$
$$f'(1)=1$$
$$f''(1)=-1$$



$$P_2(x)=0+1\cdot(x-1)+\frac{-1\cdot(x-1)^2}{2!}$$
$$=(x-1)-\frac{1}{2}\cdot(x-1)^2$$

## b) Benyt taylorpolynomiet $P_2(x)$ fra opgave 2a for at estimere værdien af $f(1.5)$


$$P_{1.5}=(1.5-1)-\frac{1}{2}\cdot(1.5-1)^2$$
$$=0.5-\frac{1}{2}\cdot0.5^{2}\approx 0.375$$


$$ln(1.5)=0.405$$


## c) Estimer worst case fejlen for estimatet i b)

Vi skal bruge Lagrange-fejlleddet


$$R_n(x)=\frac{f^{n+1}(c)\cdot(x-c)^{n-1}}{(n+1)!}$$
hvor $c$ er et punkt i intervallet mellem $x$ og det omdrejningspunkt, $a$  (her $x=1$).


### Anvendelse på $f(x)=ln⁡(x)$


Bestem den tredje afledte:


$$f^{(3)}(x)=\frac{2}{x^3}$$

**Find udtryk for fejlen:** Med $n=2$, $c$ mellem $1$ og $1.5$, og $x=1.5$ bliver fejlen

$$R_2(1.5)=\frac{f^{(3)}(c)\cdot(1.5-1)^3}{3!}=\frac{\frac{2}{x^3}\cdot(0.5)^3}{6}$$

Hvor $c$ er ukendt, men ligger i intervallet $1\leq c \leq 1.5$


**Vurder worst case:** Den maksimale fejl sker, når $f^{(3)}(c)$ er størst i intervallet $c$ $[1,1.5]$. Da $f^{(3)}(c)=\frac{2}{c^3}$ er den maksimalle værdi ved $c=1$:

$$f^{(3)}(1)=\frac{2}{1^3}=2$$

Worst case-fejlen bliver dermed:

$$R_2(1.5)\leq\frac{2\cdot(0.5)^3}{6}=\frac{2\cdot0.125}{6}=\frac{0.25}{6}\approx0.041666667$$


# Opgave 4


## a) Vi skal finde den generelle løsning til differentialligningen:

$$\frac{dy}{dx}-\frac{y}{x}=x^2$$

