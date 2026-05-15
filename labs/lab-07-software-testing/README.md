# Lab 7: Software Testing Practices

This laboratory demonstrates the differences between various testing strategies in Python using `pytest`.

## Folder Structure
- `src/`: Contains the application logic.
  - `math_operations.py`: Pure logic. No external dependencies.
  - `database.py`: Infrastructure code. Connects to a SQLite database and executes SQL.
  - `user_service.py`: Business logic. Depends on `database.py`.
- `tests/`: Contains the automated tests.
  - `unit/`: Tests that run entirely in memory. Very fast. They use "Mocking" to simulate the database.
  - `integration/`: Tests that interact with real infrastructure (an in-memory SQLite database). Slower, but verify SQL syntax.

## How to Run the Tests

1. Navigate to this folder in your terminal:
   ```bash
   cd labs/lab-07-software-testing
   ```

2. Install the requirements (we use `pytest`):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest -v
   ```

## What to observe?
Look at `tests/unit/test_user_service_mocked.py`. Notice how we test the `user_service` without ever creating a real database. We use `MagicMock()` to fake the database responses. This guarantees the test is lightning fast and not dependent on external factors.

Then, look at `tests/integration/test_database.py`. Here we use a real SQLite database (`:memory:`). If you make a typo in the SQL query in `database.py`, the unit tests will still pass (because they bypass it), but this integration test will catch the error!
