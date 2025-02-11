---
tags:
  - Notes
links: "[[Web tech Lecture 9]]"
creation date: 2025-01-06 17:48
modification date: Monday 6th January 2025 17:48:57
semester: Break before Semester 4
year: 2025
---


---
# [[Web Tech Lecture 9 Notes]]

---

# Environment  

- The environment is the context in which a web application operates, including digital and physical spaces that contain resources.
- Common environments used in development include Development, Testing, Staging (optional), and Production.



# Importance of Testing  

- Testing is essential to determine when a system starts and stops functioning correctly.
- Automated testing involves writing code to test code, which helps in detecting and addressing issues early.
- Implementing test-driven development means starting tests before writing the actual code, which improves software quality.


# Types of Testing  

- Pre-release testing includes several types:
- Post-release testing involves assessing deployed software to ensure it continues to function correctly after release.

# Unit Testing  

- Unit tests focus on small units of code and require tools like PHPUnit (or Pest for Laravel).
- Useful methods include assertions like assertTrue, assertFalse, assertArrayHasKey, and assertEquals, among others.
- Unit tests can also validate Eloquent models without needing a database connection by using the `make` method instead of `create`.



# Feature Testing  

- Feature tests examine interactions between models and can assert the functionality of routes in web applications.
- They can establish connections to a database within tests, helping to validate database operations.
- Useful methods for feature testing: get, post, put, assertOk, assertStatus, assertDatabaseHas, and others that verify the outcomes of requests.



# Browser Testing  

- Browser tests assess the interaction of web pages through the DOM, handling user interface interactions and complete use cases.
- Laravel's Dusk framework facilitates browser testing, requiring a specific setup and server operation.
- Essential methods for browser testing include visit, click, type, and assertions like assertSee and assertPresent.

# Post-release Testing  

- Testing in production encompasses various methods such as exception tracking, monitoring, smoke tests, canary releases, and A/B testing.
- Exception tracking helps in understanding faults in production, while monitoring provides insights about performance and system state.
- Smoke tests ensure critical features are operational, and canary releases introduce new features to a limited audience for risk mitigation.
- A/B testing serves to compare variations of a feature to determine the more effective version.


# Error Handling  

- In development, error handling should provide comprehensive details to aid debugging, including stack traces and logging.
- In production, users should see clear error messages without exposing details about the source code to maintain security, like 404/403 error pages.
- Environment variables like APP_DEBUG dictate the level of error detail revealed during operations, enhancing the distinction between development and production modes.


## Examples

### Unit Testing

Unit tests are designed to test individual pieces of code in isolation. Laravel utilizes PHPUnit for unit testing.

#### Example: Basic Unit Test

```php
use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class AlbumTest extends TestCase
{
    use RefreshDatabase;

    public function testCreate()
    {
        $this->assertEquals(0, Album::count());
        Album::create(['name' => 'Album 1']);
        $this->assertEquals(1, Album::count());
    }
}
```

### Feature Testing

Feature tests are used to test larger sections of your code, including interactions between different components. They allow for database connections and HTTP requests.

#### Example: Feature Test for Creating an Album

```php
use Tests\TestCase;

class AlbumTest extends TestCase
{
    public function testCreate()
    {
        $this->assertEquals(0, Album::count());

        $response = $this->post('/albums', ['name' => 'Album 1']);
        $response->assertStatus(302);
        $response->assertRedirect('/albums');
        
        $this->assertEquals(1, Album::count());
        $this->assertDatabaseHas('albums', ['name' => 'Album 1']);
    }
}
```

### Browser Testing

Browser tests allow you to interact with your application's front end, simulating user behavior. Laravel Dusk is used for this purpose.

#### Setting Up Dusk

1. Install Dusk:
    
    ```php
    composer require --dev laravel/dusk
    php artisan dusk:install
    ```
    
2. Create a test:
    
    ```php
    php artisan dusk:make AlbumTest
    ```
    
3. Update your
    
    ```plaintext
    .env
    ```
    
    file:
    
    ```plaintext
    APP_URL=http://localhost:8000
    ```
    
4. Start your server:
    
    ```plaintext
    php artisan serve
    ```
    
5. Run your Dusk tests:
    
    ```plaintext
    php artisan dusk
    ```
    

#### Example: Browser Test for Album Index

```php
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class AlbumTest extends DuskTestCase
{
    public function testIndex()
    {
        Album::create(['name' => 'Album 1']);

        $this->browse(function (Browser $browser) {
            $browser->visit(route('albums.index'))
                    ->assertSee('Album 1');
        });
    }
}
```

### Testing Middleware and Authentication

When testing routes that require authentication, you can disable middleware or simulate a logged-in user.

#### Example: Disabling Middleware

```php
public function testUserCreate()
{
    $this->withoutMiddleware();
    
    $data = ['name' => 'Album 1'];
    $response = $this->post('/user/albums', $data);
    // assertions...
}
```

#### Example: Acting as a User

```php
public function testUserCreate()
{
    $user = User::create(['email' => 'user@example.com', 'password' => bcrypt('password')]);

    $data = ['name' => 'Album 1'];
    $response = $this->actingAs($user)->post('/user/albums', $data);
    // assertions...
}
```