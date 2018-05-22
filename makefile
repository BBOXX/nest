.PHONY: clean init
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force {} +

REQUIREMENTS := $(shell find -L -name '*requirements*.txt')
init: venv
	# search for all requirements.txt in tasksets/ and install those too
	venv/bin/pip install $(addprefix  -r , $(REQUIREMENTS))
venv: 
	virtualenv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
lint:
	flake8 --exclude=.tox