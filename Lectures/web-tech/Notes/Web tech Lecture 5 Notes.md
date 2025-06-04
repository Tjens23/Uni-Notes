---
tags:
  - Notes
links: "[[Web tech Lecture 5]]"
creation date: 2025-01-06 16:59
modification date: Monday 6th January 2025 16:59:42
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 5 Notes]]

---



# MVC Overview  

- Model-View-Controller (MVC) is a design pattern that provides a reusable solution to a common design problem, originally developed for desktop graphical user interfaces (GUIs).
- The concept dates back to 1979 when it was first introduced as the Thing-Model-View-Editor and was later streamlined in Smalltalk-80 in 1988.
- The MVC paradigm emphasizes the separation of user input, the modeling of external data, and visual feedback through three specialized object types: the Model, View, and Controller.
- The Model handles data and business logic, the View manages graphical/textual output, and the Controller interprets inputs, commanding the View and Model respectively.
- This separation of concerns enhances the modularity and maintainability of applications, making it particularly popular in web application development.


## Laravel MVC Framework  

- In Laravel, the MVC structure is implemented with clear routing, views, and controllers that interact with the database.
- Routing in Laravel is defined by modifying the `routes/web.php` file, allowing developers to specify URLs that the application will accept. For example, a simple route can be defined as:
- Laravel supports various HTTP methods (GET, POST, PUT, PATCH, DELETE) and provides additional methods like `Route::any()` and `Route::match()` for more complex routing requirements.
- Named routes improve maintainability; a route defined as `Route::get('/users/{id}', function ($id) {...})->name('users.show');` can be referred to consistently in views, as in `<a href="{{ route('users.show', [1]) }}">`.


## Working with Views in Laravel

Views in Laravel are a crucial component of the **Model-View-Controller (MVC)** architecture, responsible for rendering the graphical and textual output of your application. This section will cover the essentials of working with views, including how to create them, pass data, and utilize Blade templating.

### Creating Views

```PHP
Route::get('/', function () {
    return view('welcome');
});
```


###  Passing Data to Views

You can pass variables to views, allowing them to display dynamic content. Here’s how you can do it:

```php
Route::get('/', function () {
    $data = ['data1' => 'Data 1', 'data2' => 'Data 2'];
    return view('index', $data);
});
```

you can access these variables like so:

```PHP
<body>
    {{ $data1 }} <br>
    {{ $data2 }}
</body>
```


### Using Blade Templating

Laravel's Blade templating engine enhances your views with powerful features like loops and conditionals. Here’s an example using a loop to generate a dropdown:

```PHP
<select>
    @foreach($dataArray as $key => $value)
        <option value="{{ $key }}">{{ $value }}</option>
    @endforeach
</select>
```

## Controllers in Laravel  

- Controllers serve as intermediaries that handle requests, manipulate data (through models), and prepare views to display. They are created using Artisan commands like `php artisan make:controller CustomController`.

### Key Functions of Controllers

1. **Handling Requests**:
    
    - Controllers receive HTTP requests from users.
    - They can extract data from these requests to perform necessary actions.
2. **Interacting with Models**:
    
    - Controllers communicate with models to retrieve or manipulate data.
    - They encapsulate the business logic of the application.
3. **Returning Views**:
    
    - After processing data, controllers prepare and return views to the user.
    - They can also redirect users to different routes or actions.

### Creating a Controller

You can create a controller using the Artisan command line tool:

```plaintext
php artisan make:controller CustomController
```

This command generates a new controller file in the

```plaintext
app/Http/Controllers
```

directory.

### Example of a Controller Method

Here’s a simple example of a controller method that retrieves an album and returns a view:

```php
public function show($id) {
    $album = Album::find($id); // Retrieve album by ID
    return view('albums.show')->with('album', $album); // Return view with album data
}
```

### Routing to Controller Methods

In Laravel, you can define routes that point to specific controller methods. For example:

```php
use App\Http\Controllers\AlbumController;

Route::get('/albums/{id}', [AlbumController::class, 'show']);
```

### Handling Request Data

Controllers can also handle incoming request data. Here’s how to access request parameters:

```php
public function show($id) {
    $album = request('name'); // Access request parameter
    return view('albums.index')->with('album', $album);
}
```

### Redirecting Responses

Controllers can redirect users to different routes as needed:

```php
public function redirectToHome() {
    return redirect()->to('/'); // Redirect to home
}

public function redirectToAlbum($id) {
    return redirect()->route('albums.show', ['id' => $id]); // Redirect to album show route
}
```


## HTTP Resources and CRUD Operations  

- The HTTP protocol supports various methods for resource manipulation:
- Understanding CRUD operations (Create, Read, Update, Delete) is fundamental for working with resources in web applications, as they map directly to HTTP methods.
- Laravel provides capabilities for managing these operations through its resource controllers, simplifying the development process.


## Security Considerations in MVC  

- When using the POST method in Laravel, it is crucial to implement CSRF protection by using `@csrf` directives to prevent Cross-Site Request Forgery attacks.
- Without CSRF protection, users may encounter security errors, making it essential for maintaining application security.