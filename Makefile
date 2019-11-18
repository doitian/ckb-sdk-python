ifeq (${VIRTUAL_ENV},)
  PIPENV_RUN := pipenv run
endif

test:
	${PIPENV_RUN} python -m unittest discover

publish:
	rm -rf dist
	${PIPENV_RUN} python setup.py sdist bdist_wheel
	${PIPENV_RUN} twine --version || ${PIPENV_RUN} pip install twine
	${PIPENV_RUN} twine upload dist/*
