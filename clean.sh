#!/bin/bash

isort --recursive preconvert_numpy/
black preconvert_numpy/ -l 100
