.. _upgrading_same_minor:

Upgrade from the same minor version
=====================================

Use these instructions if you are upgrading your Armor installation within the same minor version. As an example, from 2.0.0 to 2.1.1.

Upgrade Armor manager
---------------------

a) Upgrade Armor server on CentOS/RHEL/Fedora:

.. code-block:: bash

    $ sudo yum upgrade armor-manager

b) Upgrade Armor server on Debian/Ubuntu:

.. code-block:: bash

    $ sudo apt-get update && sudo apt-get install --only-upgrade armor-manager

Upgrade Armor agent
---------------------

a) Upgrade Armor agent on CentOS/RHEL/Fedora:

.. code-block:: bash

    $ sudo yum upgrade armor-agent

b) Upgrade Armor agent on Debian/Ubuntu:

.. code-block:: bash

    $ sudo apt-get update && sudo apt-get install --only-upgrade armor-agent
