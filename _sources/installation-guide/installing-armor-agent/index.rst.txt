.. _installation_agents:

Installing Armor agent
======================

The Armor agent runs on the hosts that you want to monitor. It is multi-platform and provides the following capabilities: log and data collection, file integrity monitoring, rootkits and malware detection, and security policy monitoring. In addition, it talks to the Armor manager, sending data in near real-time through an encrypted and authenticated channel.

There are several options to install a Armor agent, depending on the operating system and whether or not you wish to build from source. Consult the table below and choose how to proceed for a given agent:

+-------------------------------------------------+--------------------------------------------------+
| Type                                            | Description                                      |
+=================================================+==================================================+
| :doc:`RPM packages <armor_agent_rpm>`           | Install Armor agents on CentOS/RHEL/Fedora.      |
+-------------------------------------------------+--------------------------------------------------+
| :doc:`DEB packages <armor_agent_deb>`           | Install Armor agents on Debian/Ubuntu.           |
+-------------------------------------------------+--------------------------------------------------+
| :doc:`Windows installer <armor_agent_windows>`  | Install Armor agents on Windows.                 |
+-------------------------------------------------+--------------------------------------------------+
| :doc:`Mac OS installer <armor_agent_macos>`     | Install Armor agents on Mac OS                   |
+-------------------------------------------------+--------------------------------------------------+
| :doc:`Solaris installer <armor_agent_solaris>`  | Install Armor agents on Solaris                  |
+-------------------------------------------------+--------------------------------------------------+
| :doc:`Sources <armor_agent_sources>`            | Install Armor agents from source code.           |
+-------------------------------------------------+--------------------------------------------------+

.. note:: Deploying agents to a large number of servers or endpoints can be easier using automation tools like Puppet, Chef, SCCM or Ansible. Consider exploring these options if that is your case.

.. toctree::
    :hidden:
    :maxdepth: 2

    armor_agent_rpm
    armor_agent_deb
    armor_agent_windows
    armor_agent_macos
    armor_agent_solaris
    armor_agent_sources
