---
title: Code Quality Standards & Tools
sidebar: Handbook
showTitle: true
---

# Code Quality Standards & Tools

In a team setting it's important that all developers follow the same coding standards. 

Following a defined set of standards and "doing things the same":
- makes the codebase easier to maintain
- makes code reviews faster by producing the smallest diffs possible
- keeps the focus of code reviews on higher level issues - rather than on mundane/time-wastey syntax issues.

Here are the tools that we all (must) use to ensure that we're all following the same standards.

```python
# let's code!
```


## Python Tools

1. [Flake8](https://flake8.pycqa.org/en/latest/) - To check for errors, styling issues and complexity.
2. [isort](https://pycqa.github.io/isort/) - To automatically sort & separate code imports (standard library, third party, local).
3. [Black](https://pypi.org/project/black/) - For code formatting.
4. [Bandit](https://bandit.readthedocs.io/en/latest/) - To find common security issues in python code, such as hardcoded password strings, deserialization of untrusted data, etc.
5. [Safety](https://pypi.org/project/safety/) - To check python dependencies for known security vulnerabilities.

* Use the `--profile black` [option](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html) when using isort with Black to avoid code style collisions.

## Running Code Quality Tools

You should run run quality tools:
1. While coding (inside your IDE / editor).
2. Before committing code (using a [pre-commit](https://pre-commit.com/) [hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks#:~:text=The%20pre%2Dcommit%20hook%20is,to%20inspect%20in%20the%20code)).
3. When code is check in to source control (via [CI/CD pipeline]).