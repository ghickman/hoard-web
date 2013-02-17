Hoard
=====

Keep your environment variables in one place

Installation
~~~~~~~~~~~~

Clone the codebase::

    git clone https://github.com/ghickman/hoard-web


Install the requirements::

    pip install -r requirements.txt


Sync the database::

    python manage.py syncdb


Usage
~~~~~

Access your hoard of environment variables with the command line `app
<http://github.com/ghickman/hoard-cli>`_.

API
~~~

You can also access your hoard with the JSON API available at::

    http://<domain>/api/project/<name>

