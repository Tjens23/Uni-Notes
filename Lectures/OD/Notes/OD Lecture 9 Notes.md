---
tags:
  - Notes
links: 
creation date: 2024-12-28 14:13
modification date: Saturday 28th December 2024 14:13:54
semester: Break before Semester 4
year: 2024
---


---
# [[OD Lecture 9 Notes]]

---



# Web servers

## Overview 

- A web server comprises the software and hardware that processes HTTP (and HTTPS) requests from user agents, such as web browsers or crawlers.
- The server responds to requests with resources or error messages, supporting both static (pre-existing files) and dynamic (generated at request time) content.
- The hardware configuration of web servers can range from low-end devices, like embedded systems, to high-traffic setups using many powerful servers.
- Technologies like REST, SOAP, and WebDAV have expanded web server functionalities beyond simply serving web pages, making it possible for computer-to-computer communication.


## Historical Development of Web Servers  

- Sir Tim Berners-Lee proposed the WWW project at CERN in March 1989, aiming to facilitate information exchange among scientists using hypertext.
- The first web server outside Europe was set up at SLAC, USA, in December 1991, marking the beginning of transcontinental web communication.
- By 1994, the NCSA httpd server was released, which supported dynamic content through CGI, setting the stage for further advancements in web server technology.
- The Apache HTTP server was initiated in 1995 from patches applied to NCSA code, leading to widespread adoption due to its features and open-source nature.


## Growth and Competition (1996-2014)  

- By the end of 1996, over fifty different web server programs existed due to the growth of the Internet and increasing demand for hosting services.
- Apache HTTP Server emerged as the leading server, boasting reliability and extensive features, while competitors like Netscape Enterprise Server entered the market.
- Protocol developments like HTTP/1.0 and HTTP/1.1 caused many web servers to adapt their implementations to enhance performance, embracing TCP/IP persistent connections.
- The competition intensified as new open-source servers like Nginx and commercial options like LiteSpeed began to offer superior performance, especially for static content.

## New Challenges (2015-Present)  

- The introduction of HTTP/2 posed challenges for less popular web servers, many of which struggled to support the new protocol due to extensive required changes.
- Popular servers quickly integrated HTTP/2, leveraging previous SPDY implementations, to meet growing webmaster demands for improved performance and reduced TCP/IP connections.
- The emergence of HTTP/3 is expected to follow similar dynamics to HTTP/2, influencing server implementation strategies to enhance performance amid increasing web traffic.

## Web Server Functionality and Features  

- Web servers perform URL normalization to standardize and verify URLs in HTTP requests, ensuring consistent request handling.
- URL mapping processes determine which resources correspond to received URLs, enabling servers to return HTML documents, images, or dynamic content based on requests.
- Dynamic content generation involves interacting with internal modules or external programs, enabling varied responses based on user input or configurations.
- Web servers are designed to manage static content serving efficiently, typically avoiding changes to the file contents and relying on HTTP methods for interactions.

## Content Management and Responses  

- Web servers can handle multiple response types based on request characteristics, including successful responses, error messages, and URL redirections.
- URL redirection is used to guide clients to valid resources and can occur due to changes in resource locations or the need for secure connections.
- Caching strategies are implemented by many web servers to improve response times and resource utilization, storing frequently accessed static content for quicker delivery.
- Error handling is crucial, as servers provide feedback on malformed requests, unauthorized access, or unavailability of resources.