# HELP
.PHONY: help

app_name = hn_collector

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Removes build artifacts and any logs
	rm -rf *.egg-info && rm -rf dist && rm -rf *.log* && rm -rf build
	rm -rf venv && rm -f Pipfile && rm -f Pipfile.lock

venv: ## Creates or updates project's virtual enviornment. 
	python3 -m venv venv --prompt venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install setuptools
	venv/bin/pip install -r requirements.txt
	echo "To activate, run: source venv/bin/activate"

update: ## Updates dependencies in virtual environment
	venv/bin/pip install -r requirements.txt

test: ## verifies neo4j and neomodel work
	venv/bin/python test_neo4j.py
	venv/bin/python test_neomodel.py

run: venv ## Launches app using virtual environment
	CONFIG_ENV=config.env 
	venv/bin/python -m $(app_name)
