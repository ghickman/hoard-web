Trove
-----

Keep your environment variables in one place

Installation
~~~~~~~~~~~~

Clone the codebase::

    git clone https://github.com/ghickman/trove


Install the requirements::

    pip install -r requirements.txt


Enable `hstore` in the database::

    create extension hstore


Sync the database::

    python manage.py syncdb


Usage
~~~~~

Access your trove of secrets with the command line `app
<http://github.com/ghickman/trove-cli>`_.

API
~~~

You can also access your trove with the JSON API available at::

    http://<domain>/api/project/<name>

