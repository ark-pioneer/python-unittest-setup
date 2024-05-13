# python-unittest-setup

### Quickstart
```sh
$ git clone git@github.com:ark-pioneer/python-unittest-setup.git && cd python-unittest-setup
$ pip install -r requirements.txt
```

## Tests

to discover tests to run:
```sh
$ python -m unittest
```
to run a specific test package:
```sh
$ python -m unittest greeter.test_greet
```
to run a specific test case (group of tests)
```sh
$ python -m unittest greeter.test_greet.TestGreet
```
to run a specific unit test (individual test)
```sh
$ python -m unittest greeter.test_greet.TestGreet.test_sayHello
```

[unittest | docs](https://docs.python.org/3/library/unittest.html#command-line-interface)


## Linting
```sh
$ ruff check
$ ruff check --fix
$ ruff format
```