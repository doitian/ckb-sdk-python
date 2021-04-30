test:
	python -m unittest discover

requirements.txt: setup.py
	pip-compile

publish:
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine --version || pip install twine
	twine upload dist/*

clean:
	rm -rf dist requirements.txt

setup:
	pip install -r requirements.txt

.PHONY: test requirements.txt publish clean
