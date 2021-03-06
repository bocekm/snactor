clean:
	@rm -rf build/ dist/ *.egg-info
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +

install:
	# WORKAROUND FOR: https://github.com/ansible/ansible/issues/31741
	pip install --upgrade setuptools
	pip install -r requirements.txt
	pip install .

test:
	py.test --flake8 --cov=snactor

test-all:
	tox

.PHONY: clean install test test-all
