

## Ækvivalensrelationer (Equivalence Relations)

### Repetition (Review)

- En relation $\mathbb{R}$ på en mængde $S$ er en delmængde af $S\times S$. Når $(x,y)\in \mathbb{R}$, siges $x$ at stå i relation til $y$ Ofte skrives $x \sim y$ og relationen selv betegnes $\sim$
- En **ækvivalensrelation** kaldes en relation hvis der for alle $x,y,z\in S$ gælder:
	- $x\sim x$(**Refleksivitet**)
	- $x\sim y \rightarrow y \sim x$ (**Symmetri**)
	- $x\sim y \wedge y \sim z \rightarrow x \sim z$ (**Transitivitet**)
- En ækvivalensrelation deler $S$ i **disjunkte delmængder**, også kaldet en **partition**.


## Ækvivalensrelationer på en Grafs Knuder (Equivalence Relations on Graph Nodes)

### Uorienterede Grafer (Undirected Graphs)
- For $v, u \in V:v \sim u \leftrightarrow$ der er en (uorienteret ) sti mellen $u$ og $v$ 
-  Giver en partition af grafens knuder $V$.
- - Disse partitioner kaldes grafens **sammenhængskomponenter (CC'er)**.
- **Findes ved**: DFS eller BFS med global ydre loop.
    - Hvert kald fra ydre loop opdager præcis knuderne i én sammenhængskomponent.
    - Et kald opdager præcis de knuder, som kan nås fra $s$ via en sti af hvide knuder på tidspunktet for kaldet.
- **Tidskompleksitet**: $O(n+m)$, hvor nn er antallet af knuder og mm er antallet af kanter.



### Orienterede Grafer (Directed Graphs)

- For $v,u\in V:v\sim u$ der er en (orienteret) sti fra $u$ til $v$ **OG** der er en (orienteret) sti fra $v$ til $u$
- Giver en partition af grafens knuder $V$.
- Disse partitioner kaldes grafens **stærke sammenhængskomponenter (SCC'er)**.


## inde Stærke Sammenhængskomponenter (Finding Strong Connected Components)


- **Algoritme**:
    1. Kør DFS på grafen $G$.
    2. Beregn $G^{T}$ (den transponerede graf af $G$, hvor alle kanter er vendt om).
    3. Kør DFS på $G^{T}$, hvor knuderne besøges i rækkefølge efter faldende finish-tid fra det første DFS-kald.
1. **Tidskompleksitet**: $O(n+m)$


## Korrekthed af SCC Algoritme (Correctness of SCC Algorithm)

- **Sætning**: Algoritmen SCC ovenfor er korrekt, dvs. træerne returneret fra det andet kald til DFS repræsenterer præcis GG's SCC'er.
- **Bevis**:
	- Der er en sti $u\leadsto v$ i $G \leftrightarrow$ Der er en sti $v \leadsto u$ i $G^{T}$
	- $u$ og $v$ i samme  SCC i $G \leftrightarrow$ $u$ og  $v$ i samme SCC i $G^{T}$
	- så $G$ og $G^{T}$ har de samme SCC'er


**Lemma 1 & 2**

For en knudemængde $C \subseteq V$ defineres  
$$
f(C) = \max_{v \in C} v.f
$$
(hvor $v.f$ angiver finish-tiden fra første DFS i SCC-algoritmen).

**Lemma 1:** Hvis $C, C'$ er to forskellige SCC'er i $G$, og $(x,y)$ er en kant i $G$ med $x \in C$ og $y \in C'$, da gælder  
$$
f(C) > f(C').
$$

**Lemma 2:** Hvis $C, C'$ er to forskellige SCC'er i $G^T$, og $(x,y)$ er en kant i $G^T$ med $x \in C$ og $y \in C'$, da gælder  
$$
f(C) < f(C').
$$

---

**Bevis for Lemma 1**

Lad $u$ være den første knude i $C \cup C'$ som opdages.

- Case 1: $u \in C$. Her er der en sti fra $u$ til $w$ for alle $w \in C \cup C'$, så udsagnet følger af hvid-sti lemma.

- Case 2: $u \in C'$. Her er der en sti fra $u$ til $w$ for alle $w \in C'$, så af hvid-sti lemma følger  
$$
f(C') = u.f.
$$  
Antag at der fandtes en knude $v \in C$ med $v.d < u.f$. Da $u.d < v.d$ (eftersom $u$ var den først opdagede i $C \cup C'$) giver parentesstrukturen for $d$- og $f$-tider at  
$$
u.d < v.d < v.f < u.f.
$$  
Dvs. at $v$ og $u$ er på stakken samtidig, med $v$ øverst (push’et senest). Da det er en invariant under DFS at der i grafen findes en sti mellem knuderne på stakken (fra tidligere til senere push’ede knuder), ville dette betyde en sti fra $u \in C'$ til $v \in C$. Sammen med kanten $(x,y)$ ville dette medføre at alle knuder i $C \cup C'$ var i samme SCC, i modstrid med at $C$ og $C'$ er to forskellige SCC’er.  
Derfor haves  
$$
v.d > u.f
$$  
for alle $v \in C$, så  
$$
f(C) > u.f = f(C').
$$

---

**Korrekthed af SCC Algoritmen**

Vi viser nu sætningen om korrekthed af SCC-algoritmen ved at vise at for alle $k$ gælder:

1. Knuderne i de $k$ første træer genereret under den anden DFS i SCC-algoritmen udgør hver især en SCC i $G^T$.

2. Da SCC’erne i $G$ og $G^T$ er de samme, og da alle knuder i grafen er i et af træerne, viser dette korrektheden.

Vi viser ovenstående udsagn via induktion på $k$.

- Skridt: Antag sandt for $k$, vis sandt for $k+1$.  
Det $(k+1)$'te træ genereres ved det $(k+1)$'te kald til DFS-Visit i for-løkken i det ydre loop i DFS. Lad $u$ være knude, der kaldes på.

- Hvis vi stiller knuderne op i for-løkkens rækkefølge (efter aftagende $v.f$-værdi), ser situationen sådan ud på tidspunktet for dette kald:

Lad $C$ være SCC'en indeholdende $u$, og lad $T$ være træet genereret af kaldet på $u$. Af induktionsantagelsen udgør de sorte knuder præcis $k$ af grafens SCC’er. Derfor må alle andre SCC’er ligge inden i de hvide knuder, og $C$ er en af disse (da $u$ er hvid).

Eftersom der ved starten af kaldet er en hvid sti fra $u$ til alle $w \in C$, giver hvid-sti lemma at  
$$
C \subseteq T.
$$

Lad $C'$ være en vilkårlig hvid SCC forskellig fra $C$. Pga. for-løkkens rækkefølge ses  
$$
u.f = f(C) > f(C').
$$

Hvis der var en kant i $G^T$, som gik fra $C$ til $C'$, ville Lemma 2 give  
$$
f(C) < f(C').
$$

Så ingen kant i $G^T$ kan gå fra $C$ til $C'$. Da DFS-Visit ikke besøger de sorte knuder, kan den derfor ikke forlade $C$. Heraf ses  
$$
T \subseteq C.
$$

Vi har i alt vist  
$$
T = C,
$$  
hvilket viser udsagnet for $k+1$.

- Basis: Samme argument, blot lidt simplere (der er ingen sorte knuder, og $u$ er første knude i rækkefølgen), viser udsagnet for $k=1$.
