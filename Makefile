define PROJECT_HELP_MSG

Usage:
    make clean                  remove intermediate files (see CLEANUP)
    make ${VENV}                make a virtualenv in the base directory (see VENV)
    make python-reqs            install python packages in requirements.pip

endef
export PROJECT_HELP_MSG

help:
	echo $$PROJECT_HELP_MSG | less

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

${VENV}:
	python3 -m venv $@ 

python-reqs: requirements.txt | ${VENV}
	pip install --upgrade -r requirements.txt

CLEANUP = *.pyc

clean:
	rm -rf ${CLEANUP}

.PHONY: help git-config start-jupter python-reqs setup clean
