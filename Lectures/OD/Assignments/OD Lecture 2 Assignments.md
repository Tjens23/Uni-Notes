---
creation date: 2024-11-09 16:03
modification date: Saturday 9th November 2024 16:03:46
tags:
  - Assignments
year: 2024
semester: 3
links: "[[OD Lecture 2]]"
---

---
# [[OD Lecture 2 Assignments]]

## Task 1

```
docker run -d -p 7000:80 cocodolan/php:apache
```

- -d for detach, so you get you're terminal back
- -p for port... I'm mapping porrt 7000 to the container port 80


visit `localhost:7000` or use curl command:

```
curl http://localhost:7000
```


## Task 2

```
FROM php:apache
WORKDIR app/
COPY L2E2/* /app/
RUN docker-php-ext-install mysqli
EXPOSE 80
CMD ["apache2-foreground"]
```


```
docker buildx build -t tjens23/odl2e2 Dockerfile .
```

```
docker run -d -p 80:80 tjens23/odl2e2
```


## Task 3

```
docker run -it ubuntu bash
```


```sql
show databases;
```

```sql
create database odl2e3;
```


```sql
CREATE TABLE IF NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL
);
```


```sql
insert into user(name, surname) values('Tobias', 'Jensen');
```


```sql
select * from user;
```

```sql
truncate table user;
```

```
drop table user
```

```sql
drop database odl2e3;
```


## Task 4


```dockerfile
FROM mysql:latest
ENV MYSQL_ALLOW_EMPTY_PASSWORD="yes"
COPY L2E4/init.sql /docker-entrypoint-initdb.d/
```


```
docker buildx build -tjens23/odl2e4 Dockerfile .
```

```
docker run -d --name=ODL2E4 odl2e4
```


```
docker exec -it ODL2E4 bash
```


```
mysql -u root
```

```
show databases;
```


## Task 5

```yaml
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
