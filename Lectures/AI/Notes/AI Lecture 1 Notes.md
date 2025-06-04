---
tags:
  - Notes
links: "[[AI Lecture 1]]"
creation date: 2025-02-11 16:22
modification date: Tuesday 11th February 2025 16:22:13
semester: 4
year: 2025
---


---
# [[AI Lecture 1 Notes]]

---



## Course Overview
The course serves as an introductory survey of AI techniques, designed for students with little to no prior exposure to the subject. The primary goals include understanding AI methods and applying them to real-world problems. Python is recommended as the "AI programming language" for this course.

The textbook for the course is: _Artificial Intelligence: A Modern Approach_ by S. Russell and P. Norvig.

![Artificial Intelligence: A Modern Approach Textbook Cover](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/2aecc1b6-6217-4ab2-905f-9618330c0e7c.jpeg)

Students are expected to have programming knowledge, and examples will be given in Python. Ashkan Zare ([zare@mmmi.sdu.dk](mailto:zare@mmmi.sdu.dk)) will be holding labs on Mondays from 14:00-16:00. There will be a written exam with multiple-choice questions, worth 2, 3, or 4 points depending on the difficulty. No notes are allowed. A portion of the exam (10-20%) will involve running code. Permitted IDEs for the exam are PyCharm and Visual Studio Code

## Defining AI: Human vs. Rational

AI can be defined through different lenses, contrasting human-like and rational approaches:

1. Think like a human
2. Act like a human
3. Think rationally
4. Act rationally

##  AI Definition 1: Thinking Humanly

This approach involves studying the brain as an information processing machine, incorporating cognitive science and neuroscience.

![Collage of brain function and imaging](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/9bd82b53-a1fd-4c85-86b3-dc177e82309d.jpeg)

Building a brain-like machine poses significant challenges, as even with extensive processing power, current technology only approaches a fraction of the human brain's scale.

## 🎭 AI Definition 2: Acting Humanly

This definition is epitomized by the **Turing Test**.

![Diagram illustrating the Turing Test](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/7f92168f-6986-4adb-ba87-7db89e749742.jpeg)

> The **Turing Test** assesses a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.

To pass the Turing Test, a computer would need:

- **Natural Language Processing:** To communicate in a human language
- **Knowledge Representation:** To store information
- **Automated Reasoning:** To answer questions and draw conclusions
- **Machine Learning:** To adapt and extrapolate

### Alan Turing

Alan Mathison Turing (1912-1954) was a highly influential English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist. He played a crucial role in breaking German ciphers during World War II.

Turing predicted that by the year 2000, machines would be able to fool 30% of human judges for five minutes. The **Loebner Prize** is an annual competition that evaluates this.

![Loebner Prize Medal with Hugh G. Leachner](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/b8272cbd-f497-47ff-8c57-5862bf332dcd.jpeg)

![Loebner Prize Medal with Alan Turing](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/749cbf56-c50c-48ac-aa86-c8b9f113a315.jpeg)

Success in these competitions often depends on deception and "cheap tricks." For example, the ELIZA program (1966) and Mitsuku chatbots.

A better Turing Test would involve questions that are easily answered by humans but not by computers using such tricks. For instance:

- "The trophy would not fit in the brown suitcase because it was so large. What was so large?"
    
    - The trophy
    - The brown suitcase
- "The large ball crashed right through the table because it was made of steel. What was made of steel?"
    
    - The large ball
    - The table

Advantages of this approach over the standard Turing test:

- Can be machine-administered and graded
- Removes human subjectivity
- Verbal dodges are ineffective
- Questions can be made "Google-proof"

The lecture notes use the metaphor of artificial flight: "The quest for 'artificial flight' succeeded when engineers and inventors stopped imitating birds!" The idea is that the goal isn’t to make “machines that fly so exactly like pigeons that they can fool even other pigeons."

##  AI Definition 3: Thinking Rationally

This involves modeling thinking as a logical process, where conclusions are drawn based on symbolic logic.

- **Logic:** Patterns of argument that yield correct conclusions from correct premises. For example, "Socrates is a man; all men are mortal; therefore Socrates is mortal."

The logicist approach describes problems in formal logical notation and applies general deduction procedures to solve them.

##  AI Definition 4: Acting Rationally

A rational agent acts to optimally achieve its goals.

- Goals are application-dependent and expressed in terms of utility.
- Being rational means maximizing expected utility.

AI focuses on the study and construction of agents that "do the right thing."

## 💡 State of the Art in AI Today

AI is prevalent in various applications:

- **IBM's DeepQA (Jeopardy!):**
    
    - Watch: [https://www.youtube.com/watch?v=lI-M7O_bRNg&t=136s](https://www.youtube.com/watch?v=lI-M7O_bRNg&t=136s)
    - [https://www.youtube.com/watch?v=r7E1TJ1HtM0](https://www.youtube.com/watch?v=r7E1TJ1HtM0)

![Jeopardy! Scene](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/d0f995b4-a7cc-4013-9e96-7898220c64c0.jpeg)

- **Self-driving cars:**
    
    - Google News: [https://www.telegraph.co.uk/technology/2019/02/06/rapid-rolldriverless-cars-uk-roads-should-have-us-worried/](https://www.telegraph.co.uk/technology/2019/02/06/rapid-rolldriverless-cars-uk-roads-should-have-us-worried/)
    - Ethics: [https://www.fastcompany.com/90300056/self-driving-cars-willnever-be-moral-lets-stop-pretending-otherwise-](https://www.fastcompany.com/90300056/self-driving-cars-willnever-be-moral-lets-stop-pretending-otherwise-)
- **Natural Language and Speech Technologies:**
    
    - Google Voice Search
    - Apple Siri

![iPhone conversation with Siri](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/589ecb61-5dd9-41e4-b0c7-f34ff09bda25.jpeg)

- **Machine Translation:**
    
    - translate.google.com

![Comparison of machine and human translation](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/237f53cd-6d4b-4a32-b858-75e868b01b0b.jpeg)

- **Text Suggestions:**

![Email notification with text suggestions](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/484c1c90-8bc0-4b93-8559-13ec2a5357ec.jpeg)

_From Mor Naaman presentation in D3A conference Denmark, 01-02-2024_

- **Vision:**
    
    - Optical Character Recognition (OCR)
    - Handwriting recognition
    - Face detection/recognition (cameras, Facebook)
    - Visual search: Google Goggles, Google Lens, Google Photos

![Google Goggles demonstration](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/294bea01-5566-411e-bfb7-c1e3f2f6f01d.jpeg)

![Vision applications](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/9de43848-b666-4e66-9924-6c12c2a5ac37.jpeg)

```
*   Video, real-time applications
```

![Face Alignment Demonstration](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/37a2635a-a22a-4223-9cad-81e46fabd74d.jpeg)

_From Mor Naaman presentation in D3A conference Denmark, 01-02-2024_

- **Mathematics:**
    
    - In 1996, a computer program proved a mathematical conjecture unsolved for decades.
    - Mathematical software

![Wolfram Mathematica Logo](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/3f37c494-63b2-4d4b-a135-14b83081f956.jpeg)

- **Games:**
    
    - IBM’s Deep Blue defeated Garry Kasparov in 1997.

![Chess match on screen](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/8a008f0d-dfad-4023-bad6-5fb4c5f846d7.jpeg)

```
*   Checkers was "solved" in 2007.
*   Google's AI beat a human grandmaster at Go.
*   Google AI beats top human players at StarCraft II.
```

- **Logistics, Scheduling, Planning:**
    
    - AI logistics planning during the 1991 Gulf War.
    - NASA’s Remote Agent software on Deep Space 1.
    - NASA’s MAPGEN system for Mars Exploration Rovers.
    - Mars rovers

![NASA Mars Exploration Rover](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/92140928-2daf-45cf-80d0-7e567e24249a.jpeg)

```
*   Autonomous vehicles, self-driving cars
```

![Volkswagen SUV with Sensors](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/5d338f52-2e7a-4940-b8e6-90c4c8ac87b8.jpeg)

```
*   Autonomous helicopters
*   Drones
*   Robot soccer (RoboCup)
*   Personal robotics
*   Humanoid robots
*   Robotic pets
```

![White dog with black spots](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/cde36a90-39e8-4953-9b81-6e1b1519060a.jpeg)

```
*   Personal assistants
```

![Robotic arm folding clothes](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/21bf25a3-5c3b-44f3-8710-8d13220b8289.jpeg)

```
*   Cloth Grasp Point Detection: [https://www.youtube.com/watch?v=ve6VyzX6BCc](https://www.youtube.com/watch?v=ve6VyzX6BCc)
```

## 🕰️ Origins of AI: Early Excitement

- **1940s:** First model of a neuron (W. S. McCulloch & W. Pitts), Cybernetics
- **1950s:** Turing Test, Perceptrons (F. Rosenblatt), Computer chess and checkers (C. Shannon, A. Samuel), Machine translation (Georgetown-IBM experiment), Theorem provers (A. Newell and H. Simon, H. Gelernter and N. Rochester)

![Collage of AI pioneers](https://api-turbo.ai/bed18786-5f37-40f5-a860-f4f35cbc72b8/47e50b23-c69a-4461-b755-796f9962580f.jpeg)

- **1956:** Dartmouth meeting: "Artificial Intelligence" adopted

In 1957, Herbert Simon predicted that within 10 years, a computer would be a chess champion and prove an important new mathematical theorem. While his prediction was optimistic, it eventually came true forty years later.

### 📉 Harder Than Originally Thought

- **1966:** Eliza chatbot (Weizenbaum)
- **1954:** Georgetown-IBM experiment
    - Automatic translation of Russian sentences into English
    - Limited to six grammar rules, 250 vocabulary words, organic chemistry
    - Machine translation was promised to be solved in three to five years (press release)
    - Automatic Language Processing Advisory Committee (ALPAC) report (1966): machine translation has failed
    - "The spirit is willing but the flesh is weak." → "The vodka is strong but the meat is rotten."

### ❄️ History of AI: Taste of Failure

- **Late 1960s:** Machine translation deemed a failure, Neural nets deprecated (M. Minsky and S. Papert, 1969)
- **Early 1970s:** Intractability is recognized as a fundamental problem
- **Late 1970s:** The first "AI Winter"

### 📈 History of AI to the Present Day

- **1980s:** Expert systems boom
- **Late 1980s:** Expert system bust; the second "AI winter"
- **Early 1990s:** Neural networks and back-propagation
- **Late 1980s:** Probabilistic reasoning on the ascent
- **1990s-Present:** Machine learning everywhere, Big Data, Deep Learning

## 🚀 Recent Successes in AI

Factors contributing to recent successes include:

- Faster computers
- Dominance of statistical approaches and machine learning
- Big data
- Crowdsourcing