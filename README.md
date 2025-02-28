# Python Task Assessment

This test is designed to assess your knowledge of the following technologies:

- Python
- Django and Django ORM
- Celery
- Redis
- MongoDB

## Requirements

You have 72 hours to complete this test.

### Project Structure

1. Create a Django project named `test_{yourFirstName}`.
2. Inside the project, create an app named `main`.

### Tasks

1. **POST Endpoint for API Calls**  

   Create a POST endpoint that accepts the payload with a `count` field. The `count` represents the number of times you will call the external API.

3. **Create a Django Model**  

   Create a Django model named `User` with the following fields:
   - `id` (primary key, integer)
   - `address` (JSONB)
   - `username` (varchar)
   - `password` (varchar)
   - `first_name` (varchar)
   - `last_name` (varchar)
   - `phone_number` (varchar)

4. **MongoDB Collection**  

   Create a MongoDB collection called `users`. The `id` field will be used as the index.

5. **Fetch Data from External API**  

   Use the following API endpoint: `GET https://fakestoreapi.com/users`. Fetch and store the response data into both the PostgreSQL database (`users` table) and MongoDB (`users` collection).

6. **API Call Count Based on Payload**  

   Depending on the `count` value in the payload, make multiple API calls. For example, if the payload is `{ "count": 100 }`, you will make 100 API calls to `https://fakestoreapi.com/users`.

7. **Parallel Processing with Celery and Redis**  

   Use Celery with Redis to process the API calls in parallel.  
   - If the `count` value is `10`, create 10 Celery tasks and send them to the queue for execution.

9. **GET Endpoints for Data Retrieval**  
   Create two GET endpoints:
   - One endpoint to retrieve all users from the PostgreSQL database.
   - One endpoint to retrieve all users from the MongoDB database.

### Bonus Tasks

1. **Redis Cache with TTL**  

   Implement Redis caching for the data with a TTL (Time To Live) of 5 minutes.

3. **Fetch Product by ID from Cache**  

   Write a function that fetches a product by ID from the `Product` model and stores the result in the Redis cache.  
   - Check the Redis cache first before querying the PostgreSQL database.

5. **Product List Endpoint**  

   Write a view that returns a list of all products from the `Product` model.

7. **Logging**  

   Add logs wherever possible for better traceability.

9. **Environment Variables**  

   Add a `.env` file to manage environment variables such as database configurations, Redis settings, and other configurations.

## Guidelines

- Use best practices when writing your code.
- Make sure you have a clean folder structure.
- Comment your code wherever necessary to improve readability.
- Create a GitHub repository and push your code there. Alternatively, you may create a zip file and send it.
- Ensure your local databases are set up for PostgreSQL and MongoDB.
  
## Database Setup

- **PostgreSQL**: Set up a PostgreSQL database to store user data in the `users` table.
- **MongoDB**: Set up MongoDB and create a `users` collection.

## Submission

Once you have completed the task, please share the following:

- GitHub repository URL or a zipped version of the code.
- Ensure that all requirements are met.

Good luck!
