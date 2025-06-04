---
tags:
  - Notes
links: "[[Math Lecture 1]]"
creation date: 2024-11-09 15:50
modification date: Saturday 9th November 2024 15:50:34
semester: 3
year: 2024
Lecture: Lectures/Math/Notes
---


---
# Math Lecture 1 Notes

---

## Intro til Set-Teori

- Set-Teorien går ud på, at vi har en liste af data som vi ønsker at sammeenligne med hindanden gennem adskillige operationer.
- Vi plejer, at bruge tuborgklammerne til at definere $\{set\}$ værdierne.
- Allle værdier indee i Set-Teorien kan både være bogstaver, tal, operationstegn etc.


## Intersektionen mellen Sets $\cap$

- Intersektionen mellem sets  går ud  på at sammenligne to lister med hinanden og derved udskrive om der er værdier til fællesskab i resultatet
- intersektionen benævnest med tagnet: $\cap$ (cap)

### Eksempel:

$$A=\{1,2,3,4,5\}$$
$$B=\{4,5,6,7,8\}$$

- Værdierne sammenlignes, og ses at $4$ og $5$ er tilfælles ved begge set-teorier. Derfor skrives følgende:


$$A\cap B=\{1,2,3,\dots\} \cap \{4,5,6\dots\}$$


$$A\cap B = \{4,5\}$$


## Unionen mellem Sets $\cup$

- Intersektionen mellem sets  går ud  på at sammenligne to lister med hinanden og derved udskrive all tal sammen som et resultat uden noget duplikationer af intersektionsværdieren. Unionen benævnes med  taget: $\cup$


### Eksempel

$$A=\{1,2,3,4,5\}$$
$$B=\{4,5,6,7,8\}$$

- Værdierne sammenlignes og skrives allle værdierne samlet uden duplikationer af 5 og 5 da de er intersekteret. derfor bliver resultatet :

$$A\cup B= \{1,2\dots\} \cup \{4,5\dots\}$$
$$A\cup B = \{1,2,3,4,5,6,7,8\}$$


## Subtraktionen mellen Sets \
 ## Subtraktionen mellem sets går ud på, at lave subtraktion mellem to lister og derved udskrive de tal som står på den  "første set-liste"der ikke intersektere med den "anden set-liste". subtaktionen benævnes med tegnet: \


### Eksempel


$$A=\{1,2,3,4,5\}$$
$$B=\{4,5,6,7,8\}$$

- Set-B bliver ignoreret samt de værdier soim er fælles mellem de to ses. Det resterende af set-b skrives. Derfor bliver resultatet:


$$A\backslash B = \{1,2,3,4,5\} - \{4,5,6,7,8\}$$
$$A\backslash B= \{1,2,3,\cancel{4,5}\} - \{\cancel{4,5,6,7,8}\}$$
$$A\backslash B=A-B=\{1,2,3\}$$


## Længden eller magnituden af Sets |S|

- Længden af Sets, kan findes ved at tæller de enkelte elementer i talsættet. Længden er også kaldt for magnituden, og kan benævnes med tegnet $||$


### Eksempel


$$A=\{1,2,3,4,5\}$$
$$B=\{4,5,6,7,8\}$$

- Længden af ekelte sets, skrives på følgende måde:
	- $A=|5|$ fordi der er 5 tal inde i
	- $B=|5|$ fordi er er 5 tal inde i

- Længden af subtraktions-set fra sidste opgave:

$$A\backslash B = \{1,2,3,4,5\} - \{4,5,6,7,8\}$$
$$A\backslash B= \{1,2,3,\cancel{4,5}\} - \{\cancel{4,5,6,7,8}\}$$

$$A\backslash B=A-B=\{1,2,3\}$$
$$|A\backslash B| = 3$$

## Cardinality i sets S|1

- Cardinality er hvor man fjerner den værdi fra selve settet og derved udskriver de resternde set.


### Eksempel:

$$A=\{1,2,3,4,5\}$$

$$A|3=\{1,2,4,5\}$$



## Subset og Parentset 

- Parentset er karakteriseret for den set, der runner alle tallene for subset. Hvorimod subset som inkluderer en portion af de tal som findes i parentset.


### Eksempel


$$A= \{1,2,3,4,5\}$$
$$B=\{4,5\}$$
- Parentset er A da den indeholder alle tal fra subset
- subset er B da den indeholder nogle tal for parentset (4 og 5)


## Regler for uligheder


- Addition af et tal: hvis $a < b$, så $a\pm c<b \pm c$
- Positiv multiplikation: hvis $a<b$ og $c>0$, så $a\cdot c < b \cdot c$
- Negativ multiplikation: Hvis $a < b$ og $c < 0$ så $a\cdot c < b\cdot c$
- Inverse: hvis $a>0$, så $\frac{1}{a}>0$
- Ordre af inverse: hvis $0<a < b$, så $\frac{1}{b}<\frac{1}{a}$ 


## Intervaller 

- Intervaller er en *subset* af Reelle Tal som er defineret af uligheder.
- Der er forskellige typer:
  - **Åben:** $(a, b) = \{x \in \mathbb{R} \mid a < x < b\}$ (alle tal mellem $a$ og $b$)
  - **Lukket:** $[a, b] = \{x \in \mathbb{R} \mid a \leq x \leq b\}$ (alle tal mellem $a$ og $b$, er inkluderet)
  - **Halv-Åben:**
    - $(a, b] = \{x \in \mathbb{R} \mid a < x \leq b\}$ (alle tal mellem $a$ og $b$, hvor $b$ er inkluderet)
    - $[a, b) = \{x \in \mathbb{R} \mid a \leq x < b\}$ (alle tal mellem $a$ og $b$, hvor $a$ er inkluderet)
    - $[a, \infty) = \{x \in \mathbb{R} \mid a \leq x\}$ (alle tal er større end $a$)



### Eksempel på intervaller


$$x-4\geq 0$$

$$x-4+4=0+4$$

$$x\geq=4$$
---

$$-3x < 9$$
$$-3+3x<9+3$$
$$x<12$$



