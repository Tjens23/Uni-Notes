---
tags:
  - Notes
links: 
creation date: 2025-01-06 17:35
modification date: Monday 6th January 2025 17:35:30
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 8 Notes]]

---

## JavaScript and Client-Side Development

- JavaScript is primarily executed in the browser, enabling interactivity within web pages.
- User actions traditionally required full page reloads, leading to slower experiences.
- In response to this, Ajax was developed to allow for asynchronous web page updates without reloading the entire page.
- The primary serialization formats used for data exchange in Ajax include XML (less common today) and JSON. JSON (JavaScript Object Notation) is preferred due to its lightweight and human-readable structure.


## Ajax Overview  

- Ajax stands for Asynchronous JavaScript and XML, facilitating dynamic content loading.
- With Ajax, responses can be handled in JavaScript for real-time data updates on the web page, avoiding the need for full refreshes.


## Promises in JavaScript  

- A promise represents an asynchronous action with three potential states: Pending, Resolved, or Rejected.
- Example of creating promises:
- Promises can be chained using .then() methods, allowing for sequential processing.
- Errors are propagated through rejections and can be caught with .catch() handlers, enhancing error management in asynchronous code.

### What is a Promise?

A **JavaScript promise** represents the eventual completion (or failure) of an asynchronous operation and its resulting value. A promise can be in one of three states:

- **Pending**: The initial state, neither fulfilled nor rejected.
- **Resolved**: The operation completed successfully.
- **Rejected**: The operation failed.

### Creating Promises

You can create promises using the

```js
Promise
```

constructor:

```js
let resolvedPromise = Promise.resolve(15); // Creates a resolved promise
let rejectedPromise = Promise.reject("fail"); // Creates a rejected promise
```

### Chaining Promises

Promises can be chained using the

```js
.then()
```

method, which allows you to handle the resolved value:

```js
Promise.resolve(25)
    .then(i => Math.sqrt(i)) // Resolves to 5
    .then(j => console.log(j)); // Logs 5
```

### Error Handling with Promises

Errors in promises are propagated as rejections. You can catch these errors using the

```js
.catch()
```

method:

```js
Promise.resolve(25)
    .then(i => { throw new Error("Foo"); }) // Throws an error
    .catch(err => console.log(err.message)); // Logs "Foo"
```

### Example: Using Promises with AJAX

In modern JavaScript, the

```js
fetch
```

API is commonly used for making AJAX requests and returns a promise. Here’s an example that demonstrates how to handle errors when fetching data from a JSON file:

```js
fetch("file.json")
    .then(response => {
        if (response.status === 200) {
            return response.json(); // Parse JSON if the response is OK
        } else {
            throw new Error("Network response was not ok: " + response.statusText);
        }
    })
    .then(data => {
        console.log(data); // Handle the data received
    })
    .catch(error => {
        console.error("There was a problem with the fetch operation:", error.message); // Handle errors
    });
```



## Fetch API in Ajax  

- The Fetch API simplifies making Ajax requests and returns promises.
- Example of a fetch call that checks response status:
- Fetch includes helpful methods to parse response bodies, such as text() for text responses and json() for JSON responses.
- Note that a 404 response is considered successful in terms of receiving a response from the server, but it should still be handled appropriately.

## RESTful APIs  

- RESTful APIs utilize the aforementioned constraints, and resources are identified through URIs.
- Common HTTP methods used in RESTful APIs include GET, POST, PUT, PATCH, and DELETE.
- Data is often exchanged in formats such as JSON or XML, similar to how data is handled in Ajax calls.
- Example API endpoint:
- It is important to utilize appropriate naming conventions and adhere to HTTP standards when designing RESTful APIs.

## Examples

### Setting Up Routes

In Laravel, routes are defined in the

```plaintext
routes/web.php
```

or

```plaintext
routes/api.php
```

files. Here’s how to define a simple GET and POST route:

```php
// routes/api.php

use App\Http\Controllers\AlbumController;

Route::get('/albums', [AlbumController::class, 'index']);
Route::post('/albums', [AlbumController::class, 'store']);
```

### Creating a Controller

You can create a controller using the Artisan command line tool. Here’s an example of a controller that handles album data:

```plaintext
php artisan make:controller AlbumController
```

Then, in your

```plaintext
AlbumController.php
```

, you can define methods to handle requests:

```php
// app/Http/Controllers/AlbumController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Album;

class AlbumController extends Controller
{
    public function index()
    {
        return response()->json(Album::all());
    }

    public function store(Request $request)
    {
        $album = Album::create($request->all());
        return response()->json($album, 201);
    }
}
```

### CSRF Protection

When making POST requests from JavaScript, ensure you include the CSRF token. Here’s how to do that with Axios:

```php
axios.post('/albums', {
    name: 'New Album',
    artist: 'Artist Name',
    _token: '{{ csrf_token() }}' // Include CSRF token
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error(error);
});
```

### Fetch API Example

Using the Fetch API to interact with your Laravel backend can be done like this:

```php
fetch('/api/albums', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRF-TOKEN': '{{ csrf_token() }}'
    },
    body: JSON.stringify({
        name: 'New Album',
        artist: 'Artist Name'
    })
})
.then(response => {
    if (!response.ok) throw new Error('Network response was not ok');
    return response.json();
})
.then(data => console.log(data))
.catch(error => console.error('There was a problem with the fetch operation:', error));
```

### Handling AJAX Requests in Laravel

You can handle AJAX requests in your Laravel application easily. Here’s an example of how to return JSON data:

```php
// In your controller method
public function getAlbums()
{
    $albums = Album::all();
    return response()->json($albums);
}
```

###  RESTful API Example

Here’s an example of a RESTful API route setup in Laravel:

```php
// routes/api.php

Route::apiResource('albums', AlbumController::class);
```

This single line creates routes for all standard RESTful actions (index, store, show, update, destroy).

### Middleware for API Authentication

If you want to protect your API routes, you can use middleware. Here’s how to apply it:

```php
// routes/api.php

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});
```