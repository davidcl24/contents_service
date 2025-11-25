# ContentsService

This service manages the creation and update of contents for a 
streaming app.

## Characteristics
- It offers a full CRUD for the following contents:
  * Actors
  * Directors
  * Genres
  * Movies
  * Shows
  * Episodes

- It connects to a PostgreSQL database making use of the SQLModel library.

- Modular structure based on FastAPI routers.

## Configuration
The app uses environment variables to build the database connection URL.
If there was no environment variable, it will take a default value from a .env file.
```
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=default
DB_PASSWORD=example
DB_DATABASE=streamingdb
```

## How to setup
To start your Uvicorn server:

* Run `pip install -r requirements.txt` to install and setup dependencies
* Start Uvicorn endpoint with `fastapi run ./app/main.py` or `uvicorn app.main:app --host 0.0.0.0 --port 8000`

Now the server will be active at [`localhost:8000`](http://localhost:8000).

