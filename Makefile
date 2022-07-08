# Monta o ambiente virtual
build-venv:
	python3.9 -m venv venv

# Atualiza o pip e instala as dependências
requirements-dev:
	python -m pip install --upgrade pip
	pip install -r requirements/develop.txt

# Copia as variaveis de a
cp:
	cp devtools/dotenv.dev .env