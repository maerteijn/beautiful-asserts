.PHONY: install lint test cov format

default: install

install:
	poetry install

lint:
	flake8 src tests

test:
	pytest

cov:
	pytest --cov=beautiful_asserts --cov-report=html --cov-report=term

format:
	black src tests
	isort src tests
