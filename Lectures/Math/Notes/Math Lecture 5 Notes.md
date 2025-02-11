---
tags:
  - Notes
links: "[[Math Lecture 5]]"
creation date: 2024-11-27 19:13
modification date: Wednesday 27th November 2024 19:13:53
semester: 3
year: 2024
---


---
# [[Math Lecture 5 Notes]]

---



# Grænseværdier

- Lad os forestille, at vi skal finde Grænseværdien af følgende funktion:

$$\lim_{x\rightarrow2} \frac{x^2-4}{x-2}$$

Vi vil forsøge, at indsætte tallet: 2,1 ved $f(2.1)$

$$f(2.1)=\frac{2.1^2-4}{2.1-2}=\frac{0.41}{0.1}=4.1$$


Hvorimod ved f(2.01) har vi følgende:

$$f(2.01)=\frac{2.01^2-4}{2.01-2}=4.01$$


**OBS**: Vi kan se, at jo tættere vores x-værdi inde i funktionen nærmere sig ved 2, desto mere præcis har vi en y-værdi som er ved tallet 4. Men i fleste tilfælde er situationen ikke såden, men anderledes!


## Eksempler på Grænseværdier

Vi har følgende funktion, som vi skal udregne:

$$\lim_{x\rightarrow 2}\frac{x^{2}-4}{x-2}=4$$

- STEP 1: Samme værdier fjernes på nævneren og tælleren i brøken.

$$\lim_{x\rightarrow 2}\frac{(x+2)\cdot (\cancel{x-2)}}{\cancel{(x-2)}}=\lim_{x\rightarrow 2}(x+2)=2+2=4$$

---

Vi kan se, at vi har følgende funktion:

$$\lim_{x\rightarrow 5}x^2+2x-4$$

STEP 1: X-værdien indsættes inde på funktionens x-værdier.


$$x=5$$

$$5^2+2\cdot5-4\leftrightarrow25+10-4\leftrightarrow35-4=31$$

---



Vi har følgende funktion, som vi skal udregne:

$$\lim_{x\rightarrow 3}\frac{x^3-27}{x-3}$$

- STEP 1: Vi ved på forhånd, at vi har en kubik $x^3$ derfor bruges formlen: 

$$A^3-B^3=(A\cdot B)\cdot(A^{2}+A\cdot B+B^{2})$$

$$x^3=3^2+3\cdot3+9=9\cdot3=27$$



---


## Eksempler på Uendeligheder


- at finde Grænse af Uendeligheden og dets løsninger:
	- Her er der tilføjet nogle eksempler på, hvordan Uendeligheder er med en Konstant.
	- **BEMÆRK**: At når vi har en værdi som går mod uendelig fra det ene side eller det andet, så ender resultatet med at være uendeligt med en plus eller minus fortegn foran, afgørende om hvilken retning vi går mod.


$$\lim_{x\rightarrow \infty}(x^2)=+\infty$$

$$\lim_{x\rightarrow -\infty}(x^2)=(-\infty)^2=+\infty$$


$$\lim_{x\rightarrow \infty}(x^3)=(\infty)^3=+\infty$$


$$\lim_{x\rightarrow -\infty}(x^3)=(-\infty)^3=-\infty$$


## Mean Value Teorien


- Når vi snakker om Mean Value teorien, forsøger vi at finde den midterste punkt mellem to dele.
- Her kommer vi til at vise steps til hvordan man løser opgaven med Mean Value teorien.


- STEP 1: Opskriv funktionen

$$f(x)=x^2-4x+1$$

og $$[1,5]$$


- STEP 2: Differentiere funktionen:


$$f'(x)=2x-4$$



- STEP 3: Indsæt Interval værdierne inde i stamfunktionen.


$$f(5)=5^2-4\cdot5+1=25-20+1=6$$

$$f(1)=1^2-4+1=-3+1=-2$$


STEP 4: Sæt værdierne ind i formlen.


## Tangentlinjen
- Her kommer vi til at snakke om, hvordan man kan danne en tangentligning udefra en funktion.
- EKS: Vi har fået funktionen:  $f(x)=3x^{4}-5x^{3}+6x+8$ ved $x=1$
- Vi starter med, at finde y-værdien da vi allerede har fået oplyst at x, men mangler y for (x,y).
	- Måden vi finder y-værdien er på, at tage alle talværdierne (uden) x og lægger dem sammen med deres foretegn.


$$f(x)=3-5+6+8=12$$

$$P(x,y)=(1,12)$$
- Differentiere x-værdierne i stamfunktionen

$$f(x)=3x^{4}-5x^{3}+6x+8$$
$$=3\cdot(4x^{4-1})-3\cdot5\cdot(x^{3-1})+6+0$$
$$=3\cdot(4x^3)-3\cdot5\cdot(x^{2})+6$$
$$=12\cdot x^{3}-15\cdot x^{2}+6$$


udregn hældningen og dette gøres ved at sætte værdierne uden x med deres fortegn sammen.

$$f(x)=12-15+6=3$$

- find funktionforskriften: $y-y_1=m\cdot(x-x_1)$


$$y-12=3\cdot (x-1)$$
$$y-12+12=3\cdot(x-1)+12$$
$$y=3x-3\cdot12$$

![[{F278E985-2659-4652-9CEE-60224877F4BF}.png]]


## Differentialregning


|     $f(x)$     |         $f'(x)$          |
| :------------: | :----------------------: |
|      $k$       |           $0$            |
|      $x$       |           $1$            |
|     $x^2$      |           $2x$           |
| $a\cdot x +b$  |            a             |
|     $x^a$      |     $a\cdot x^{a-1}$     |
| $\frac{1}{x}$  | $-(\frac{1}{x^2})=-x^-2$ |
|     $e^x$      |          $e^x$           |
| $e^{k\cdot x}$ |  $k\cdot e^{k\cdot x}$   |
|     $a^x$      |     $ln(a)\cdot a^x$     |
|    $ln(x)$     |      $\frac{1}{x}$       |
|    $sin(x)$    |         $cos(x)$         |
|    $cos(x)$    |        $-sin(x)$         |
|    $tan(x)$    |       $tan^2(x)+1$       |


## Differentielregneregler


|        Operation         |                               Regl                                |
| :----------------------: | :---------------------------------------------------------------: |
|         Addition         |                      $(f+g)'(x)=f'(x)+g'(x)$                      |
|        Subtaktion        |                      $(f-g)'(x)=f'(x)-g'(x)$                      |
|         Produkt          |        $(f\cdot g)'(x)=f'(x)\cdot g(x)  + f(x)\cdot g'(x)$        |
|         Kvotient         | $\frac{f}{g}'(x)=\frac{f'(x) \cdot g(x)-f(x)\cdot g'(x)}{g(x)^2}$ |
| Skalering for c konstant |                  $(c \cdot f)'(x)=c\cdot f'(x)$                   |
