# Typical test directory structure in Python 
* [https://gist.github.com/tasdikrahman/2bdb3fb31136a3768fac](https://gist.github.com/tasdikrahman/2bdb3fb31136a3768fac)
* [https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure/24266885#24266885](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure/24266885#24266885)

To run all the test cases, use the command ```python -m unittest discover -s tests```

Also you can run a single test module, a single ```unittest.TestCase```, or a single test method:

```
python -m unittest tests.<test_module>
python -m unittest tests.<test_module>.<test_case>
python -m unittest tests.<test_module>.<test_case>.<test_method>
```

For example:
```
python -m unittest tests.test_addition_subtraction
python -m unittest tests.test_addition_subtraction.TestAdditionSubtraction
python -m unittest tests.test_addition_subtraction.TestAdditionSubtraction.test_addition
```