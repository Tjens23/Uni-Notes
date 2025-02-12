---
tags:
  - Notes
links: "[[Math Lecture 6]]"
creation date: 2024-11-29 11:27
modification date: Friday 29th November 2024 11:27:51
semester: 3
year: 2024
---


---
# [[Math Lecture 6 Notes]]

---



# Newtons Raphsons Metode

- For, at kunne beregne Newtons Metode anvendes følgende formel:

$$x_{n+1}=n_x-\frac{f(x_n)}{f'(x_n)}$$
- $x_n$ er en definerede værdi.
- $f(x_n)$ er resultatet af x-værdien indsat i funktionsligningen.
- $f’(x)$ er resultatet af x-værdien indsat i den differentierede ligning.

## Eksempel


$$f(x)=x^3-4x^2+1=0$$

$$x_1=0.5$$


- formlen anvendes:


$$x_{1+1}\rightarrow x_{2}=0.5-\frac{f(0.5)}{f'(0.5)}$$


- Nu finder vi værdierne fra formlen såsom $f(0,5)$ og $f’(0,5)$.

$$f(0.5)=0.5^3-4\cdot0.5^2+1=0$$







# L - Hospitalsreglen

L'Hôpitals regel benyttes, når man skal bestemme grænseværdier for brøker, hvis tæller og nævner er funktioner, der opfylder visse betingelser. Følgende regel gælder, når grænseværdien for en brøkfunktion ønskes undersøgt for $x$ gående imod $a$, hvor $a$ kan være et reelt tal, $a^{+}, a^-$, samt $\pm\infty$

$$\lim_{x\rightarrow a}(\frac{f(x)}{g(x)})=\lim_{x\rightarrow a}(\frac{f'(x)}{g'(x)})$$

hvor  $a$ kan være talværdier eller $\pm\infty$ . Betingelserne for at ovenstående gæler er:

- Både $f$ og $g$ er differentiable
- Enten $\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=0$ eller $\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=\infty$


## Eksembel

Bestem grænseværdien:
$$\lim_{x\rightarrow3}\frac{cos(\pi\cdot \frac{x}{2})}{x²-x-6}$$

sæt 3 ind på x's plads

$$\lim_{x\rightarrow3}\frac{cos(\pi\cdot \frac{3}{2})}{3²-3-6}=\frac{0}{9-3-6}=\frac{0}{0}$$


Vi bruger L - Hospitalsreglen

$$\lim_{x\rightarrow 3}{x\rightarrow3}\frac{cos(\pi\cdot \frac{x}{2})}{x²-x-6}=\lim_{x\rightarrow 3}\frac{-sin(\pi\cdot\frac{x}{2})\cdot\frac{\pi}{2}}{2x-1}$$


sæt 3 in på x's plads

$$\lim_{x\rightarrow 3}\frac{-sin(\pi\cdot\frac{3}{2})\cdot\frac{\pi}{2}}{2\cdot3-1}=\frac{1\cdot\frac{\pi}{2}}{5}=\frac{\pi}{10}$$
