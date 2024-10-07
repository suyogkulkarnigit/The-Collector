MAKEFLAGS += --silent

WHAT ?= meta
PYTHON_CMD ?= $(shell command -v python3 || command -v python)
PIP_CMD ?= $(shell command -v pip3 || command -v pip)

.PHONY: check-pipenv install-pipenv  install
check-pipenv:
	@which pipenv > /dev/null || { \
		echo "pipenv is not installed. Installing pipenv..."; \
		$(PIP_CMD) install pipenv || { echo "Failed to install pipenv. Please install it manually."; exit 1; }; \
	}

install: check-pipenv setup
	pipenv run $(PIP_CMD) install -r req.txt

setup:
	pipenv run $(PYTHON_CMD) setup.py install

run:
	pipenv run $(PYTHON_CMD) main.py -w $(WHAT)

rm:
	pipenv --rm