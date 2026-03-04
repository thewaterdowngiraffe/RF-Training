

# Standards
rules:
- unit tests
- formatting
- linting
- assertion (When and how to use it)
- error handling
    - general
    - best practice
    - throwing errors
- Documentation
    - Python
    - Robot Framework
    - readme

# resources
- [markdown](https://www.markdownguide.org/basic-syntax/)
- [pep-8](https://pep8.readthedocs.io)
- [robot framework errors](https://robocop.dev/stable/linter/linter/)

# Checkers

commands
move into directory
```shell
pip install -r requirements.txt
cd <replace with target dir>
```

robocop clear all
```shell
python -m robocop check --exit-zero --reports all --config='../config/robot.toml'
```

unit test coverage get to 100%
```shell
python -m pytest --junitxml=pytest.xml --cov -ra --tb=auto --cov-branch --cov-report=term-missing --cache-clear &&  rm ./.coverage && rm pytest.xml
```

pylint
get this over 8. aim for 10/10
```shell
python -m pylint * -f colorized --rcfile ../config/.pylintrc --clear-cache-post-run=true
```

