---
creation date: 2024-11-09 14:57
modification date: Saturday 9th November 2024 14:57:40
tags:
  - Assignments
year: 2024
semester: 3
links: "[[OD Lecture 1]]"
---

---
# OD Lecture 1 Assignments


---

## Assignment 1: Hello world!

- Create a container that runs the above-mentioned hello-world image

```
docker run -rm hello-world
```

## Assignment 3: Home cooked image

```
FROM ubuntu
RUN echo "Some text" > helloWorld
CMD cat helloWorld
```

build image

```
docker build -t tjens23/hello-world .
```


run image: 


```
docker run -rm tjens23/hello-world
```


## Assignment 4: Building Dockerfiles

- Build the included Dockerfile. Remember to give the build a tag
- Run the above-built image. Remember to run it in a way that makes it possible to enter the container
- Install python 3 and run the included print.py file


```
FROM ubuntu
COPY L1E3/ /home/
CMD bash
```

```
docker build -t tjens23/assgin04 .
```


```
docker run -it  tjen23/assign04 
```

