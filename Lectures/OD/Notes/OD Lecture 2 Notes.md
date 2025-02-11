---
tags:
  - Notes
links: "[[OD Lecture 2]]"
creation date: 2024-11-09 16:04
modification date: Saturday 9th November 2024 16:04:09
semester: 3
year: 2024
---


---
# [[OD Lecture 2 Notes]]

---



## Operating Systems Definition and Goals

An OS is a progream that acts as an intermediary between users and the computer hardware, facillitating the execution of the user programs and providing a interface for users to interact with the system.

### Definition of an operating system

- The kernel: The core component of the OS that is always running and responsible for managin hardware resources.
- System utils: Additional programs and tools necessary for the operation and management of the OS.
- **Drivers and Firmware**: Software that allows the OS to communicate with hardware devices.

### Goals of an Operating System

1. **Execution of User Programs**: The OS is designed to execute user applications efficiently, ensuring that they run smoothly and effectively on the hardware.  
  
2. **Convenience of Use**: An OS aims to make the computer system easy and convenient for users to operate, providing a user-friendly interface and responsive interactions.  
  
3. **Efficient Resource Utilization**: The OS optimizes the use of computer hardware resources, including CPU, memory, and storage, to ensure that the system operates efficiently and performs tasks in a timely manner.  
  
4. **Management of System Resources**: The OS acts as a resource allocator, managing hardware resources and providing a uniform interface for applications to interact with these resources.

## Unix and Linux Architecture

Unix and Linux architectures share a  structure that includes four main components: hardware, kernel, shell, and utilities.  
  
##### Unix Architecture

1. **Hardware**: The physical components of the computer system.  
2. **Kernel**: The core part of the operating system that manages hardware resources and facilitates communication between hardware and software.  
3. **Shell**: An interface that allows users to interact with the kernel through commands. It interprets user commands and executes them.  
4. **Utilities**: A collection of programs that perform specific tasks, enhancing the functionality of the operating system.  
  
**Unix Philosophy**: Unix promotes a design philosophy that emphasizes simplicity and modularity. Each program is designed to do one thing well, allowing for efficient composition of commands. The output of one program can be easily used as the input for another, fostering a powerful and flexible command-line environment.  
  

##### Linux Architecture

1. **Hardware**: Similar to Unix, it includes the physical components of the system.  
2. **Kernel**: The Linux kernel, which is open-source, manages system resources and acts as a bridge between applications and the hardware.  
3. **Shell**: Like Unix, Linux provides various shell options (e.g., Bash, Zsh) for user interaction.  
4. **Utilities**: Linux distributions come with a wide array of GNU tools and libraries, additional software, documentation, and often a graphical user interface (GUI) that includes a window system and desktop environment.  
  
**Linux Distributions**: These are packaged versions of Linux that include the Linux kernel, GNU tools, libraries, and additional software tailored for specific user needs or preferences. Each distribution can vary significantly in terms of included software and user interface, but they all adhere to the core principles of the Linux architecture.



## Scheduling in Operating Systems

- Scheduling algorithms determine how CPU time is allocated to processes in the ready queue and are crucial for system performance.
- Various algorithms are employed, including:
- Evaluation of scheduling focuses on maximizing CPU utilization and minimizing turnaround time, waiting time, and response time.


## Job Control and Command Line Interface

- Linux command-line utility facilitates job control, allowing users to manage processes effectively using commands like `sleep`, `kill`, and `ps`.
- Example commands include running a task in the background with `&`, terminating a process with `kill <PID>`, and bringing a background job to the foreground using `fg`.
- These features empower users to orchestrate and monitor processes efficiently in a multi-tasking environment.