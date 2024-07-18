==========
Sweet Logs
==========


.. image:: https://img.shields.io/pypi/v/sweet_logs.svg
        :target: https://pypi.python.org/pypi/sweet_logs

.. image:: https://readthedocs.org/projects/sweet-logs/badge/?version=latest
        :target: https://sweet-logs.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A collection of logging formatters, filters, and functions. Original inspiration
came from `mCoding's video <https://youtu.be/9L77QExPmI0>`_ on logging in Python.


* Free software: GNU General Public License v3
* Documentation: https://sweet-logs.readthedocs.io.


Features
--------

Utilizing the sweet_logs package can be as simple as importing it and running
the setup function. This will configure the root logger to us the JSONFormatter
and log to the console via sys.stdout.

.. code-block:: python

    import sweet_logs

    sweet_logs.setup_logging()

    logger = logging.getLogger(__name__)
    logger.info('This is an info message')

The ``setup_logging`` function can take a few arguments to customize the
logging configuration. What is passed to the config option is passed to the
`logging.config.dictConfig <https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig>`_
function.

Credits
-------

This package was created with Cookiecutter_ and the `jorwoods/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`jorwoods/cookiecutter-pypackage`: https://github.com/jorwoods/cookiecutter-pypackage
