# Restaurant Info System Backend Introduction

## Prerequisites

To run the project, the Docker should be installed. The Postman is recommended for validating the APIs.

## Deployment

Use the 

```dockerfile
docker-compose up --build
```

command for initializing the project dependencies, setup databases, and run the project. In the first run, as the backend is dependent on the database, its container might stop as the database might not be ready yet, it should be online once you restart it. So there is room for improvement.



Then if you can see the following administration page displayed normally, the application is started fine:

http://127.0.0.1:8000/admin

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

Sadly, I didn't install Postgres database locally and the docker image is used instead. I cannot initialize the database tables and records locally. The database schema is created once the container is started (`python manage.py makemigrations`). So you may have to use the "add" API to add some data to the tables first. The data should be added in the body like this.



I also give some Postman API examples for how to send the API requests in the `./test` directory. You can import the `RestaurantSystemAPIs.postman_collection_2.1.json` file to the Postman to send the requests. The template data are in the `template_data.json` file. You can use them for adding initial data to the database.

## Authentication

I also use the CSRF (Cross-Site Request Forgery) token for authentication. It is used against cross-site attackers. If you use the Postman for sending the requests there won't be any problems because using Postman for sending requests won't be a CSRF attack. But if you use the browser for sending a POST, DELETE, or PUT request, a CSRF token is needed. Like this:

| Header      | ****                             |
| ----------- | -------------------------------- |
| X-csrftoken | IbizIeiE2Y04uV586Ug209nlQPdt0jDy |

## Remarks

If you meet any problem during deployment or other steps, please contact via email zlbee_work@outlook.com or WeChat :). 