VENV=.venv

run:
	python src/

venv: requirements.txt
	python -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

venv-delete:
	rm -rf $(VENV)

clean:
	rm -rf **/*/__pycache__/