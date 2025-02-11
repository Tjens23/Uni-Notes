---
tags:
  - Notes
links: "[[Web tech Lecture 1 Notes|Web tech Lecture 1 Notes]]"
creation date: 2025-01-06 14:22
modification date: Monday 6th January 2025 14:22:25
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 1 Notes]]

---



# Web History

- The concept of the World Wide Web was proposed by **Tim Berners-Lee** in 1989 at CERN.

---

# HTTP (HyperText Transfer Protocol)

- HTTP is the client-server protocol for loading web pages and resources.
- Operates over **TCP**, using:
  - **Port 80** for HTTP
  - **Port 443** for HTTPS
- Communication follows an asymmetric **request/response pattern**:
  - The client sends a request.
  - The server responds.

### HTTP Request Methods
- **GET**
- **POST**
- **DELETE**
- **PUT**
- **PATCH**

---

# HTTP Response Status Codes

### Categories of Status Codes

1. **1xx: Informational**
   - Indicates the request has been received and is being processed.

2. **2xx: Success**
   - The request has been successfully received, understood, and accepted.
   - Example: `200 OK`

3. **3xx: Redirection**
   - Further action is required by the client to complete the request.
   - Example: `301 Moved Permanently`

4. **4xx: Client Error**
   - The request contains bad syntax or cannot be fulfilled.
   - Example: `404 Not Found`

5. **5xx: Server Error**
   - The server failed to fulfill a valid request.
   - Example: `500 Internal Server Error`

> For visual representation of status codes, visit [HTTP Cats](https://http.cat/).

---

# Structure of HTTP Messages

### Components of HTTP Messages

1. **Start Line**: Contains the request or response line.
2. **Message Headers**: Provide additional information about the request or response.
3. **Blank Line**: Indicates the end of the headers.
4. **Message Body**: Contains the actual content being sent.

---

### Example: Request Message

```http
GET /doc/test.html HTTP/1.1
Host: www.test101.com
Accept: image/gif, image/jpeg, */*
Accept-Language: en-us
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0
Content-Length: 35

BookId=12345&author=Tan+Ah+Teck
```



### Example: Response Message

```
HTTP/1.1 200 OK
Date: Sun, 08 Feb xxxx 01:11:12 GMT
Server: Apache/1.3.29 (Win32)
Last-Modified: Sat, 07 Feb xxxx
ETag: "0-23-4024c3a5"
Accept-Ranges: bytes
Content-Length: 35
Connection: close
Content-Type: text/html`
<h1>My Home page</h1>
```



---

# HTML (HyperText Markup Language)

- HTML is the standard markup language for creating web pages.
- It allows browsers to interpret and display content.

## Basic Structure of an HTML Document

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <script src="index.js"></script>
  </body>
</html>
```

- DOCTYPE htlm: tells the browser what version of HTML the page is written in.
- Viewport:
    - Controls layout and scaling of the webpage.
    - Attributes:
        - `width=device-width`: Sets the width of the viewport to the device's screen width.
        - `initial-scale=1.0`: Sets the initial zoom level.
- X-UA-Compatible Meta Tag:
    - Specifies compatibility settings for browsers.
    - Attributes:
        - `http-equiv="X-UA-Compatible"`: Indicates compatibility mode.
        - `content="ie=edge"`: Forces Internet Explorer to use its latest rendering engine.



## HTML Forms

HTML forms allow users to input data and submit it to a server.

### Basic Structure of a Form
```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  <button type="submit">Submit</button>
</form>
```

### Common Input Types

- Text fields
- Radio buttons
- Checkboxes
- Submit buttons


--- 

# Evolution of HTTP

### Timeline of HTTP Versions

1. **HTTP/0.9 (1991)**:
    
    - **Prototype**: Supported only the `GET` method.
    - Features:
        - No headers, only simple hypertext requests.
        - Connection closed after each response.
2. **HTTP/1.0 (1996)**:
    
    - **Enhancements**: Introduced `HEAD` and `POST` methods.
    - Features:
        - Added headers for more complex interactions.
        - Connection closed after each response.
3. **HTTP/1.1 (1999)**:
    
    - **Improvements**: Persistent connections.
    - Features:
        - Support for all methods (e.g., `PUT`, `DELETE`).
        - Non-hypertext resources (CSS, images).
        - Introduced chunked transfer encoding.
4. **HTTP/2 (2015)**:
    
    - **Goals**: Reduce latency, improve performance.
    - Features:
        - Binary protocol (instead of text-based).
        - Multiplexing: Multiple requests/responses sent over one connection.
        - Header compression to reduce overhead.
5. **HTTP/3 (2021)**:
    
    - **Innovation**: Built on QUIC instead of TCP.
    - Features:
        - Faster, more reliable connections.
        - Mandatory encryption (TLS).
        - Connection ID for seamless transitions between networks.