---
tags:
  - Notes
links: 
creation date: 2025-01-06 17:27
modification date: Monday 6th January 2025 17:27:33
semester: Break before Semester 4
year: 2025
---


---
# [[Web tech Lecture 7 Notes]]

---



## Cookies  

- Cookies are small client-side files, typically limited to 4KB in size, used for session management, personalization, and tracking.
- Cookies are set by servers through special header options and are sent back to servers with each request.
- There are different types of cookies: first-party cookies (associated with the domain of the page, e.g., mysite.com) and third-party cookies (from a different domain, e.g., adsdomain.com).
- Security concerns include the visibility of cookie values, the ability of users to alter cookies, and the risk of copying cookies to another browser.
- Performance can be impacted by multiple cookies; large quantities of cookie data sent back to the server can slow down requests.


## Sessions  

- Sessions are used to maintain state between page requests and are managed server-side, in contrast to cookies which are client-side.
- Each session requires a unique session ID stored in a cookie, which the server uses to retrieve the appropriate session data.
- Session data can be stored in various ways including files, secure encrypted cookies, databases, or caching systems like memcached or Redis.
- Laravel's session configuration can be found in config/sessions.php. The framework also provides handy methods for managing session data, such as session('key'), session()->put('key', 'value'), and session()->forget('key').
- Flash sessions are temporary sessions that last only for a single page request, useful for transferring status messages from one page to another.


## Authentication  

- Authentication is the process of verifying user identities, typically through a combination of username/email and password.
- Laravel comes with a built-in User model and migration for managing users. It's critical never to store passwords in plain text; use hashing instead.
- Important authentication methods in Laravel include auth()->login($user), auth()->check(), and auth()->logout().
- Session management is intrinsic to authentication, where the authenticated user's ID is stored in the session and correspondingly in cookies.
- The application must handle user sessions effectively, often storing only user identifiers in sessions, while sensitive information remains secure.


## Authorization  

- Authorization refers to the permission given to authenticated users to perform certain actions or access specific resources within the application.
- In Laravel, routes can be restricted to either authenticated users or guest users using middleware, such as Route::get('/albums', ...)->middleware('auth').
- More specific authorization can be achieved using Gates and Policies to define who can perform which actions (e.g., distinguishing between students and admin users).
- Utilizing `auth()->check()` and Blade directives like @auth can facilitate conditional rendering based on the user's authentication state.
- Middleware can be utilized for checking user roles (e.g., AdminAuthenticated) and must be registered in the Kernel to be functional within routes.


## Middleware  

- Middleware in Laravel acts as a bridge between a request and response, allowing for request modification or rejection, and response modification.
- Custom middleware can be created using artisan commands, with functionalities such as authorization checks embedded within the handle method.
- Middleware must be registered in app/Http/Kernel.php, enabling its use throughout the application's routes.
- The example of an AdminAuthenticated middleware illustrates how to enforce role-based access controls by aborting unauthorized requests.
- Overall, middleware is essential for adding layers of security and functionality without altering the core logic of the application's routes.


## Examples

#### Basic Authentication Flow

1. **User Registration**: To register a user, you can create a controller method like this:
    
    ```php
    public function register(Request $request) {
        $validatedData = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);
    
        $validatedData['password'] = bcrypt($validatedData['password']);
        User::create($validatedData);
        
        return redirect()->route('login')->with('success', 'Registration successful!');
    }
    ```
    
2. **User Login**: To log in a user, use the following method:
    
    ```php
    public function login(Request $request) {
        $credentials = $request->only('email', 'password');
    
        if (auth()->attempt($credentials)) {
            return redirect()->intended('dashboard')->with('success', 'Logged in successfully!');
        }
    
        return back()->withErrors([
            'email' => 'The provided credentials do not match our records.',
        ]);
    }
    ```
    
3. **User Logout**: Logging out a user can be done simply with:
    
    ```php
    public function logout() {
        auth()->logout();
        return redirect()->route('login')->with('success', 'Logged out successfully!');
    }
    ```
    

### Authorization

Authorization determines what authenticated users can do. Laravel provides a robust system using **Gates** and **Policies**.

#### Using Gates

Gates are simple closures that determine if a user can perform a given action.

```php
Gate::define('view-album', function ($user, $album) {
    return $user->id === $album->user_id;
});
```

You can check a gate in a controller:

```php
public function show(Album $album) {
    if (Gate::allows('view-album', $album)) {
        return view('albums.show', compact('album'));
    }

    abort(403);
}
```

#### Using Policies

Policies are classes that organize authorization logic around a particular model.

1. **Create a Policy**: Use Artisan to create a policy:
    
    ```php
    php artisan make:policy AlbumPolicy
    ```
    
2. **Define Methods**: In
    
    ```php
    AlbumPolicy.php
    ```
    
    , define methods for authorization:
    
    ```php
    public function update(User $user, Album $album) {
        return $user->id === $album->user_id;
    }
    ```
    
3. **Register the Policy**: In
    
    ```php
    AuthServiceProvider.php
    ```
    
    , register your policy:
    
    ```php
    protected $policies = [
        Album::class => AlbumPolicy::class,
    ];
    ```
    
4. **Using the Policy**: Check authorization in your controller:
    
    ```php
    public function edit(Album $album) {
        $this->authorize('update', $album);
        return view('albums.edit', compact('album'));
    }
    ```
    

### Middleware for Authorization

Middleware can be used to restrict access to routes based on user roles.

1. **Create Middleware**: Generate middleware with:
    
    ```php
    php artisan make:middleware AdminAuthenticated
    ```
    
2. **Middleware Logic**: Implement the logic in
    
    ```php
    AdminAuthenticated.php
    ```
    
    :
    
    ```php
    public function handle($request, Closure $next) {
        if (!auth()->user() || !auth()->user()->isAdmin()) {
            abort(403);
        }
        return $next($request);
    }
    ```
    
3. **Register Middleware**: Add to
    
    ```plaintext
    app/Http/Kernel.php
    ```
    
    :
    
    ```php
    protected $routeMiddleware = [
        'admin' => \App\Http\Middleware\AdminAuthenticated::class,
    ];
    ```
    
4. **Using Middleware in Routes**: Apply middleware to routes:
    
    ```php
    Route::get('/albums/manage', [AlbumsController::class, 'manage'])
        ->middleware('admin');
    ```
    

### Session Management

Laravel provides a straightforward way to manage sessions, which are essential for maintaining user state.

#### Session Configuration

You can configure session settings in

```php
config/session.php
```

. Common storage options include:

- **File**: Stored in
    
    ```php
    storage/framework/sessions
    ```
    
    .
- **Database**: Requires a sessions table.
- **Redis/Memcached**: For fast, cache-based storage.

#### Using Sessions

Here are some useful methods for session management:

```php
// Store data in session
session(['key' => 'value']);

// Retrieve data from session
$value = session('key');

// Check if a session key exists
if (session()->has('key')) {
    // Do something
}

// Flash data for one-time use
session()->flash('message', 'This is a flash message!');
```

