1. Documentation including setup instructions, project structure, and explanation of functionalities.

Setup Instructions:

1.Ensure you have Python and Django installed.
2.Clone the project from the repository.
3.Navigate to the project directory.
4.Install project dependencies using pip install -r requirements.txt.
5.Apply migrations using python manage.py migrate.
6.Run the development server using python manage.py runserver.

Project Structure:

1. vms/: Main project directory.
2. vms/: Django project directory.
3. settings.py: Django settings file.
4. urls.py: Main URL configuration file.
5. vmsapp/: Django app directory.
6. views.py: Contains view functions.
7. models.py: Contains database models.
8. forms.py: Contains Django forms.
9. urls.py: URL configuration for the app.
10. templates/: HTML templates.
11. static/: Static files (CSS, JavaScript, etc.).
12. media/: Directory for uploaded media files.
13. db.sqlite3: SQLite database file.
14. requirements.txt: File containing project dependencies.


Explanation of Functionalities and System Flow:

* User Authentication: Allows users to sign up, log in, and log out.
* Dashboard: Provides separate dashboards for regular users and security department users.
* Vehicle Registration: Allows users to register vehicles with details such as vehicle name, number, type, etc.
* Vehicle Listing: Displays a list of vehicles registered by the current user.
* Vehicle Search: Allows searching for vehicles based on purchase order numbers.
* Quality Check: Enables users to perform quality checks on vehicles.
* Vehicle Checkout: Allows users to check out vehicles after completing quality checks.

2. Database Schema Design:

* UserProfile: One-to-one relationship with the Django User model, indicating whether the user belongs to the security department.
* Vendor: Stores information about vendors supplying products.
* Product: Represents products supplied by vendors.
* Vehicle: Stores details of registered vehicles, associated with users and products.
* QualityCheck: Represents quality checks performed on vehicles.


3. How to Run the Project:

1. Follow the setup instructions provided above.
2. Run the development server using python manage.py runserver.
3. Access the application in a web browser at http://localhost:8000/.


4. Explanations for Each Component and Functionality:

1. Views: Contains functions handling HTTP requests and returning HTTP responses.
2. Models: Defines database schema and relationships between entities.
3. URLs: Maps URLs to view functions.
4. Settings: Contains project settings including database configuration, static files, media files, etc.
5. Templates: Handles the front-end HTML/CSS/JavaScript code codes

5. Documentation of Endpoints, Request Methods, Request Parameters, and Response Formats:

Postman documents: https://documenter.getpostman.com/view/33234022/2sA2rFRL3N#f0f45658-7a67-4742-896b-dcf3c44f3763

1. Endpoint: /signup/
 * Request Method: POST
 * Request Parameters: Form data containing user details.
 * Response Format: Redirect to login page upon successful registration.

2. Endpoint: /login/
 * Request Method: POST
 * Request Parameters: Form data containing username and password.
 * Response Format: Redirect to respective dashboards based on user type upon successful login.

3. Endpoint: /vehicle_registration/
 * Request Method: GET, POST
 * Request Parameters: Form data containing vehicle details.
 * Response Format: Rendered HTML with a form for vehicle registration.

4. Endpoint: /vehicle_list/
 * Request Method: GET, POST
 * Request Parameters: Form data containing purchase order number.
 * Response Format: Rendered HTML with a list of vehicles matching the purchase order number.

6.Endpoint: /vehicle_details/<vehicle_id>/
 * Request Method: GET
 * Request Parameters: Vehicle ID in the URL.
 * Response Format: Rendered HTML displaying details of the specified vehicle.

7.Endpoint: /quality_check/<vehicle_id>/
 * Request Method: POST
 * Request Parameters: Form data containing quality check status.
 * Response Format: Redirect to vehicle details page upon successful quality check.

8.Endpoint: /vehicle_checkout/<vehicle_id>/
 * Request Method: POST
 * Request Parameters: None
 * Response Format: Redirect to vehicle details page upon successful checkout.
