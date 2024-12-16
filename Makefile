#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`/src

#* Docker variables
IMAGE := wfp_survey_toolbox
VERSION := latest

#* Installation
.PHONY: install
install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv .venv
	. .venv/bin/activate && uv pip install -r requirements.txt

.PHONY: pre-commit-install
pre-commit-install:
	. .venv/bin/activate && pre-commit install

#* Formatters
.PHONY: check-codestyle
check-codestyle:
	python -m isort --diff --check-only ./
	python -m black --check ./
	python -m darglint -v 2 **/*.py

#* Linting
.PHONY: test
test:
	set "PYTHONPATH=%cd%\src" && pytest --cov-report=html --cov=src/wfp_survey_toolbox tests/

.PHONY: mypy
mypy:
	. .venv/bin/activate && mypy ./

.PHONY: check-safety
check-safety:
	. .venv/bin/activate && safety scan --full-report
	. .venv/bin/activate && bandit -ll --recursive wfp_survey_toolbox tests

.PHONY: lint
lint: test check-codestyle mypy

#* Documentation
.PHONY: docs
docs:
	. .venv/bin/activate && mkdocs build

.PHONY: docs-serve
docs-serve:
	. .venv/bin/activate && mkdocs serve

#* Docker
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove
