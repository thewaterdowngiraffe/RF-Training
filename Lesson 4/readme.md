

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
> note these commands exclude the provided solutions and lessons 1 and 2
update requirements if needed
```shell
pip install -r requirements.txt
```


robocop clear all
```shell
python -m robocop check --exit-zero --reports all --config='config/robot.toml'
```

unit test coverage get to 100%
```shell
python -m pytest --junitxml=pytest.xml --cov -ra --tb=auto --cov-branch --cov-report=term-missing --cache-clear -c config/robot.toml &&  rm ./.coverage && rm pytest.xml
```
>if you have issues with this command remove `&&  rm ./.coverage && rm pytest.xml` from the end

pylint
get this over 9/10 to consider a passing grade, but for a full pass aim for 10/10
```shell
python -m pylint * -f colorized --rcfile config/.pylintrc --clear-cache-post-run=true
```

