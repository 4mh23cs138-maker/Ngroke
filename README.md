# FastAPI + SQLAlchemy + Vercel Postgres

## Project Structure

```text
.
|-- api/
|   `-- index.py
|-- app/
|   |-- core/
|   |   `-- config.py
|   |-- db/
|   |   `-- database.py
|   |-- models/
|   |   `-- user.py
|   |-- routes/
|   |   `-- users.py
|   |-- schemas/
|   |   `-- user.py
|   `-- main.py
|-- .env.example
|-- main.py
|-- requirements.txt
`-- vercel.json
```

## Run locally

1. Create and activate virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variable:
   ```bash
   set POSTGRES_URL=postgres://username:password@host:5432/dbname
   ```
   On PowerShell:
   ```powershell
   $env:POSTGRES_URL="postgres://username:password@host:5432/dbname"
   ```
4. Start app:
   ```bash
   uvicorn main:app --reload
   ```

## Routes

- `POST /users/` create user
- `GET /users/` get all users
- `GET /users/{user_id}` get user by id

## Deploy (bonus)

1. Push code to Git repository.
2. Import project in Vercel.
3. Add `POSTGRES_URL` in Vercel Project Environment Variables.
4. Deploy.
