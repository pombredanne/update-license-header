all:
	python setup.py build

check:
	python -m unittest discover

clean:
	python setup.py clean -a
	rm -rf dist

dist: all
	python setup.py bdist
