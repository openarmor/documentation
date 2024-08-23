.. _connect_armor_app:

Connect the Armor App with the API
==================================

In this section, we'll register the Armor API (installed on the Armor server) into the Armor App in Kibana:

1. Open a web browser and go to the Elastic Stack server's IP address on port 5601 (default Kibana port). Then, from the left menu, go to the Armor App.

  .. thumbnail:: ../../images/installation/armorapp/kibana_app.png
    :align: center
    :width: 100%

2. Click on ``Add new API``.

  .. thumbnail:: ../../images/installation/armorapp/connect_api.png
    :align: center
    :width: 100%

3. Before filling out the fields, go to your Armor server and using the command prompt as root set a non-default credentials to protect your Armor API:

  .. code-block:: bash

    # Replace your desired username for myUserName.
    $ cd /var/ossec/api/configuration/auth
    $ sudo node htpasswd -c user myUserName

    # Do not forget to restart the API to apply the changes:
    $ systemctl restart armor-api
    $ service armor-api restart

4. Fill Username and Password with appropriate credentials you created in previous step.  Enter ``http://MANAGER_IP`` for the URL, where ``MANAGER_IP`` is the real IP address of the Armor qserver. Enter "55000" for the Port.

  .. thumbnail:: ../../images/installation/armorapp/fields_api.png
    :align: center
    :width: 100%

.. note:: If you have followed the Armor Documentation for Nginx, the URL must be ``https://localhost``.

6. Click on ``Save``.

  .. thumbnail:: ../../images/installation/armorapp/app_running.png
    :align: center
    :width: 100%

Next steps
----------

Once the Armor and Elastic Stack servers are installed and connected, you can install and connect Armor agents. How to do it:

- :ref:`Debian/Ubuntu <armor_agent_deb>`
- :ref:`RedHat/CentOS <armor_agent_rpm>`
- :ref:`Windows <armor_agent_windows>`
