---
tags:
  - Notes
links: "[[OD Lecture 1]]"
creation date: 2024-11-09 14:56
modification date: Saturday 9th November 2024 14:56:37
semester: 3
year: 2024
---


---
# OD Lecture 1 Notes

---

## Docker and Containerization

- Docker is defined as a container runtime responsible for managing the lifecycle of containers.
- A Dockerfile creates a Docker Image, consisting of a read-only template built layer by layer.
- Example Dockerfile commands show the process of initializing an image and specifying configuration options.
- Docker containers are isolated, run instances created from images, and can be run via the Docker CLI commands.


##  Container Registry and Architecture

- The Docker Registry functions similarly to GitHub but for Docker Images, with Docker Hub being the default public registry.
- The architecture of Docker Compose allows for the configuration of multi-container applications, clarifying methods for exposing ports and managing services.


```mermaid
flowchart TB

    subgraph Host

        Docker_Daemon["Docker Daemon"]

        subgraph Containers

            Container_1["Container 1<br>App: Nginx"]

            Container_2["Container 2<br>: MySQL"]

            Container_3["Container 3<br>: Redis"]

            Container_4["Container 4<br>: Node.js"]

        end

    end

  

    Client["Docker Client <br>docker run <br> docker build <br> docker pull"]

    Client --> Docker_Daemon

    Docker_Daemon --> Container_1

    Docker_Daemon --> Container_2

    Docker_Daemon --> Container_3

    Docker_Daemon --> Container_4

  

    Container_1 -.-> Container_2

    Container_1 -.-> Container_3

    Container_4 -.-> Container_2

    Container_4 -.-> Container_3
```


# Containers in Production

- Deployment considerations in a production environment highlight isolation, portability, maintainability, and deplorability advantages.
- Strategies for addressing application or host failures within single and multi-machine setups are discussed, emphasizing resource management and recovery needs.
- Key challenges include ensuring scalability, availability, reliability, recoverability, and robustness in deploying containers.


# Container Orchestration

- Container orchestration systems manage configurations, coordination, and the lifecycle of containers across clusters.
- The orchestrator plays a critical role in operating within a container runtime infrastructure, ensuring efficient resource utilization and application performance.
- Emphasis is placed on the ability to efficiently manage multiple containers to maintain service levels despite varying workloads.


# Infrastructure and Virtualization

- Examples demonstrate various server infrastructures under different conditions (Type 1 and Type 2 Hypervisors) and the implementation of virtual machines.
	- A hypervisor is a software layer that enables the creation and management of virtual machines (VMs) on a physical host machine. It acts as an intermediary between the hardware and the operating systems running on the VMs, allowing multiple operating systems to run concurrently on a single physical machine.
	- **Type 1 Hypervisor (Bare-metal)**: This type runs directly on the host's hardware without an underlying operating system. It is typically more efficient and offers better performance as it has direct access to the hardware resources. Examples include VMware ESXi and Microsoft Hyper-V.
	- **Type 2 Hypervisor (Hosted)**: This type runs on top of a conventional operating system. It relies on the host OS for resource management and may have slightly lower performance compared to Type 1 hypervisors. Examples include VMware Workstation and Oracle VirtualBox.
- Advantages of virtualization include host protection and suspension capabilities of running VMs, while disadvantages encompass resource sharing and startup speeds.
## Virtual machine architecture 

![[Pasted image 20241006135754.png]]

## What's a Hypervisor

A hypervisor is a form of virtualization software used in Cloud hosting to divide and allocate the resources on various pieces of hardware. The program which provides partitioning, isolation, or abstraction is called a virtualization hypervisor. The hypervisor is a hardware virtualization technique that allows multiple guest operating systems (OS) to run on a single host system at the same time.

### TYPE-1 Hypervisor:

The hypervisor runs directly on the underlying host system. It is also known as a “Native Hypervisor” or “Bare metal hypervisor”. It does not require any base server operating system. It has direct access to hardware resources. Examples of Type 1 hypervisors include VMware ESXi, Citrix XenServer, and Microsoft Hyper-V hypervisor.


### TYPE-2 Hypervisor:

A Host operating system runs on the underlying host system. It is also known as ‘Hosted Hypervisor”. Such kind of hypervisors doesn’t run directly over the underlying hardware rather they run as an application in a Host system(physical machine). Basically, the software is installed on an operating system. Hypervisor asks the operating system to make hardware calls. An example of a Type 2 hypervisor includes VMware Player or Parallels Desktop. Hosted hypervisors are often found on endpoints like PCs.  The type-2 hypervisor is very useful for engineers, and security analysts (for checking malware, or malicious source code and newly developed applications).