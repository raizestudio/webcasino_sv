.PHONY: test coverage

# Reset migrations
reset-migrations:
	find . -path "*/migrations/*.py" ! -name "__init__.py" -not -path "./venv/*" -delete
	find . -path "*/migrations/*.pyc"  -not -path "./venv/*" -delete

# Run all tests with pytest
test:
	pytest

# Run tests with coverage
coverage:
	pytest --cov=. --cov-report=term-missing --cov-report=html

# Run tests with coverage without report
coverage-no-report:
	pytest --cov=. --cov-report=term-missing
	
# Format code with Black and isort
format:
	black . && isort .

# Lint code with Flake8
lint:
	flake8 .

# Install dependencies
install:
	pip install -r requirements.txt
	python manage.py install