# Restaurant Info System Backend Introduction

## Prerequisites

To run the project, the Docker should be installed. The Postman is recommended for validating the APIs.

## Deployment

Use the 

```dockerfile
docker-compose up --build
```

command for initializing the project dependencies, setting-up databases, and running the project.

## API Documentation

| API Path                                                     | API HTTP Method | Description                                                  |
| ------------------------------------------------------------ | --------------- | ------------------------------------------------------------ |
| http://127.0.0.1:8000/api/restaurant/query-all               | GET             | Query the names of all the restaurants.                      |
| http://127.0.0.1:8000/api/restaurant/query-detail/pk         | GET             | Query the detailed information of a specific restaurant according to the primary key `pk`. |
| http://127.0.0.1:8000/api/restaurant/add                     | POST            | Add a restaurant record.                                     |
| http://127.0.0.1:8000/api/restaurant/delete/pk               | DELETE          | Delete a restaurant record according to the primary key `pk`. |
| http://127.0.0.1:8000/api/restaurant/update/pk               | PUT             | Update a restaurant record according to the primary key `pk`. |
| http://127.0.0.1:8000/api/restaurant/query-filtered/?location=xxx&cuisine=yyy | GET             | Query restaurants according to location or cuisine.          |
| http://127.0.0.1:8000/api/restaurant/query-all-paged         | GET             | Query the names of all the restaurants with pagination       |

I also gave some Postman API examples for how to send the API requests in the `./test` directory. You can import the `RestaurantSystemAPIs.postman_collection_2.1.json` file to the Postman to send the requests. The template data are in the `template_data.json` file. You can use them for adding initial data to the database.

## Authentication

The CSRF (Cross-Site Request Forgery) token is applied for authentication. It is used against cross-site attackers. If you use the Postman for sending the requests there won't be any problems because using Postman for sending requests won't be a CSRF attack. But if you use the browser for sending a POST, DELETE, or PUT request, a CSRF token is needed. Like this:

| Header      | ****                             |
| ----------- | -------------------------------- |
| X-csrftoken | IbizIeiE2Y04uV586Ug209nlQPdt0jDy |
