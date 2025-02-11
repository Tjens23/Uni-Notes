---
tags:
  - Notes
links: "[[Web tech Lecture 10]]"
creation date: 2025-01-07 16:01
modification date: Tuesday 7th January 2025 16:01:58
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 10 notes]]

---



# Overview  

- Security is a cross-functional concern in software engineering that affects multiple features and concerns within applications.
- Computer Security focuses on protecting systems and networks from unauthorized access, damage, and disruption of services.
- A single class or course cannot comprehensively cover all aspects of security; the focus will mainly be on common web security issues and attacks.


## Encryption Basics  

- Encryption involves converting plaintext into ciphertext, making it unreadable without a decryption key.
- The process of decryption reverses this by turning ciphertext back into plaintext.
- Ciphers consist of algorithms for encryption and decryption, which are controlled by cryptographic keys.
- The Caesar Cipher is an example of a simple encryption method that can be easily broken with brute force.
- Asymmetric cryptography uses different keys for encryption (public) and decryption (private), while symmetric cryptography employs the same key for both processes.

## HTTPS  

- HTTPS (HTTP Secure) is an encrypted version of HTTP, usually using TLS (Transport Layer Security) for secure communication.
- HTTPS runs on port 443 by default, compared to HTTP’s port 80, and ensures privacy, integrity, and identification.
- The TLS handshake starts with a negotiation using a public/private key pair, leading to session encryption using a symmetric key.
- The use of HTTP Strict Transport Security (HSTS) forces browsers to communicate only over HTTPS, protecting against man-in-the-middle attacks.


## Certificate Authorities  

- Certificate Authorities (CAs) issue digital certificates that validate the ownership of public keys and improve trust in secure communications.
- Three main types of TLS certificates exist: Domain Validated (DV), Organization Validation (OV), and Extended Validation (EV) certificates, differing in their levels of verification.
- Self-signed certificates can be used in development but do not establish the same level of trust as CA-signed certificates.


## OWASP Top 10 Web Application Security Risks

### **Broken Access Control**
    
    - Users can act outside their intended permissions.
    - Example: Non-admin users accessing admin pages.
```PHP
// Risky code allowing unauthorized access
$userId = request("user_id");
$user = User::find($userId); // Any user can access any other user's data
```

**Mitigation**: Always check if the user has permission to access the requested resource.
### Cryptographic Failures
    
- Weak encryption practices or lack of encryption.
- Example: Storing passwords in plain text.

```php
// Storing passwords in plain text (vulnerable)
$password = request("password");
DB::table('users')->insert(['password' => $password]); // Bad practice
```

**Mitigation**: Always hash passwords before storing them.
```php
$hashedPassword = password_hash($password, PASSWORD_DEFAULT);
DB::table('users')->insert(['password' => $hashedPassword]);
```

### Injection
    
- Attackers can inject malicious code into applications.
- Types include SQL Injection and Cross-Site Scripting (XSS).

```php
// Vulnerable SQL query
$id = request("id");
$query = "SELECT * FROM users WHERE id = $id"; // Bad practice
```

**Mitigation**: Use prepared statements.
```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $id]);
```

### **Insecure Design**
    
- **Description**: Flaws in the design of the application can lead to security vulnerabilities.
- **Example**: Not implementing proper authentication mechanisms can lead to unauthorized access.
- **Mitigation**: Always design with security in mind, ensuring proper authentication and authorization checks.
### **Security Misconfiguration**
    
- **Description**: Insecure default configurations or incomplete setups can expose applications.
- **Example**: Leaving debug mode enabled in production.

```php
// In production, debug should be false
define('DEBUG', true); // Bad practice
```

- **Mitigation**: Ensure proper configuration settings for production environments.
###  Vulnerable and Outdated Components

- **Description**: Using outdated libraries or components can introduce vulnerabilities.

- **Example**: Using an outdated version of a library with known vulnerabilities.

- **Mitigation**: Regularly update libraries and dependencies.
### Identification and Authentication Failures
    
- **Description**: Weak authentication methods can lead to unauthorized access.

- **Example**:

```php
// Simple password check (vulnerable)
if ($_POST['password'] == 'password123') {
    // Access granted
}
```

- **Mitigation**: Implement strong password policies and use multi-factor authentication.
### Software and Data Integrity Failures
    
- **Description**: Lack of integrity checks can lead to unauthorized changes.
- **Example**: Not validating file uploads can allow malicious files.
- **Mitigation**: Validate and sanitize all inputs and file uploads.
### Security Logging and Monitoring Failures
    
- **Description**: Insufficient logging can hinder the detection of security breaches.
- **Example**: Not logging failed login attempts.
- **Mitigation**: Implement comprehensive logging for all security-related events.
### Server-Side Request Forgery (SSRF)
    
- **Description**: Attackers can manipulate server requests to access internal resources.

- **Example**:

```php
// Vulnerable SSRF code
$url = request("url");
$response = file_get_contents($url); // Bad practice
```

- **Mitigation**: Validate and restrict URLs that can be accessed.

```php
$allowedDomains = ['example.com'];
if (in_array(parse_url($url, PHP_URL_HOST), $allowedDomains)) {
    $response = file_get_contents($url);
}
```

## Laravel Security Best Practices  

- In Laravel, the APP_KEY is pivotal for encrypting sensitive data and securing sessions. Changes to APP_KEY can affect stored passwords and data encryption.
- Developers must ensure secrets, like APP_KEY, are kept private and not included in version control systems.
- Utilizing good security practices, such as having minimal user permissions and implementing hash and salt for passwords, contributes to overall security.
- A "defense in depth" approach helps to create layers of security, slowing attackers to allow for early responses to potential breaches.