# Overview

TODO

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

Install the app into your virtualenv:

    (venv)$ pip install -e git+ssh://git@github.com/ixc/<app_name>.git#egg=<app_name>

Update your settings module:

    INSTALLED_APPS += ('{{ app_name }}', )

## Usage

TODO

## HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to build a static HTML
version that you can host anywhere:

    (venv)$ mkdocs build

Or you can use the built-in dev server to preview your documentation as you're
writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
