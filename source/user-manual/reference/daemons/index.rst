.. _daemons:

Daemons
=======

+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Daemons                                           | Descriptions                                                    | Supported installations     |
+===================================================+=================================================================+=============================+
| :doc:`ossec-agentd <ossec-agentd>`                | Client side daemon that communicates                            | Agent                       |
|                                                   |                                                                 |                             |
|                                                   | with the server                                                 |                             |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-agentlessd <ossec-agentlessd>`        | Runs integrity checking on systems without                      | manager                     |
|                                                   |                                                                 |                             |
|                                                   | an agent installed                                              |                             |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-analysisd <ossec-analysisd>`          | Receives log messages and compares                              | manager                     |
|                                                   |                                                                 |                             |
|                                                   | them to the rules                                               |                             |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-authd <ossec-authd>`                  | Adds agents to Armor manager                                    | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-csyslogd <ossec-csyslogd>`            | Forwards Armor alerts via syslog                                | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-dbd <ossec-dbd>`                      | Inserts alert logs into a database                              | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-execd <ossec-execd>`                  | Executes active responses                                       | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-logcollector <ossec-logcollector>`    | Monitors configured files and commands for                      | manager, agent              |
|                                                   |                                                                 |                             |
|                                                   | new log messages                                                |                             |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-maild <ossec-maild>`                  | Sends Armor alerts via email                                    | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-monitord <ossec-monitord>`            | Monitors agent connectivity and compresses log files            | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-remoted <ossec-remoted>`              | Communicates with agents                                        | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-reportd <ossec-reportd>`              | Creates reports from Armor alerts                               | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`ossec-syscheckd <ossec-syscheckd>`          | Checks configured files for security changes                    | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`armor-modulesd <armor-modulesd>`            | Armor module manager                                            | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+


.. toctree::
    :hidden:
    :maxdepth: 1

    ossec-agentd
    ossec-agentlessd
    ossec-analysisd
    ossec-authd
    ossec-csyslogd
    ossec-dbd
    ossec-execd
    ossec-logcollector
    ossec-maild
    ossec-monitord
    ossec-remoted
    ossec-reportd
    ossec-syscheckd
    armor-modulesd
