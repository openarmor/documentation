
.. _ossec-control:

ossec-control
=============

The ossec-control script is used to start, stop, configure, or check on the status of Armor processes.  This script can enable or disable client-syslog, database logging, agentless configurations, integration with slack and pagerduty, and debug mode.

+-------------+---------------------------------------------------------------------------------------------------------+
| **start**   | Start the Armor processes.                                                                              |
+-------------+---------------------------------------------------------------------------------------------------------+
| **stop**    | Stop the Armor processes.                                                                               |
+-------------+---------------------------------------------------------------------------------------------------------+
| **restart** | Restart the Armor processes.                                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **reload**  | Restart all Armor processes except ossec-execd.                                                         |
|             |                                                                                                         |
|             | This allows an agent to reload without losing active response status.                                   |
|             |                                                                                                         |
|             | This option is not available on a local Armor installation.                                             |
+-------------+---------------------------------------------------------------------------------------------------------+
| **status**  | Determine which Armor processes are running.                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **enable**  | Enable Armor functionality.                                                                             |
+             +-----------------+---------------+-----------------------------------------------------------------------+
|             | Allowed options | database      | Enable the ossec-dbd daemon for logging to a database.                |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | client-syslog | Enable ossec-csyslogd for logging to remote syslog.                   |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | agentless     | Enable ossec-agentlessd for running commands on systems               |
|             |                 |               |                                                                       |
|             |                 |               | without Armor agents.                                                 |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | integrator    | Enable integrator for connection to external APIs and alerting tools. |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server                                                                |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | auth          | Enable the ossec-authd daemon for add agents to the manager.          |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server                                                                |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | debug         | Run all Armor daemons in debug mode.                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **disable** | Disable Armor functionality.                                                                            |
+             +-----------------+---------------+-----------------------------------------------------------------------+
|             | Allowed options | database      | Disable the ossec-dbd daemon for logging to a database.               |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | client-syslog | Disable ossec-csyslogd for logging to remote syslog.                  |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | agentless     | Disable ossec-agentlessd for running commands on systems              |
|             |                 |               |                                                                       |
|             |                 |               | without Armor agents.                                                 |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server and local                                                      |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | integrator    | Disable integrator for connection to external APIs and alerting tools.|
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server                                                                |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | auth          | Enable the ossec-authd daemon for add agents to the manager.          |
+             +                 +               +-----------------------------------------------------------------------+
|             |                 |               | Server                                                                |
+             +                 +---------------+-----------------------------------------------------------------------+
|             |                 | debug         | Turn off debug mode.                                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+

.. note::
    To use the database option, Database support must be compiled in during initial installation.
