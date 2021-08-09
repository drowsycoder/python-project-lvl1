install:
	chmod +x brain_games/scripts/brain_games.py
	chmod +x brain_games/scripts/brain_calc.py
	chmod +x brain_games/scripts/brain_even.py
	chmod +x brain_games/scripts/brain_gcd.py
	chmod +x brain_games/scripts/brain_prime.py
	chmod +x brain_games/scripts/brain_progression.py
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --build -r testpypi

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games