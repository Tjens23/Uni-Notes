---
creation date: 2024-12-20 16:36
modification date: Friday 20th December 2024 16:36:33
tags:
  - Assignments
year: 2024
semester: Break before Semester 4
links: "[[OD Lecture 7]]"
---

---
# [[OD Lecture 7 Assignments]]

## Task 1


```python
import time

StartTime = time.time();

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
fibonacci(35)
EndTime = time.time();
print(f"Time taken: {EndTime - StartTime} seconds")
```



## Task 2

```Dockerfile
FROM python:latest
WORKDIR /app/
COPY Main.py /app/
CMD ["python", "/app/Main.py"]
```


```
docker buildx build -t <tag> -f Dockerfile .
```

```sh
 docker run -it --cpus=<value> <tag>
```

