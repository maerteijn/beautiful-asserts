# Beautiful Asserts

A demo project for the blogpost "Beautiful asserts with your Django Test Client".

## Development setup

### Requirements

- At least python 3.9 (pyenv managed recommended)


### Install the django project with poetry
```bash
pyenv virtualenv 3.9 beautiful-asserts  # or your alternative to create a venv
pyenv activate beautiful-asserts
pip install poetry
make install
```

Optional, when you're not creating the virtualenv yourself poetry will do it for you. You can activate the poetry venv like so:
```bash
source $(poetry env info --path)/bin/activate
```

### Linting
`flake8-black` and `flake8-isort` are installed and configured
```bash
make lint
```

### Formatting

`black` and `isort` are configured
```bash
make format
```

### Test

Pytest with coverage is default enabled
```bash
make test
```
