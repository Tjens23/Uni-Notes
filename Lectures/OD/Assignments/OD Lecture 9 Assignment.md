---
creation date: 2024-12-28 14:43
modification date: Saturday 28th December 2024 14:43:48
tags:
  - Assignments
year: 2024
semester: Break before Semester 4
links: "[[OD Lecture 9]]"
---

---
# [[OD Lecture 9 Assignment]]


# OD OLD EXAM


## Describe the three file system abstractions

- Physical file system
- Virtual file system
- Logical file system 


### Answer
- Physical file system: A physical file sysmte is something that's used by your operating system to manage and organize  data stored on physical devices such as SSD or HDD
- Virtual File system: The Virtual File System is the software layer in the kernel that provides the filesystem interface to userspace programs.
- Logical File system: The logical file system is the level of the file system at which users can request file operations by system call.


## Which of the following  are the purposes of a scheduler?

### Answer

- To select the next process to run
- To context-switch between process
- To ensure optimal use of resources



## Scaling by increasing the nuimber of machines is called?

### Answer:

- Horizontal scaling


## Which of the following are layer 4 protocols?


- TCP
- UDP
- IP
- ARP
### Answer
- TCP
- UDP

## Which is the Slowest:

- Sequential Writes
- Random writes
- Combination of sequential and random writes
- All same speed


### Answer

- Random writes


## What is Processor Affinity? 

- Method to support asymmetic multi-processing
- Mathod to ensure coherency of RAM
- Method to pin a process to a specific CPU
- Method to improve scheduling in FIFOs

### Answerr

- Method to pin a process to a specific CPU



## What is a reverse proxy:


- A server places after the clients,  used to sort thougfh client-generated traffic
- A server placed in front of servers, usedf to forward client request  to the servers
- A server placed between servers and databases to obfuscate requests
- a server placed in front of  servers, used as a firewalll


### Answer:
- A server placed in front of servers, used to forward client request  to the servers


## What is a type 2  hypervisor

- A layer enabling hyperthreading
- A layer between os and application
- a layer between hardware and os
- a layer between a host and guest os


### Answer:
- a layer between a host and guest os


### What is a multi-core system
- A system with multiple cores in a single processor
- A system with multiple processors
- A system with a single core
- A system with a single processor


### Answer
- A system with multiple cores in a single processor


## ICP can be used with

- Asynchronous message parsing
- Synchronous message parsing
- Shared memory
- Resource discovery


### Answer
- Asynchronous message parsing
- Synchronous message parsing
- Shared memory


## What is a partition 
- A division of a disk
- A sector
- A block
- Dual boot


### Answer
- A division of a disk


## How is a docker image configured?

- Dockerfile
- in a Docker Container
- on Docker hub
- in C++


### Answer
- In a Dockerfile


## Page tables maps between
- physical memory
- physical file system
- virtual memory
- virtual file system 


### Answer:
- physical memory
- virtual memory


## What is hyperthreading
- A technology allowing for more than one thread on each core
- A technology doubling the number of cores
- A technollogy doubling the number of processors
- A technology making the processor run more than one process at a time


### Answer
-  A technology allowing for more than one thread on each core


## What is type 1 hypervisor?

- A layer enabling hyperthreading
- a layer between os and application
- a layer between hardware and os
- a layer between a host and guest os


### Answer:

- a layer between hardware and os


## What is an I/O bound process
- Programs that are very cpy-heavy
- programs that are  often waiting for I/O input
- programs that minimise the use of CPU
- programs that try to minimise the wait on I/O


### Answer:
- programs that are  often waiting for I/O input



## What is Race condition?


- A condition where the behaviour of a process depends on timing and concurrent theads and processes 
- A condition where processes are blocked because each process is holding resources whilst waiting on other reousces acquired by   another proces
- A condition where the cpu finishes its processing prematurely 
- a locking mechanism where resources can be locked for induvidual use

### Answer:

- A condition where the behaviour of a process depends on timing and concurrent theads and processes 



## NGINX can be used as a
- webserver
- reverse proxy
- database  server
- load balancer

### Answer

webserver
- web server
- reverse proxy
- load balancer


## How many bits in IPv4 address
- 16
- 32
- 64
- 128

### Answer
- 32


## Which protocoll is used to connect ip addresses to MAC addresses?


- ARP
- TCP
- UDP
- IP

### Answer

- ARP


## What is docker?

- Virtulisation at the hardware level
- virtulisation  at the operating system level
- virtulisation of virtual machines
- virtulisatoin of shells

### Answer
- virtulisation  at the operating system level


## How many keys are involed in asymmetric encryption 
- 1
- 2
- 3
- 4


### Answer
- 2

## Which as the largest overhead?
- TCP
- UDP
- ARP
- Their overheads are identical


### Answer
- TCP


## What is a  sector in storage
- smallest physical unit
- Smallest logical unit
- Smallest virtual unit
- Smalllest memory unit 


### Answer
- smallest physical unit


## What is a network protocol
- A set of  rules and guidelines for describing network packets
- A set of rules and  guidelines for describing communication 
- a set of guidelines to folow wwhen something goes incorrectly
- A set of guidelines to describe OS performace


### Answer
-  A set of rules and  guidelines for describing communication 



## What  layer in the IP/TCP model to the TCP protocol belong on?
- 2
- 3
- 4
- 5


### Answer

- 4



## Why do we need a firewall
- To protect data
- to protect identity
- to protect  resources
- to protect againts physical intruders



### Answer
- To protect data
- to protect identity
- to protect  resources



## What is fragmentation 
- When blocks are larger than sectors
- when a sector is broken 
- when the order of  data is inverted
- when data is scattered



### Answer
- when data is scattered


## Which of the following are not abstractions of memory

- Vertical Memory
- Virtual memory
- Physical memory
- Logical Memory
### answer
- Vertical Memory
- Logical Memory


## What is a frame
- a chunck of physical memory
- a chunck of virtual memory
- a cpu cache holding memory references
- information about memory structure


### Answer
- a chunck of physical memory


## Which of the following are not scheduling algorithms

- Priority
- Fastest First
- Least I/O first
- shortest job first

## Answer
- Fastest First
- Least I/O first


## What is RAID

- Testing of  Random Access pseeds of a disk
- A way to  copy disk
- Virtulisation of storage in a redundant manner
- when orcs attack  at night

### Answer
- Virtulisation of storage in a redundant manner




## Multitaksing is __ based
- process
- thread
- job
- task


### answer
- process



## What is the first line in an HTTP GET request
- HTTP/1.1 200 OK 
- GET / HTTP/1.1
- GET / HTML/1.1
- HTML/1.1 200 OK


### answer
- GET / HTTP/1.1


## Which of the following are not instructions used in Dockerfiles

- RUN
- MOVE
- FROM
- EXEC


### Answer
- MOVE
- EXEC

## Reverse proxying in NGINX can be done using
- Proxy_prass
- Request_pass
- HTTP_pass
- Reverse_proxy_Pass


### Answer

-  Proxy_prass


## Which of the following are not vaild docker commands
- docker compose up / docker-compose up 
- docker run nginx
- docker build .
- docker export nginx



### Answer
- docker export nginx


## Construct a docker command that creates and starets a container from the image "mysql" and maps port 3000 on the host port 31000 in container

- docker run -d -p 3000:31000 -e MYSQL_ROOT_PASSWORD=Hyg57aff -e MYSQL_ALLOW_EMPTY_PASSWORD=false -e MYSQLL_RANDOM_PASSWORD=false mysql


### Expected keywords

- docker
- run
- -p 3000:31000
- mysql



## What is the second message sent in SSL/TLS

- Client Hello
- Server Hello
- Key Share
- HTTP GET Request


### Answer 
- Server Hello



## Wjhat is deadlock
- A condition where the behaviour of the porcess depe3nds on timing and concurrect threads and processes
- A condition where process are blocked becase each process is holding resources whilst waiting on other resources acquired by another process
- A condition where the cpu finishes it's processing prematurely 
- a locking mechanism where resources can be locked for individual use 
### Answer:

- A condition where process are blocked becase each process is holding resources whilst waiting on other resources acquired by another process


