install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint
		
all: install lint test format

extract:
	python main.py extract

transform_load: 
	python main.py transform_load

query:
	python main.py general_query "SELECT t1.day_of_week, AVG(t1.births) as avg_daily_births, COUNT(*) as total_days_recorded FROM default.births2000 t1 JOIN default.births1994 t2 ON t1.year = t2.year GROUP BY t1.day_of_week ORDER BY avg_daily_births DESC LIMIT 3;"
