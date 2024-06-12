
venv-linux:
	python3 -m venv venv

venv-linux-activate:
	source venv/bin/activate


venv-windows:
	python -m venv venv

venv-windows-new:
	python3 -m venv venv


install:
	pip install -r requirements.txt

