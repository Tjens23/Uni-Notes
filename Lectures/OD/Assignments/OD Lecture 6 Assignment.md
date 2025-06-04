---
creation date: 2024-11-09 15:45
modification date: Saturday 9th November 2024 15:45:02
tags:
  - Assignments
year: 2024
semester: 3
links: "[[OD Lecture 6]]"
---

---
# OD Lecture 6 Assignment

---

# Task 2

```sh
kubectl get nodes
kubectl get namespace
kubectl get deploy
kubectl get svc
kubectl get pods
```

### 2: In which namespaces are there currently resources present?


 all but the default namespace


## Task 3



```yml
version: '3.8'
services:
  web:
    build: 
      context: .
      dockerfile: DockerfileL2E2
    container_name: web_container
    ports:
      - "5000:80"
    depends_on:
      - db
    volumes:
      - ./L2E2:/var/www/html
  db:
    build:
      context: .
      dockerfile: DockerfileL2E4
    container_name: db_container
```




```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: merged-container
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ODL6E3
  template:
    metadata:
      labels:
        app: ODL6E3
    spec:
      containers:
      - name: odl2-web
        image: tjens23/odl2e2
        ports:
        - containerPort: 80
        volumeMounts:
        - name: web-files
          mountPath: /var/www/html
      - name: odl2-sql
        image: tjens23/odl2e4
        env:
        - name: MYSQL_ALLOW_EMPTY_PASSWORD
          value: "yes"
        - name: MYSQL_DATABASE
          value: "abook"
        ports:
        - containerPort: 3306
      volumes:
      - name: web-files
        hostPath:
          path: ./L2E2
          type: Directory
```


```yaml
apiVersion: v1
kind: Service
metadata:
  name: merged-service
spec:
  selector:
    app: ODL6E3
  ports:
    - name: web
      port: 5000
      targetPort: 80
    - name: mysql
      port: 3306
      targetPort: 3306
  type: LoadBalancer
```



