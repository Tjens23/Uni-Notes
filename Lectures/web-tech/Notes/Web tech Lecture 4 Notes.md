---
tags:
  - Notes
links: 
creation date: 2025-01-06 15:21
modification date: Monday 6th January 2025 15:21:08
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 4 Notes]]

---



# Web Technologies Overview

- The simplest structure of web technologies involves a client-server architecture where clients send requests to the server, which responds accordingly.
- Server-side development includes Common Gateway Interface (CGI) as a method for executing programs in response to client requests, though it is less common today due to modern alternatives.
- Modern web servers support multiple programming languages, APIs, and frameworks, allowing developers to choose the appropriate tools based on the project scale: small personal home pages, small to medium projects using robust frameworks, or large projects requiring multiple servers with load balancing.


## Server-side Development Considerations  

- When selecting a tool for server-side development, factors such as project size and requirements must be considered.
- For small applications, a small server API suffices while medium projects are better handled with frameworks that support desired software design. For larger projects, a load balanced architecture with multiple servers is recommended.
- Laravel, a Model-View-Controller web framework for PHP, is commonly used for web development due to its structured approach to application development.


## Laravel Framework  

- Laravel is influenced by the book "Laravel Up & Running: A Framework for Building Modern PHP Apps," although developers are advised to consult the official documentation for the most current information.
- The framework operates on the principle that it is a software architecture requiring developers to fill in code where necessary, and it differentiates between API calls and framework functionalities.
- Key components of a Laravel application include the configuration files, public resources (JS and CSS), and Blade files, which are HTML templates that allow PHP integration for dynamic content.

## PHP Language Features  

- PHP, which stands for Hypertext Preprocessor, began as CGI tools for web applications before transitioning into a fully-fledged programming language.
- PHP allows for both server-side scripting and command-line execution, and it is dynamically typed with primitives including numbers, strings, and booleans, which can be declared using the dollar sign ($).
- Variables can be created in PHP and are capable of handling both string interpolation and concatenation, where double-quoted strings can parse variables within them, unlike single-quoted strings.


## PHP Functions and Types  

- PHP supports function overloading where the same function can behave differently based on the types of arguments passed, as shown in the examples of the `sum` function illustrating type coercion.
- By enabling strict types with `declare(strict_types=1);`, PHP can enforce type checking at runtime. If a type mismatch occurs, it will throw a TypeError, enhancing code reliability.
- Functions in PHP can return different types such as integers and can also handle various forms of input through parameter type hints, promoting better code practices.



## Object-Oriented Programming in PHP  

- PHP supports object-oriented programming (OOP) principles like classes, inheritance, and access modifiers. An example class `User` demonstrates using properties and methods along with access modifiers.
- The constructor and destructor methods in PHP classes enable initialization and cleanup of resources when objects are instantiated or destructed.
- Inheritance is implemented using the `extends` keyword, while the `final` keyword restricts further inheritance of classes. PHP also allows for abstract classes and interfaces which define contracts for implementation by derived classes.


## PHP Namespaces and File Inclusion  

- Namespaces are used to encapsulate classes, allowing for better organization and avoidance of name conflicts in larger projects.
- PHP supports file inclusion mechanisms with different behaviors: `require` and `require_once` will cause fatal errors if the file cannot be included, whereas `include` and `include_once` will emit warnings.
- The use of namespaces can simplify code maintenance and enhance clarity, particularly in large applications.


## Examples


### Displaying Users

```PHP
<div>
    <p>Hello, User A</p>
    <p>Hello, User B</p>
</div>
<div>
    @foreach ($users as $user)
        <p>Hello, {{ $user->name }}</p>
    @endforeach
</div>
```

### Accessing Assets

To include CSS and JavaScript files located in the

```
public
```

folder, you can use the

```PHP
asset()
```

function:

```PHP

<!-- In a Blade file -->
<link rel="stylesheet" href="{{ asset('css/style.css') }}">
<script src="{{ asset('scripts/event.js') }}"></script>
```


### PHP Variables and Types
In PHP, variables are declared with the `$` symbol. Here’s an example of declaring variables and using different types:


```PHP
<?php
$num = 42; // Integer
$str = "Hello, World"; // String
$bool = true; // Boolean
$nullVar = null; // Null
?>
```

### ### PHP Functions

Here’s an example of a simple function in PHP that demonstrates type hinting and strict types:

```PHP
declare(strict_types=1);

function sum(int $a, int $b): int {
    return $a + $b;
}

echo sum(5, 10); // Outputs: 15
```

### Object-Oriented Programming in PHP

```PHP
class User {
    public $name;
    public $email;

    public function __construct($name, $email) {
        $this->name = $name;
        $this->email = $email;
    }

    public function printUser() {
        echo "$this->name: $this->email";
    }
}

$user = new User("John Doe", "john@example.com");
$user->printUser(); // Outputs: John Doe: john@example.com
```


### Namespaces in PHP

Namespaces help organize code and avoid name conflicts. Here’s how to define and use namespaces:

```PHP
// File: app/Model/User.php
namespace App\Model;

class User {
    public function greet() {
        return "Hello from User!";
    }
}

// File: another_file.php
require 'app/Model/User.php';

use App\Model\User;

$user = new User();
echo $user->greet(); // Outputs: Hello from User!
```
