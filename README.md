# Beautiful Asserts

A demo project for the blogpost "[Beautiful asserts with your Django Test Client](https://www.maerteijn.nl/en/blog/beautiful-asserts-with-your-django-test-client)".

## Development setup

### Requirements

- At least python 3.9


### Install the django project with poetry
```bash
pyenv virtualenv 3.9 beautiful-asserts  # or your alternative to create a virtualenv
pyenv activate beautiful-asserts
pip install poetry
poetry install
```

Optional, when you're not creating the virtualenv yourself poetry will do it for you. You can activate the poetry virtualenv like so:
```bash
source $(poetry env info --path)/bin/activate
```

### Development server

Run the development server to see the example view and form:
```bash
manage.py runserver
```

Now browse to http://localhost:8000

### Test

Run the testsuite:
```bash
pytest
```
