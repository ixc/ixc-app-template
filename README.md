# Readme

Docs can be found in the [docs](docs/index.md) folder.

## App Template

This is a bare-bones skeleton app template, for use with the
`django-admin.py startapp` command.

You will need `django 1.4+`, `git`, `python 2.7+`, `pip` and `virtualenv`  to
create a new app with this template.

    # Create environment variables for the app and module name, so we can use
    # it in the following commands. E.g. `django-foo-bar` and `foo_bar`
    $ export APP=<app_name>
    $ export MODULE=<module_name>

    # Create app from template.
    $ mkdir -p ~/Projects/$APP
    $ django-admin.py startapp -e md -n .coveragerc \
    --template=https://github.com/ixc/ixc-app-template/archive/master.zip \
    $MODULE ~/Projects/$APP

    # Make `manage.py` executable, for convenience.
    $ cd ~/Projects/$APP
    $ chmod 755 manage.py

    # Create git repository and push initial commit.
    $ git init
    $ git add -A
    $ git commit -m 'Initial commit.'
    $ git remote add origin git@github.com:ixc/$APP.git
    $ git push

    # Create virtualenv and install requirements.
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt

    # Run tests against all environments.
    (venv)$ tox

Now start work on your app! You might want to start with:

  * Remove the `App Template` section (these instructions) from `README.md`
    (this file).
  * Update the `requirements.txt` file (e.g. add forked, pre-release and
    private dependencies that can't go in the `setup.py` file).
  * Update the `tox.ini` file (e.g. configure environments and add conditional
    dependencies).
  * Update the `{{ app_name }}/apps.py` file (e.g. add `verbose_name` and
    register signal handlers).
  * Update the `{{ app_name }}/tests/settings.py` file (e.g. configure apps).
  * Add forms, models, templates, views, and tests!
