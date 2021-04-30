test:
	python -m unittest discover

requirements.txt: setup.py
	pip-compile

publish: setup requirements.txt
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine --version || pip install twine
	twine upload dist/*

clean:
	rm -rf dist ckb.egg-info

setup:
	pip install pip-tools wheel twine
	pip install -r requirements.txt

.PHONY: test publish clean setup
