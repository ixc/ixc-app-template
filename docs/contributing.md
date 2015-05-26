# Contributing

Please follow these guidelines when making contributions to this app.

## Getting Started

Clone the repository and change directory:

    $ git clone git@github.com:ixc/<app_name>.git
    $ cd <app_name>

Create a virtualenv and install dependencies:

    $ pip install -U virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt -e .[dev,postgres]  # Omit unwanted optional extras.

Run the tests:

    (venv)$ tox  # All environments.
    (venv)$ tox -e django17-py27,django18-py27  # Given environments.
    (venv)$ ./manage.py test  # Virtualenv.

Run the `tests` project interactively:

    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py runserver

## Django Versions & Migrations

We support the current and previous release of Django, plus the current LTS
release. Consequently, it is important that all migrations for this app are
created with the lowest supported version of Django.

## Git

We are using the [Gitflow branching model]. Basically:

  * The `master` branch always contains production ready code, and each commit
    represents a release to production.
  * The `develop` branch serves as an integration branch for new features, and
    is merged into `master` when we are ready to tag a new release.
  * New features are developed in `feature/*` branches. Create a pull request
    when you are ready to merge a feature branch back into `develop`.

The [SourceTree] app (OS X and Windows) has built-in support for Gitflow, and
there is also a collection of [git-extensions] for command line users.

## Code Style

It's important that we all adopt a consistent code style to minimise code churn
and make collaboration easier.

  * Follow [PEP8] for Python code, unless there is a good reason not to.
  * Install the [EditorConfig] plugin for your preferred code editor.

## Documentation

Docs are probably more important than tests!

  * Write [Markdown] docs for all notable changes and additions.
  * Include examples so new contributors can get started quickly.
  * Include rationale when there are competing solutions, so people know why
    they should use our solution.
  * Keep the [changelog] up to date. Use plain language to describe changes,
    as it may be read by people who are not as familiar with the project or a
    particular feature as you.

## Tests

We don't need 100% test coverage, but we should at least have:

  * Unit tests for all regression bugs.
  * Unit or integration tests for complex, fragile, or important functionality.

## Releases

  * When the changelog for a release gets sufficiently long (half a page to a
    page) or major features or fixes are implemented, tag a release.

[changelog]: changelog.md
[EditorConfig]: http://editorconfig.org/
[git-extensions]: https://github.com/nvie/gitflow/
[Gitflow branching model]: http://atlassian.com/git/workflows#!workflow-gitflow
[Markdown]: http://daringfireball.net/projects/markdown/
[PEP8]: http://legacy.python.org/dev/peps/pep-0008/
[SourceTree]: http://sourcetreeapp.com/
