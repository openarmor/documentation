.. _upgrading_same_major:

Upgrade from the same major version
=====================================

Use these instructions if you are upgrading your Armor installation within the same major version. As an example, from 2.0.1 to 2.1.1.

Upgrade Armor manager
---------------------

Before upgrading the Armor manager, stop ``ossec-authd`` in case that it is running in background. Since Armor 2.1.0, ``ossec-authd`` should be configured in the :doc:`auth section <../../user-manual/reference/ossec-conf/auth>` of ``ossec.conf``.


a) Upgrade Armor server on CentOS/RHEL/Fedora:

.. code-block:: bash

    $ sudo yum upgrade armor-manager

b) Upgrade Armor server on Debian/Ubuntu:

.. code-block:: bash

    $ sudo apt-get update && sudo apt-get install --only-upgrade armor-manager

Upgrade Armor API
---------------------

a) Upgrade Armor API on CentOS/RHEL/Fedora:

.. code-block:: bash

    $ sudo yum upgrade armor-api

b) Upgrade Armor API on Debian/Ubuntu:

.. code-block:: bash

    $ sudo apt-get update && sudo apt-get install --only-upgrade armor-api


Upgrade Armor agent
---------------------

a) Upgrade Armor agent on CentOS/RHEL/Fedora:

.. code-block:: bash

    $ sudo yum upgrade armor-agent

b) Upgrade Armor agent on Debian/Ubuntu:

.. code-block:: bash

    $ sudo apt-get update && sudo apt-get install --only-upgrade armor-agent


Upgrade Armor Kibana App
-------------------------


1) On your terminal, remove the current Armor Kibana App:

    .. code-block:: bash

        $ /usr/share/kibana/bin/kibana-plugin remove armor

2) Once the process is completed, you must stop Kibana with:

  a) For Systemd:

    .. code-block:: bash

        $ systemctl stop kibana

  b) For SysV Init:

    .. code-block:: bash

        $ service kibana stop

3) Remove the current kibana bundles:

.. code-block:: bash

    $ rm -rf /usr/share/kibana/optimize/bundles

4) Upgrade Armor Kibana App (this can take a while):

.. code-block:: bash

    $ /usr/share/kibana/bin/kibana-plugin install https://packages.armor.com/armorapp/armorapp.zip

5) Once the process is completed, you must start Kibana again with:

  a) For Systemd:

    .. code-block:: bash

        $ systemctl start kibana

  b) For SysV Init:

    .. code-block:: bash

        $ service kibana start
