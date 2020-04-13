.PHONY: environment clean format test

#################################################################################
# COMMANDS                                                                      #
#################################################################################

clean: ## Clean environment.
	@rm -rf venv .pytest_cache *.egg-info **/__pycache__

environment: ## Create Python virtual environment and install dependencies.
	@echo "Creating environment..."
	@python3 -m venv venv
	@( \
		. venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r requirements.txt;\
	)

format: ## Format source code.
	@black .

test: ## Run tests.
	@pytest

run: ## Run application
	@uvicorn bike_charts.main:app --reload

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'