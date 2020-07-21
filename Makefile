install:
	poetry install

import: install
	poetry add pytest-cov
	poetry add requests

lint:
	poetry run flake8 page_loader

build:
	poetry build

pub:
	poetry publish -r ppt

test:
	poetry run pytest --cov=page_loader tests/ --cov-report xml

dt:
	poetry run pytest --cov=page_loader tests/ --cov-report term-missing 