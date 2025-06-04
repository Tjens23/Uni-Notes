---
creation date: 2024-12-28 17:00
modification date: Saturday 28th December 2024 17:00:18
tags:
  - Assignments
year: 2024
semester: Break before Semester 4
links: "[[OD Lecture 10]]"
---

---
# [[OD Lecture 10 Assignment]]


# Take-home assignment
- Application to insert and show names in a database
- html files are provided. The rest of the solution are up to you
- A three container application setup, with a database, backend and proxy
- A database-centered application, operating behind a reverse proxy
- Only the proxy is exposed to the world, meaning there are no immediate need for encrypted communication behind the proxy 
- Multiple docker networks should be used, to ensure isolation of containers with confidential data 
- Remember: Name services exactly as proposed in the assignment



##  Requirements: Proxy

- Must implement a nginx server
- Enable https communication between the user and the proxy through port 443
- Serve the provided html files 
- Proxy POST /person/ and GET /persons/ to backend
- Self-signed certificate and root CA certificate should be saved in /etc/nginx/sslas respectively site.crt and rootCA.pem


## Requirements: Backend

- Expose its services through port 5000 
- Must serve the two endpoints 
	- POST /person/
	- GET /persons/
- The endpoints is used take input data from a html form and inserting it into the database
- The backend can be implemented in whatever language


## Requirements: Database

- Must implement a mysql server
- Should contain one table,Person, with the following parameyers
	- Automatically incrementing integer PersonID
	- Text field Firstname 
	- Text field, lastname


## Test your solution
If your solution passes the following tests, it is good to go

**Run Newman Tests**

```shell
docker compose exec -T newman newman run --env-var url=proxy od-2023-test.json
```


**Verify SSL Certificate**


```shell
docker compose exec -T proxy openssl verify -CAfile /etc/nginx/ssl/rootCA.pem /etc/nginx/ssl/site.crt
```


**Check Database Exposure**

```shell
wget --no-check-certificate --timeout 1 -qO /dev/null http://localhost:3306 || echo "Database not exposed"

```


**Check Backend Exposure**

```shell
wget --no-check-certificate --timeout 1 -qO /dev/null http://localhost:5000/ || echo "Backend not exposed"
```
