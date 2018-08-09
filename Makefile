# Shell to use with Make
SHELL := /bin/bash

# Set important Paths
PROJECT := elite
PROJECTPATH := $(CURDIR)
PYTHONPATH := /usr/bin/python

# Export targets not associated with files
.PHONY: test clean db run

all: clean test db run

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf model/app.db
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info

# Targets for testing
test:
	python tests/test.py

db:
	python $(PROJECTPATH)/model/Users.py db upgrade
	mv $(PROJECTPATH)/app.db $(PROJECTPATH)/model/

run:
	python app.py


.ONESHELL: clean

# Publish to gh-pages
# Make sure to change the prefix to the subdirectory of your docs build