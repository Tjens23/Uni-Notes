---
tags:
  - Notes
links: "[[Software Maintenance Lecture 1]]"
creation date: 2025-09-06 15:39
modification date: Saturday 6th September 2025 15:39:40
semester: 5
year: 2025
---


---
# [[Software Maintenance Lecture 1 Notes]]

---



## **Course Overview**

- **Weight:** 5 ECTS (0.083 full‑time equivalent)
- **Prerequisites**
    - Advanced skills in **object‑oriented programming** (≈ 12.5 ECTS)
    - **Software Engineering** covering process modeling, requirements, analysis, design, architecture (≈ 20 ECTS)
    - Experience with **project teamwork**
- **Learning outcome:** Ability to **maintain larger existing software projects**
- **Teaching language:** English or Danish
    

##  Examination & Portfolio**

- **Exam format:** Written report submitted on campus
- **Assessment:** Individual portfolio evaluated on a **7‑point grading scale**
- **Portfolio task:** **Refactor JHotDraw** features according to **Clean Code** principles (mandatory individual examples)

##  Introduction & Motivation**

- **Software is everywhere** – pervasive in daily life and industry
- **Internet in everything** – connectivity drives software proliferation
    

> **Definition:** _Essential properties_ are inherent to software (e.g., complexity, changeability), whereas _accidental properties_ stem from implementation choices (e.g., programming language, hardware platform).

##  Software Engineering History**

- **Ad‑hoc era** – programmers recruited from hardware engineering and mathematics backgrounds
- **1950s:** Software began to be **separated from hardware**
- **Later:** **Software engineering** emerged as an independent discipline
    

##  Paradigms**

### **⚙️ Ad‑hoc**

- Informal, undocumented processes
- Relied on individual expertise

### ** Waterfall**

- **Linear process** resembling construction/manufacturing
- Intuitively appealing metaphor but assumes fixed requirements
    
###  Agile**

- Iterative, incremental development
- Emphasizes flexibility and rapid feedback
    

###  Agile vs. Waterfall**

- **Agile:** embraces change, frequent releases, close stakeholder collaboration
- **Waterfall:** sequential phases, heavy upfront planning, limited adaptability

##  Requirements Volatility & CHAOS Report**

- **Requirements volatility:** change rate of **2–3 % per month** (Casper‑Jones)
- **Standish Group CHAOS reports** (published annually since 1994)
    - Analyze ≈ 50 000 projects worldwide
    - Success defined by **on‑time**, **on‑budget**, and **satisfactory** results
        

## ** Software Life‑Span Models**

| Model                  | Core Idea                                        | Typical Stages                                                                       | Main Advantage                                              |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Staged Model           | Linear progression from conception to retirement | Conception → Development → Operation → Maintenance → Retirement                      | Simple, easy to understand                                  |
| Versioned Staged Model | Adds version control to staged flow              | Same as Staged + Versioning (major/minor releases)                                   | Supports parallel development of multiple versions          |
| V-Model                | Emphasizes verification & validation             | Requirements ↔ Test Planning, Design ↔ System Testing, Implementation ↔ Unit Testing | Strong quality focus, clear test traceability               |
| Prototype Model        | Builds early prototypes to refine requirements   | Prototype → Evaluation → Refined Prototype → Final System                            | Reduces requirement uncertainty, early stakeholder feedback |


> **Definition:** A **software life‑span model** provides a **simplified, comprehensive view** of the entire software engineering discipline, describing the stages a product undergoes from conception to death.

##  Reengineering**

- Systematic **remodeling** of existing software to improve structure, performance, or maintainability without altering external behavior
    

## Summary of Key Points**

- **Software as a product** since the 1950s, facing intrinsic difficulties:
    - **Complexity** – large, interdependent components
    - **Invisibility** – lack of physical representation
    - **Changeability** – frequent updates required
    - **Conformity** – must fit evolving standards and environments
    - **Discontinuity** – rapid technology turnover
        
- **Three primary paradigms** coexist: **Ad‑hoc**, **Waterfall**, **Iterative/Agile**
    
- **Life‑span models** (Staged, Versioned Staged, V‑Model, Prototype) help organize development, maintenance, and evolution activities across a software system’s entire existence.