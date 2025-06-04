---
tags:
  - Notes
links: "[[Web tech Lecture 3]]"
creation date: 2025-01-06 15:11
modification date: Monday 6th January 2025 15:11:52
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 3 Notes]]

---



# JavaScript Overview  

- JavaScript (JS) is a programming language primarily used for web development.
- Its name was part of a marketing strategy by Netscape and Sun Microsystems and does not relate to Java.
- JS began as a scripting language for web pages and has evolved to include server-side development.
- The course primarily references Marijn Haverbeke's book "Eloquent JavaScript" as a comprehensive resource for learning.
- Brendan Eich created the first JavaScript interpreter in only 10 days.

## Basic JavaScript Concepts  

- JS is dynamically typed, meaning it does not require type annotations. For example, `let num = 42;`.
- There are two categories of values in JS: primitive types (e.g., numbers, strings, booleans, special values like null and undefined) and objects.
- Common math operators include addition (+), subtraction (-), multiplication (*), and division (/), with '+' also used for string concatenation (e.g., "foo" + "bar" results in "foobar").
- The `typeof` operator is used to determine value types, like `typeof 5` returning "number".


## Type Conversions in JavaScript  

- JavaScript uses both explicit and implicit conversions.
- Explicit conversion examples include `Number("5e3")` producing `5000`, `String(false)` resulting in "false", and `Boolean(1)` yielding `true`.
- Implicit conversions also occur; for example, `5 + ""` results in "5".
- Questions regarding implicit conversions can include checking the Boolean value of various inputs, such as `Boolean(0)` or `Boolean("hello")`.


## Variable Binding and Scope  

- Variables can be declared using `let`, `const`, and `var`, each with its own scope and mutability.
- `let` creates block-scoped variables, while `const` creates immutable ones.
- An example: trying to reassign a constant like `const c = "hello"; c = "hi";` results in an error.
- Using `var` can lead to challenging consequences due to function scope versus block scope during declarations.

## Control Flow and Functions  

- Control flow structures include `if`, `else`, `while`, `for`, and `switch` statements.
- Functions can be declared in various ways: traditional function declaration, function expressions, and arrow functions (lambda).
- For example, a function to calculate the power can be defined with default parameters: `function power(base, exp = 2) { return base ** exp; }`.
- Missing parameters default to `undefined`, and extra parameters are ignored without error.


## Arrays in JavaScript  

- Arrays are created using brackets and are zero-indexed, such as `let a = [1, 2, 3];`.
- Properties like `.length` give the number of elements, but it's not a function call (no parentheses).
- Arrays can be heterogeneous, containing mixed data types, e.g., `let a = ["a", 1, true, NaN, [1, 2]];`.
- Classic iterating methods include the `for...of` loop for elegant traversing.


## JavaScript Objects and Prototype Inheritance  

- JS objects are dynamic collections of properties (like dictionaries).
- Example: `let o = { a: 1, b: 2 };` allows property access via dot notation or bracket notation.
- Prototypes can link objects to share properties and behaviors, unlike classical class structures.
- Using class-based structures, functions can be used as constructors, such as `function Point(x,y) { this.x = x; this.y = y; }`.


## JavaScript Oddities  

- JavaScript has peculiar behaviors, often related to type coercion and comparisons.
- Examples include `true + true`, `0 == "0"`, and `0.1 + 0.2 === 0.3`.
- Developers should be aware of how JavaScript implicitly converts types and what that means for comparisons and operations.

## JavaScript and the Browser  

- JS can manipulate the Document Object Model (DOM) to dynamically change HTML content and structure.
- Developers can create elements, modify attributes, and update content, which reflects immediately in the browser.
- Document navigation can be performed using methods like `getElementsByTagName`, `getElementById`, and `querySelector`.
- Events can be handled to control user interactions with the page, including mouse clicks and keyboard inputs.


## jQuery Integration  

- jQuery simplifies many JavaScript tasks and is often used alongside vanilla JS for ease of DOM manipulation.
- Example constructions include using `$` for selecting elements and `.on()` for event handling.
- Users can create and append new DOM elements with simple methods, which can be particularly useful with dynamic content.
- jQuery was one of the strongest libraries for JS before the advancement of native features becoming more robust.



## Examples

```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p id="demo">JavaScript can change HTML content.</p>

<button type="button" onclick='document.getElementById("demo").innerHTML = "Hello JavaScript!"'>Click Me!</button>

</body>
</html>
```


```html
<!DOCTYPE html>
<html>
<body>

	<h2>Demo JavaScript in Body</h2>
	
	<p id="demo">A Paragraph.</p>
	
	<button type="button" onclick="myFunction()">Try it</button>
	
	<script>
	function myFunction() {
	  document.getElementById("demo").innerHTML = "Paragraph changed.";
	}
	</script>

</body>
</html> 
```
