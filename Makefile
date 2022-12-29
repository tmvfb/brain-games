install:
	poetry build
	poetry install
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games
