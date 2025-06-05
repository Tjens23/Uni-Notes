---
creation date: 2025-06-04 14:18
modification date: Wednesday 4th June 2025 14:18:24
tags:
  - Assignments
year: 2025
semester: 4
links:
---

---
# [[AI Lecture 7 Assignments]]

## Question 1

Consider two medical tests, A and B, for a virus. Test A is 95% effective at recognizing the virus when it is present, but has a 10% false positive rate (indicating that the virus is present, when it is not). Test B is 90% effective at recognizing the virus, but has a 5% false positive rate. The two tests use independent methods of identifying the virus. The virus is carried by 1% of all people. Say that a person is tested for the virus using only one of the tests, and that test comes back positive for carrying the virus. Which test returning positive is more indicative of someone really carrying the virus? Justify your answer mathematically.

$$P(A\mid B)=\frac{P(B\mid A)\cdot P(A)}{P(B)}$$
where:

$$P:\text{Probability. The function P() denotes the probability of an evnet}$$
$$A: \text{Represents the event of interest}$$
$$B: \text{Represents the observed evidence}$$

|        | Recognizes Virus When Present | False Positive Rate |
| ------ | ----------------------------- | ------------------- |
| Test A | 95%                           | 10%                 |
| Test B | 90%                           | 5%                  |
The Prevalence of vrius: $P(V)=0.01=1\%$

expanding the equation we get: 
$$P(V\mid +)=\frac{P(+\mid V)\cdot P(V)}{P(+)}$$
where:

$$P(V\mid +): \text{Probability of having virus given positive test}$$
$$P(+\mid V): \text{Test semsitivity (detecting virus when present)}$$
$$P(V):\text{Prior probability of having the virus (prevalence)}$$
$$P(+): \text{Total Probability of a positive test result}$$

Theirs two outcomes: 
- Either you test positive and you have the virus
- You test positive and you dont have the virus

can be calculated by using formular: 

$$P(V\mid +)=\frac{P(+ \mid V)\cdot P(V)}{P(+\mid V)\cdot P(V)+P(+\mid \neg V)\cdot P(\neg V)}$$



### Test A  Calculation 

$P(+\mid V) = 0.95$
$P(+ \mid \neg V)= 0.10$
$P(V)=0.01$ 
$P(\neg V)=0.99 (\text{Because 1-0.01 = 0.99})$

$$\text{Test A}=\frac{0.95\cdot 0.01}{0.95\cdot0.01+0.10\cdot0.99}\cdot100=8.76\%$$

So there is a $8.76\%$ chance that's a true positive
### Test B Calculation 

$P(+\mid V) = 0.90$
$P(+ \mid \neg V)= 0.05$
$P(V)=0.01$ 
$P(\neg V)=0.99 (\text{Because 1-0.01 = 0.99})$

$$\text{Test B}=\frac{0.90\cdot 0.01}{0.90\cdot 0.01+0.05\cdot 0.99}\cdot 100 = 15.38\%$$

So there is a $15.38\%$ chance that's a true positive

### Conclusion
Given the calculations the **Test B** is the best


## Question 2

After your yearly checkup, the doctor has bad news and good news. The bad news is that you tested positive for a serious disease and that the test is 99% accurate (i.e., the probability of testing positive when you do have the disease is 0.99, as is the probability of testing negative when you don’t have the disease). The good news is that this is a rare disease, striking only 1 in 10,000 people of your age. Why is it good news that the disease is rare? What are the chances that you actually have the disease?


$P(+\mid V) = 0.99$
$P(V)=\frac{1}{10.000}=0.0001$
$P(+\mid \neg V) = 1-0.99 =0.01$
$P(\neg V)=1-0.0001=0.9999$



$$P(V\mid +)=\frac{P(+ \mid V)\cdot P(V)}{P(+\mid V)\cdot P(V)+P(+\mid \neg V)\cdot P(\neg V)}$$

$$\frac{0.99\cdot 0.0001}{0.99\cdot0.0001+0.01\cdot 0.9999}\cdot100=0.98\%$$

### Conclusion

Bad news are that I tested positive for a virus and the test is 99% accurate, however despite testing positive, there's only about a 1% chance that the person actually has the condition


## Question 3

Would it be rational for an agent to hold the three beliefs $P(A)=0.4$, $P(B)=0.3$, and $P(A\vee B)=0.5$? If so, what range of probabilities would be rational for the agent to hold for $A\wedge B$?

use formular:

$$P(A \vee B)=P(A)+P(B)-P(A\wedge B)$$


plugin the values:

$$P(A\vee B)= 0.4+0.3-0.5$$
$$=0.7-0.5$$
$$=0.2$$

### Verifying Rationality

for probabilities to be rational the intersection of two events can't be greater than the probability of either  events:

$$0\leq=(A\wedge B)\leq min(P(A),P(B))$$

in our case:

$$0\leq0.2\leq min(0.4,0.3)=0.3$$


### Conclusion

Yes it is rational because the value is between $0$ and $1$



## Question 4:  Would it be rational for an agent to hold the three beliefs $P(A)=0.4$, $P(B)=0.3$ and $P(A\wedge B) =0.7$

use formular:

$$P(A \vee B)=P(A)+P(B)-P(A\wedge B)$$


plugin the values:

$$P(A\vee B)= 0.4+0.3-0.7$$
$$=0.7-0.7$$
$$=0$$


### Conclusion 

No it's not rational.... A and B have a mutually exclusive relationship meaning that two events cannot happen at the same time. If one event occurs, the other cannot occur.


## Question 5: 5.Given the full joint distribution shown bellow, calculate the following:


- P(toothache)
- P(cavity)
- $P(\text{toothache} \wedge \text{cavity})$
- $P(\text{toothache}\vee cavity)$
- $P(\text{toothache} \mid \text{cavity})$
- $P(\text{cavity}\mid\text{toothache, catch})$
- $P(\text{toothache}\mid\text{cavity, catch})$
- Is toothache conditionally independent of catch given cavity? In other words: Does knowing that there is a catch have any effect on having toothache, when you that there is cavity? Justify your answer mathematically and describe(In a few words)what conditional independence means


![[{B0031D5A-0536-49FA-8029-4E2196F1E6F1}.png]]


Notation: 
- T: Toothache
- C: Cavity
- H: Catch


### Calculation of $P(T)$

sum all the probabilities where toothache is true:

$$P(T)=0.108+0.012+0.016+0.064=0.2$$

### Calculation of $P(C)$

sum all the probabilities where cavity is true:

$$P(C)=0.108+0.012+0.072+0.008=0.2$$


### Calculation of $P(T \wedge C)$

sum all the probabilities where cavity and toothache is true:

$$P(T\wedge C)=0.108+0.012=0.12$$


### calculation of $P(T\vee C)$

subtract from 1 where the person does **NOT** have a toothache **AND** cavity

$$P(T\vee C)=1-P(\neg T \wedge \neg C)$$
$$=1-0.576$$
$$=0.424$$


### calculation of $P(T \mid C)$

$$P(T\mid C)=\frac{P(T\wedge C)}{P(C)}$$
$$=\frac{0.12}{0.2}$$
$$=0.6$$


### Calculation of $P(C\mid\text{T, H})$

$$P(C\mid\text{T,H})=\frac{P(C\wedge T\wedge H)}{P(T\wedge H)}$$
$$=\frac{0.108}{0.108+0.016}$$
$$=\frac{0.108}{0.124}$$
$$=0.871$$

### Calculations of - $P(T\mid\text{C, H})$

![[{B0031D5A-0536-49FA-8029-4E2196F1E6F1}.png]]

$$P(T\mid\text{C,H})=\frac{P(T\wedge C\wedge H)}{P(C\wedge H)}$$

$$=\frac{0.108}{0.108+0.072}$$
$$\frac{0.108}{0.18}$$
$$0.6$$
# PRACTICE QUESTIONS

## Practice question 1

A company offers two different diagnostic tests, Test X and Test Y, for detecting a rare genetic condition found in 2% of the population. Test X has a sensitivity of 92% and a false positive rate of 8%. Test Y has a sensitivity of 88% and a false positive rate of 4%. The tests are independent. If a person takes only one test and the result is positive, for which test is a positive result more likely to indicate that the person actually has the condition? Justify your answer with calculations.


|        | Recognizes Virus When Present | False Positive Rate |
| ------ | ----------------------------- | ------------------- |
| Test X | 92%                           | 8%                  |
| Test Y | 88%                           | 4%                  |



$$P(V\mid +)=\frac{P(+\mid V)\cdot P(V)}{P(+)}$$
where:

$$P(V\mid +): \text{Probability of having virus given positive test}$$
$$P(+\mid V): \text{Test semsitivity (detecting virus when present)}$$
$$P(V):\text{Prior probability of having the virus (prevalence)}$$
$$P(+): \text{Total Probability of a positive test result}$$


### Test X calculations


$P(+\mid V) = 0.92$
$P(V)=0.02$
$P(+\mid \neg V) = 0.08$
$P(\neg V)=1-0.02=0.98$


$$P(V\mid +)=\frac{P(+ \mid V)\cdot P(V)}{P(+\mid V)\cdot P(V)+P(+\mid \neg V)\cdot P(\neg V)}$$$$P(V\mid +)=\frac{0.92\cdot 0.02}{0.92\cdot0.02+0.08\cdot 0.98}\cdot 100=19\%$$

### Test Y calculations


$P(+\mid V) = 0.88$
$P(V)=0.02$
$P(+\mid \neg V) = 0.04$
$P(\neg V)=1-0.02=0.98$

$$P(V\mid +)=\frac{0.88\cdot 0.02}{0.88\cdot0.02+0.04\cdot 0.98}\cdot 100\approx31\%$$



## Practice question 2: Would it be rational for an agent to hold the following three beliefs: $P(C)=0.5 \quad P(D)=0.6 \quad P(C\cap D)=0.2$ if so, what value for $P(C\cup D)$ would be rational for the agent to hold? 


Use formular $$P(C\cup D)=P(C)+P(D)-P(C\cap D)$$


$$P(C\cup D)=0.5+0.6-0.2$$
$$=1.1-0.2$$
$$=0.9$$

### Conclusion

Yes it is rational because the value is between 0 and 1
