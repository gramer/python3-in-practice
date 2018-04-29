TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
TEST_PATH=./tests
SOURCE_PATH=./practices


install-env: ## Install dev by pipenv
	@echo ${TAG}Clean complied files${END}
	pipenv install --dev
	pipenv install -e .
	@echo

lint:  ## Check code style
	@echo ${TAG}Check code style${END}
	pipenv run py.test --pylint --mypy ${SOURCE_PATH}
	@echo

clean-pyc: ## Clean complied files
	@echo ${TAG}Clean complied files${END}
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	@echo

clean-build: ## Clean build files
	@echo ${TAG}clean -pyc${END}
	rm -rf build/ dist/ *.egg-info
	@echo

test: clean-pyc ## Run unittests
	@echo ${TAG}Running unittests${END}
	pipenv run py.test --junitxml=junit.xml --cov practices  
	@echo

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.DEFAULT_GOAL = help
.PHONY = install-env lint clean-pyc clean-build test help
