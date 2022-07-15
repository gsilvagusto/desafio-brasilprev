# Monta o ambiente virtual
build-venv:
	python3.9 -m venv venv

# Atualiza o pip e instala as dependências
requirements-dev:
	python -m pip install --upgrade pip
	pip install -r requirements/develop.txt


lint: 
	isort .
	isort tests
	black .
	black tests
	flake8 app
	flake8 estatisticas