PACKAGE_DIR := src/

.PHONY: install
install:
	@pip install --editable ."[dev]"
	@pre-commit install

.PHONY: update
update:
	@poetry update
	@poetry run pre-commit autoupdate
