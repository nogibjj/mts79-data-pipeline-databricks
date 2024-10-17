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
	python main.py general_query "SELECT COALESCE(t1.day_of_week, t2.day_of_week) AS day_of_week, AVG(t1.births) AS avg_births_2000,AVG(t2.births) AS avg_births_1994,COUNT(t1.date_of_month) AS days_recorded_2000,COUNT(t2.date_of_month) AS days_recorded_1994 FROM default.births2000db t1 FULL OUTER JOIN default.births1994db t2 ON t1.day_of_week = t2.day_of_week GROUP BY COALESCE(t1.day_of_week, t2.day_of_week) ORDER BY day_of_week;"
