PACKAGE_DIR := src/

.PHONY: install
install:
	@pip install --editable ."[dev]"
	@pre-commit install

.PHONY: test
test:
	@ruff $(PACKAGE_DIR)
	@mypy $(PACKAGE_DIR)
