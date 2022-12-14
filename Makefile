install:
	pip install -r requirements.txt

format:
	black *.py

lint: 
	pylint

test:
	python -m pytest tests.py