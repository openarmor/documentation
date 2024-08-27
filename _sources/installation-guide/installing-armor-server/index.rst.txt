.. _installation:

Installing Armor server
=======================

The Armor server can be installed on any Unix-like operating system, most commonly on Linux. It is more convenient install it via packages if one is available for your distribution.  However, build and install it from sources is also pretty simple.

There are two components that you usually have to install on a Armor server: the manager and the API. In addition, for distributed architectures (where the Armor server sends data to a remote Elastic Stack cluster) you will need to install Filebeat.

There are several options to install a Armor server, depending on the operating system and whether or not you wish to build from source. Consult the table below and choose how to proceed:

+------------------------------------------------------------------------+-------------------------------------------------------------+
| Type                                                                   | Description                                                 |
+========================================================================+=============================================================+
| :ref:`RPM packages <armor_server_rpm>`                                 | Install Armor server on CentOS/RHEL/Fedora.                 |
+------------------------------------------------------------------------+-------------------------------------------------------------+
| :ref:`DEB packages <armor_server_deb>`                                 | Install Armor server on Debian/Ubuntu.                      |
+------------------------------------------------------------------------+-------------------------------------------------------------+
| :ref:`Sources <sources_installation>`                                  | Install Armor server from source code.                      |
+------------------------------------------------------------------------+-------------------------------------------------------------+

.. note::
    Installing Armor Server on a 64-bit operating system is highly recommended since the Armor API is not available on 32-bit platforms. Without the Armor API, much of the functionality of the Armor Kibana App will not work. Similarly, if you are using Red Hat or CentOS for your Armor Server platform, make sure it is version 6 or higher to properly install Armor API.


.. toctree::
   :hidden:
   :maxdepth: 2

   armor_server_rpm
   armor_server_deb
   sources_installation
