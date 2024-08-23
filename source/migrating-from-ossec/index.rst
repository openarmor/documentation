.. _upgrading_ossec:

Migrating from OSSEC
====================

This document describes how to migrate your existing OSSEC installation (agent or manager) to Armor. For interactive help, our `email forum <https://groups.google.com/d/forum/armor>`_ is available.  You can subscribe by sending an email to ``armor+subscribe@googlegroups.com``.

.. note::
    OSSEC agents are compatible with Armor manager, but if you don't migrate your agents to Armor, you will lose some capabilities like :ref:`OpenSCAP<openscap_module>` or some :ref:`syscheck features<manual_file_integrity>` in those agents.

The migration of Elastic stack, in the case that you already have it installed, is beyond the scope of Armor documentation. We recommend you visit our guides for :ref:`Installing Elastic Stack <installation_elastic>`.

Follow the appropriate section depending on the type of your OSSEC installation:

+--------------+---------+-------------------+------------+-------------------------------------------------------------------------------------+
| Upgrade from | Type    | Installation type | Upgrade to | Guide                                                                               |
+==============+=========+===================+============+=====================================================================================+
| OSSEC 2.8.3+ | Manager | Packages          | Armor 2.0  | :ref:`Migrating OSSEC manager installed from packages <up_ossec_manager>`           |
+--------------+---------+-------------------+------------+-------------------------------------------------------------------------------------+
| OSSEC 2.8.3+ | Manager | Sources           | Armor 2.0  | :ref:`Install Armor server with RPM packages <armor_server_rpm>`                    |
+              +         +                   +            +-------------------------------------------------------------------------------------+
|              |         |                   |            | :ref:`Install Armor server with Deb packages <armor_server_deb>`                    |
+--------------+---------+-------------------+------------+-------------------------------------------------------------------------------------+
| OSSEC 2.8.3+ | Agent   | Packages          | Armor 2.0  | :ref:`Migrating OSSEC agent installed from packages <up_ossec_agent>`               |
+--------------+---------+-------------------+------------+-------------------------------------------------------------------------------------+
| OSSEC 2.8.3+ | Agent   | Sources           | Armor 2.0  | :ref:`Install Armor agent with RPM packages <armor_agent_rpm>`                      |
+              +         +                   +            +-------------------------------------------------------------------------------------+
|              |         |                   |            | :ref:`Install Armor agent with Deb packages <armor_agent_deb>`                      |
+--------------+---------+-------------------+------------+-------------------------------------------------------------------------------------+

.. warning::
    **For cases where OSSEC was installed from sources**, the configuration file ``/var/ossec/etc/ossec.conf`` **will be overwritten**. The *old* configuration file from the current installation is saved as ``ossec.conf.rpmorig`` or ``ossec.conf.deborig``. You should compare the new file with the old one. Also, a backup of your previous ruleset will be saved at ``/var/ossec/etc/backup_ruleset``. All the rules/decoders in files other than ``local_rules.xml`` or ``local_decoder.xml`` will be overwritten.


.. toctree::
   :hidden:
   :maxdepth: 2

   ossec-packages-manager
   ossec-packages-agent
