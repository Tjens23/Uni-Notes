---
tags:
  - Notes
links: "[[Web tech Lecture 2]]"
creation date: 2025-01-06 15:00
modification date: Monday 6th January 2025 15:00:02
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 2 Notes]]

---



# HTML Basics

- HTML elements consist of start and end tags, encapsulating the content. For example, `<p>Hello World</p>` has a start tag `<p>`, end tag `</p>`, and content "Hello World".
- An HTML page is structured with several elements, typically including `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`. Example structure:
- Common HTML elements include:
- HTML can include empty elements like `<img src="image">` for images, and `<br/>` for line breaks.



# CSS Fundamentals

- CSS (Cascading Style Sheets) is used for defining the style and layout of web pages, complementing HTML, which structures content.
- A basic CSS rule format is `selector { declarations; }`. For example, `p {background-color: purple;}` sets the background color for all `<p>` elements.
- CSS can be embedded in HTML in three ways:
- CSS properties define appearance aspects such as `background-color`, `color`, `width`, and `height`, with possible values including color names, units (px, %), and functions like `calc()`, `rgb()`, etc.

# CSS Selectors and Specificity  

- CSS selectors identify which elements to style. Common selectors include:
- CSS specificity determines which styles are applied when multiple rules conflict. The order of precedence is: Inline > Internal > External. More specific selectors win if rules have equal specificity.
- If necessary, `!important` can be used to force a style, overriding all other rules.


# Advanced CSS Features  

- Advanced selectors in CSS allow for intricate targeting, such as selecting elements based on their relationship:
- Pseudo-classes modify the style of an element based on its state, for instance, `:hover` for mouse-over effects, while pseudo-elements target specific portions of elements, such as `::first-line`.


# Layout and the Box Model

- The CSS Box Model defines how elements are rendered in terms of padding, borders, and margins. For example:
- Elements can be classified as block-level (e.g., `div, p`) which take up full width and cause new lines, or inline elements (e.g., `span, a`) that do not disrupt the flow.
- CSS properties such as `display` can alter default element behavior, including options like `none`, `inline`, `block`, and `inline-block`.
- Flexbox and Grid layouts provide advanced options for responsive design, allowing for more complex arrangements and alignments within web pages.


## Internal CSS

- An internal CSS is used to define a style for a single HTML page.
- An internal CSS is defined in the `<head>` section of an HTML page, within a `<style>` element.


```html
<!DOCTYPE html>  
<html>  
<head>  
<style>  
	body {background-color: powderblue;}  
	h1   {color: blue;}  
	p    {color: red;}  
</style>  
</head>  
<body>  
  
<h1>This is a heading</h1>  
<p>This is a paragraph.</p>  
  
</body>  
</html>
```

The example sets the text color of ALL the `<h1>` elements (on that page) to blue, and the text color of ALL the `<p>` elements to red. In addition, the page will be displayed with a "powderblue" background color


## External CSS

- An external style sheet is used to define the style for many HTML pages.
- To use an external style sheet, add a link to it in the `<head>` section of each HTML page:

```html
<!DOCTYPE html>  
<html>  
<head>  
  <link rel="stylesheet" href="styles.css">  
</head>  
<body>  
  
<h1>This is a heading</h1>  
<p>This is a paragraph.</p>  
  
</body>  
</html>
```


```css
body {  background-color: powderblue;}  
h1 {  color: blue;}  
p {  color: red;}
```

