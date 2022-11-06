# Backend Development (PoC): Necati REST API (necati-api)

[![Language](https://img.shields.io/badge/language-python3-brightgreen)](https://www.python.org/)
[![License](https://img.shields.io/github/license/davait/necati-api)](https://opensource.org/licenses/GPL-3.0)
[![Repo size](https://img.shields.io/github/repo-size/davait/necati-api)](https://github.com/davait/necati-api)

This is a PoC of RESTful API with Python and MongoDB using Flask microframework. The project uses Docker (docker-compose) for easy to use, encapsulated and safe environment.

## Authors
- [Eugenio Grytsenko](https://github.com/davait)

## Stack

- Python v3.11
- Flask
- Pymongo
- Unittest
- Docker
- Swagger

## Usage

[Install Docker](https://www.docker.com/products/docker-desktop) if you don't have it yet and please use a clean docker installation without allocated resources like images, volumes, networks and so on. Run each container - for the database and for the API:

```sh
$ docker-compose up --build --force-recreate --no-deps -d database
$ docker-compose up --build --force-recreate --no-deps -d api
```

It will run both Web and MongoDB containers in Development environment on `localhost:9090`.
For other environments change FLASK_ENV in `docker-compose.yml` in `api` service declaration:

```sh
api:
   ...
    environment:
      - FLASK_ENV=production
```

You can use Development, Production or Testing or add your own environment in `src/config.py`.

## Structure

Here is a folder and file structure with explanation.

```
├── LICENSE
├── README.md
├── Makefile - Optional (you should install GNU make utility)
├── mongo-setup.js - Database initial user and roles setup
├── src
│   ├── Dockerfile
│   ├── app.py - Entry point of application
│   ├── app_tools.py - API tools (JSON encoder for ObjectId)
│   ├── config.py - Configuration with environments
│   └── requirements.txt - Dependencies
├── docker-compose.yml
├── vol-mongodb - Disk volume for MongoDB storage
└── tests
    └── text_base.py - Example test file
```

## Documentation

Thanks to handy decorators this boilerplate will generate Swagger with documentation on the fly.
By default Swagger runs on `/` so you should see it on `http://localhost:9090`. Read more [here](https://flask-restplus.readthedocs.io/en/stable/swagger.html).

## Testing

You can run tests easily within Docker container:

```
docker-compose run api python tests/test_base.py
```

## License

See LICENSE file.
