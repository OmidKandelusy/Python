Example test cases using pytest to validate basic Python utilities.
Demonstrates fixtures, parameterized tests, and standard test functions 
for `unique_elements` and `remove_first_element`, covering normal and edge cases.

To run these tests, execute in the terminal:

    pytest -v test_filename.py

or, if you want to clear the pytest cache first:

    pytest --cache-clear -v test_filename.py

Pytest will automatically discover and run all functions starting with `test_`.