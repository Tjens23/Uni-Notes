---
tags:
  - Notes
links: "[[Cloud Computing Lecture 1]]"
creation date: 2025-09-06 15:45
modification date: Saturday 6th September 2025 15:45:27
semester: 5
year: 2025
---


---
# [[Cloud Computing Lecture 1 Notes]]

---



## **Course Overview**

- **Course name:** Cloud Computing Continuum
- **Instructor:** Mahyar T. Moghaddam (mtmo@mmmi.sdu.dk) – Associate Professor, SDU MMMI, Head of DECO lab
- **Co‑instructors:** Charlie Frederik Warnes, Daniel Bermann Schmidt (student assistants)
- **Language:** English
- **Format:** Online lectures, weekly slides, optional books, industry talks, data‑center visits
    

> **Definition – Cloud Computing**  
> “A style of computing in which scalable and elastic IT‑enabled capabilities are delivered as a service to external customers using Internet technologies.” – Gartner


## **Schedule & Timeline**

|Model|Core Idea|Typical Stages|Main Advantage|
|---|---|---|---|
|Staged Model|Linear progression from conception to retirement|Conception → Development → Operation → Maintenance → Retirement|Simple, easy to understand|
|Versioned Staged Model|Adds version control to staged flow|Same as Staged + Versioning (major/minor releases)|Supports parallel development of multiple versions|
|V-Model|Emphasizes verification & validation|Requirements ↔ Test Planning, Design ↔ System Testing, Implementation ↔ Unit Testing|Strong quality focus, clear test traceability|
|Prototype Model|Builds early prototypes to refine requirements|Prototype → Evaluation → Refined Prototype → Final System|Reduces requirement uncertainty, early stakeholder feedback|

- Groups of **6 students** work on the assignment throughout the semester.
    
- Both presentations are prerequisites for the final exam; all group members must present and answer questions.

## **Course Materials & Prerequisites**

- **No strict prerequisites**, but useful background:
    - Component‑based software engineering
    - Software architectures
    - Databases
    - Programming languages
        
- **Materials:** weekly slides, optional textbooks (distributed on request), online resources.


## **Group Work & Grading**

- Form **one group of 6** early in the course.
    
- **Grading components:**
    1. Participation in lectures & labs
    2. Project deliverables (V1, V2)
    3. Two mandatory presentations
    4. Final exam (only for groups that completed presentations)
        

> **Policy – Generative AI**  
> Use of GenAI is allowed **only if** you cite it and provide a critical analysis/validation of its output.



## **Cloud Business Drivers**

1. **Capacity Planning** – matching future IT demand with resource supply.
    - Strategies: Lead (anticipate), Lag (react), Match (incremental).
2. **Cost Reduction** – aligning IT expenses with business performance.
    - Distinguish **capital** (acquisition) vs. **operational** (ownership) costs.
3. **Organizational Agility** – ability to scale quickly in response to market changes.


| Driver                 | Goal                              | Typical Challenge                            |
| ---------------------- | --------------------------------- | -------------------------------------------- |
| Capacity Planning      | Minimize over-/under-provisioning | Accurate demand forecasting                  |
| Cost Reduction         | Lower total cost of ownership     | Balancing CAPEX & OPEX                       |
| Organizational Agility | Rapid response to change          | Budget constraints, reliability under stress |


## Cloud Computing Definitions & Paradigms**

> **Definition – Utility Computing**  
> “The service provider supplies needed resources and charges the customer based on usage.”

### **Major Paradigms**

| Paradigm              | Core Idea                                              | Typical Use                                 |
| --------------------- | ------------------------------------------------------ | ------------------------------------------- |
| Distributed Computing | Multiple systems collaborate on a single problem       | Fault-tolerant services                     |
| Parallel Computing    | Simultaneous execution of sub-tasks on many processors | High-performance scientific tasks           |
| Cluster Computing     | Nodes work as a single machine for scalability         | Web hosting, data processing                |
| Grid Computing        | Virtual supercomputer across many sites                | Large data-set analysis                     |
| Utility Computing     | Pay-per-use resource rental                            | Dynamic workloads                           |
| Edge Computing        | Compute close to the data source                       | IoT, low-latency apps                       |
| Fog Computing         | Intermediate layer between edge and cloud              | Real-time analytics, bandwidth optimization |


## Deployment Models

|Model|Description|Pros|Cons|
|---|---|---|---|
|Public Cloud|Multi-tenant infrastructure owned by a provider|Easy access, cost-effective|Shared security boundaries|
|Private/Enterprise Cloud|Exclusive use by a single organization (on- or off-prem)|Strong security, customization|Higher cost, limited scalability|
|Hybrid Cloud|Combination of private & public clouds with data/app portability|Cost balance, privacy, disaster recovery|Complexity of integration|
|Multi-Cloud|Simultaneous use of two or more clouds (public or private)|Reduce vendor lock-in, geographic distribution|Management overhead|

## Scaling Concepts

**Scaling** = ability of an IT resource to handle varying demand.

|Type|Direction|Action|
|---|---|---|
|Horizontal Scaling|Out / In|Add or remove instances (scale out/in)|
|Vertical Scaling|Up / Down|Replace a node with a larger or smaller instance (scale up/down)|


> **Definition – Horizontal Scaling**  
> “The allocating or releasing of IT resources across multiple instances.”

> **Definition – Vertical Scaling**  
> “Replacing an existing resource with one of higher or lower capacity.”


## **Cloud Provider Histories**

- **Amazon Web Services (AWS)** – From an e‑shop (1990s) to a service company (2003); introduced Elastic Compute Cloud (2006).
    
- **Google Cloud Platform (GCP)** – Launched 7 Apr 2008 with App Engine; now the fastest‑growing public cloud (+40 % QoQ).
    
- **Microsoft Azure** – Announced Oct 2008, launched Feb 2010 as Windows Azure; rebranded 2014; focuses on data, AI, and hybrid solutions (Azure Arc).


## **GCP Labs & Credits**

- **Optional** Certified Cloud Engineer path: labs on [cloudskillsboost.google](https://www.cloudskillsboost.google).
    
- **Certification exam** covers: environment setup, solution planning, operation, security.
    
- **Credits:** each student receives a $50 voucher (renewable once).
    - Redeem by 31 Dec 2025.
    - Use university email for account creation; avoid personal credit cards.
        

**Steps to claim a voucher**
1. Visit the provided coupon URL.
2. Enter school email and name.
3. Confirm via the email link.
4. Redeem the code before the deadline.
    

> **Note:** GCP labs are **not** part of the course grade but are encouraged for skill development.


## **Classroom Expectations**

- Attend and prepare for every lecture.
- Practice examples, follow the project workflow, and meet all deadlines.
- Actively contribute to discussions and group presentations.
- Adhere to the **Generative AI** citation policy.