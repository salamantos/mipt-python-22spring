def test_string_format():
    name = 'Mike'

    expected = 'Hello, Mike!'
    actual = f'Hello, {name}!'

    assert actual == expected

# to run, enter "pytest -v ." in console
# or "pytest -v test_pytest.py"
# or even "pytest -v test_pytest.py::test_string_format"
