Trove API Enpoints
==================


/login
------

POST
~~~~

Authenticates the user with the given credentials, payload should look like
the following::

    {
        'username': 'username',
        'password': 'your_password',
    }

The API will return a token like so::

    {
        'token': 'alongtokenstring'
    }



/projects
---------

GET
~~~

List all projects, returning a list of objects like so::

    [
        {
            'name': 'project',
            'envs': [
                'dev',
                'live',
            ]
        }, {
            'name': 'another_project',
            'envs': [
                'dev',
            ]
        }
    ]



/projects/:name
---------------

GET
~~~

Retrieve a specific project::

    {
        'name': 'project',
        'envs': [
            'dev',
            'live',
        ]
    }


DELETE
~~~~~~

Delete a specific project


/envs
-----

GET
~~~

List all envs, returning a list of objects like so::

    [
        {
            'name': 'dev',
            'projects': [
                'project',
                'another_project',
            ]
        }, {
            'env': 'live',
            'projects': [
                'project',
            ]
        }
    ]



/envs/:name
-----------

GET
~~~

Retrieve a given env::

    {
        'env': 'live',
        'projects': [
            'project',
        ]
    }


DELETE
~~~~~~

Delete a specific env



/projects/:name/envs/:name
--------------------------

GET
---

Retrieve the environment variables for the given deployment::

    {
        'key': value,
        'key': value,
        ...
    }



/projects/:name/envs/:name/keys/:key
----------

DELETE
~~~~~~

Delete a specific key/value pair on the deployment

