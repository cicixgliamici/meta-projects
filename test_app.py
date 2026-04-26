name: Python CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test-python-api:
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: apps/hello-api-python

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
