#!/bin/bash

mypy --ignore-missing-imports preconvert_numpy/
isort --check --diff --recursive preconvert_numpy/
black --check -l 100 preconvert_numpy/
flake8 --max-line 100 --ignore F403,F401
safety check
bandit -r preconvert_numpy/
