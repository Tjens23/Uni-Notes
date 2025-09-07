---
tags:
  - Notes
links: "[[Cyber Security Lecture 1]]"
creation date: 2025-09-06 12:38
modification date: Saturday 6th September 2025 12:38:58
semester: 5
year: 2025
---


---
# [[Cyber Security Lecture 1 Notes]]

---



## Objectives

- **Introduce** the basics of **cybersecurity**
- **Develop** awareness and understanding of security concepts
- Identify **relevant activities** and challenges
- Explore ways to achieve a **higher level of security**
- Cover **threats, vulnerabilities, and penetration testing**
- Provide **conceptual foundations** and **hands‑on experience**


## Motivation


- Cyber criminals have stolen **> $1 trillion** USD in funds and assets.
- “The cybersecurity crisis is a fundamental failure of architecture.” – _Mowbray, T. J._
    
    
- Common root causes:
    - **Simple bugs**
    - **Mis‑configuration**
    - **Unintended side effects** from system complexity
    - **Human factors** (mistakes or malicious intent)

**Countermeasures** include best‑practice policies, pattern checks, training, and experience.

## Definition of Cybersecurity

> *“A set of activities and other measures intended to protect from attack, disruption, or other threats—computers, computer networks, related hardware and devices, software and the information they contain and communicate.” – Fischer, 2016*


> *“Measures and controls that ensure **confidentiality, integrity, and availability** of information system assets…” – NISTIR 7298, 2013*


- **Fuzzy term** – no single silver bullet.
- **Iterative, ongoing process** rather than a one‑time fix.

## CIA Triad

|Principle|Goal|Typical Controls|
|---|---|---|
|Confidentiality|Prevent unauthorized access to sensitive data|Encryption, access control, authentication|
|Integrity|Guard against unauthorized modification or deletion|Checksums, digital signatures, version control|
|Availability|Ensure data/services are accessible when needed|Redundancy, backups, DoS mitigation|
**Confidentiality $\approx$ privacy** – data is classified by potential damage; privileged personnel receive special training.

## Threats & Attack Surface

**Attack vectors** are the ways an adversary can interact with a system (network, physical machine, software, human).   The **attack surface** is the **sum of all attack vectors**.

### **Visual Overview**

![Computer setup illustrating a basic system](https://api-turbo.ai/e5863bac-0186-4527-b7ff-d71900b6235b/ab7ee5a6-a0ab-46c8-885a-979bc50c48fc.jpeg)


_The diagram shows a typical workstation (monitor, CPU, keyboard, mouse). Understanding the components helps identify entry points for attackers._

![Expanded view of the same workstation](https://api-turbo.ai/e5863bac-0186-4527-b7ff-d71900b6235b/f2f8946c-68b2-4716-bf93-256d72c35ae8.jpeg)

  
_An additional perspective emphasizes peripheral connections that can broaden the attack surface._

#### **Common Vulnerability Types**

![Vulnerability overview](https://api-turbo.ai/e5863bac-0186-4527-b7ff-d71900b6235b/04196916-5bcc-45a6-b4b4-54e596bb34e4.jpeg)

  
_The image lists reachable and exploitable weaknesses, such as open ports, internal services, data‑processing code, and social‑engineering targets._

**Stakeholder perspectives**
- **Attacker:** expands exposed interfaces.
- **Operator:** limits surface area.
- **Designer:** builds systems with minimal attack vectors.
    
**Key questions**
1. What do we want to protect?
	1. The **confidentiality, integrity, and availability (CIA)** of information‑system assets – data, software, hardware, network services, and the communications they carry.
2. How is the protected entity handled?
	1. Through **security controls** such as encryption, access‑control/authentication, integrity checks (checksums, digital signatures), redundancy/backups, and monitoring (IDS/IPS, firewalls). Policies, training, and best‑practice processes enforce these controls throughout the system lifecycle.
3. Where are the vulnerabilities?
	1. In any **attack surface**: open ports, mis‑configured services, insecure code, outdated software, and human factors (phishing, weak passwords, insider mistakes). They appear at network, host, application, and user layers.
4. How can we secure it?
	- **Reduce the attack surface** (close unnecessary ports, harden configurations).
	- **Apply layered defenses** (firewalls, IDS/IPS, patch management, encryption).
	- **Strengthen people** (security awareness training, least‑privilege policies).
	- **Continuously test and improve** (regular penetration testing, vulnerability assessments, incident‑response drills).


## Malware Types

|Malware|Characteristics|Typical Behaviors|
|---|---|---|
|Virus|Self-replicates, needs user action (e.g., opening email attachment)|Consumes resources, spreads via email/USB|
|Trojan|Disguised as legitimate software|Downloads additional payloads, contacts C2 servers, logs keystrokes|
|Spyware / Keyloggers|Monitors user activity|Collects web movements, cookies, keystrokes|
|Logic Bomb|Triggers on a specific condition (date, count, presence)|Disrupts system availability when condition met|
## Basic Security Devices

- **Firewall:** filters network traffic.
- **Proxy server:** masks internal IP addresses.
- **Intrusion Detection System (IDS):** monitors traffic for suspicious activity.
- **Intrusion Prevention System (IPS):** IDS + active countermeasures.

## Penetration Testing

> “Testing the security of systems from the attacker’s perspective; a simulated attack with a fixed goal performed within a limited time.”

### Differentiation

- **Not** a vulnerability assessment (which merely identifies weaknesses).
- **Complementary** to other security measures; does **not** guarantee security.

### Typical Steps (Numbered)

1. **Gather Information** – IP ranges, public data, employee info.
2. **Scan Networks** – Identify live hosts, open ports, service versions.
3. **Fingerprinting** – Determine operating systems and software specifics.
4. **Identify Vulnerable Services** – Match findings to known exploits.
5. **Exploit Vulnerabilities** – Create proof‑of‑concept attacks (carefully).
6. **Document Findings & Recommendations** – Suggest remediation actions.


## Tentative Schedule (Exercises & Topics)

|Week|Date|Topic|Exercise|
|---|---|---|---|
|1|03-09|Introduction & Set-up|Exercise 1|
|2|10-09|Penetration Testing – Metasploit|Exercise 2|
|3|17-09|Security Assessment|Exercise 3|
|4|24-09|Social Engineering|Exercise 4|
|5|01-10|Malware & SQL Injection|Exercise 5|
|6|11-10|Test Exam & Midterm Evaluation|-|
|7|15-10|Autumn break|-|
|8|22-10|Firewalls & Intrusion Detection|Exercise 6|
|9|29-11|Denial of Service|Exercise 7|
|10|05-11|Staying on Top (advanced topics)|-|
|11|12-11|Threat Modelling|Exercise 8|
|12|19-11|Cryptography – Crypto Challenge|Exercise 9|
|13|26-12|Exam Q&A & Evaluation|Final submission|

## Resources

Books

- _Computer Security Fundamentals_ – Chuck Easttom
- _Penetration Testing Fundamentals_ – Chuck Easttom
- _Computer Security: Principles and Practice_ (4th) – William Stallings & Lawrie Brown
- _Threat Modeling: Designing for Security_ – Adam Shostack
- _Penetration Testing: A Hands‑On Introduction to Hacking_ – Georgia Weidman
    

Online Sources
- Exploit Database, CVE, CWE, CERT, Vulnerability Factory, Phrack, OWASP, F‑Secure threat feeds.

Standards & Legal
- NIST, ISOC, ITU‑T, ISO – security management and architecture.
- Computer Security Act (1987), OMB Circular A‑130, HIPAA, GDPR (2018).


## Summary
- **Cybersecurity** is an iterative, domain‑specific process with no silver bullet.
- Core focus: **What** to protect, **how** to handle it safely, **where** attacks can occur, **how** to mitigate them, and **what** to do in worst‑case scenarios.
- Shift perspective **between designer and attacker** to uncover hidden weaknesses.