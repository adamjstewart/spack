Hi {github.actor}! I noticed that the following package(s) don't have maintainers:
{steps.maintainers.outputs.packages-without-maintainers}

Are you interested in adopting these package(s)? If so, simply add the following to the package class:
```python
    maintainers = ['{github.actor}']
```
You don't have to be a Spack expert or package developer in order to be a "maintainer", it just gives us a list of users willing to review PRs or debug issues relating to this package.
