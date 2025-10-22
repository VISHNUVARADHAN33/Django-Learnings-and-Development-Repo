# Django Learnings and Development Repo

This repository is a learning and development playground for Django projects and related clients (JS/Python). It contains a small Django backend with apps for products, articles, search, and a few client examples.

## Contents

- `backend/` - Django project and apps (products, articles, search, api, etc.)
- `js_client/` - Simple JavaScript client examples
- `py_client/` - Small Python client scripts for exercising the API
- `requirements.txt` - Python dependencies

## Quick setup (Windows)

1. Create a virtual environment and activate it (cmd.exe):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```cmd
pip install -r requirements.txt
```

3. Run migrations and start the development server:

```cmd
cd backend
python manage.py migrate
python manage.py runserver
```

By default the dev server will be available at http://127.0.0.1:8000/.

## Running tests

From the `backend` directory run:

```cmd
python manage.py test
```

## Notes about `backend/products/validators.py`

This file contains a `UniqueValidator` instance used with DRF serializers. You may also see two small validator functions commented out — these were experimental/alternative validators kept for reference:

- `validate_title(value)`: earlier custom uniqueness check using `Product.objects.filter(title__iexact=value)`.
- `validate_title_no_hello(value)`: example that rejected titles containing the substring `"iphone"`.

If you're cleaning the codebase, it's safe to either:
- Remove these commented functions (they were kept only for reference), or
- Re-enable them and add them to serializer fields explicitly if you need custom behavior.

If you want, I can remove the commented code and add a short git commit message for the cleanup.

## Next steps / suggestions

- Consider adding model-level `UniqueConstraint` for database-enforced uniqueness (recommended for production).
- Move any validators that reference the DB into serializer fields (avoid heavy DB ops at module import time).
- Add a contributor guide or simple architecture diagram if others will use this repo.

---

If you'd like, I can:
- Remove the commented code in `backend/products/validators.py` and commit the change, or
- Add more detailed setup steps (e.g., Docker, PostgreSQL) if you plan to productionize this.
