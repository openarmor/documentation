Upgrading Armor agents
======================

Follow next steps in order to update your ``Armor v1.x`` agents to ``Armor v2.x``.

a) On DEB or RPM based **Linux systems**, you can easily rely on the packages manager to upgrade your agents. The process differs very little from installing a new agent. More information available in our documentation at:

  - :ref:`Install Armor agent with RPM packages <armor_agent_rpm>`
  - :ref:`Install Armor agent with Deb packages <armor_agent_deb>`

  You can check your agent version running the following command:

  .. code-block:: bash

      /var/ossec/bin/manage_agents -V

          Armor v2.0 -OpenArmor Inc.

          This program is free software; you can redistribute it and/or modify
          it under the terms of the GNU General Public License (version 2) as
          published by the Free Software Foundation.

b) On **Windows**, **Mac OS** and other operating systems, we advise you to delete your previous version and install Armor v2.x from scratch. More information can be found at:

  - :ref:`Install Armor agent on Windows <armor_agent_windows>`
  - :ref:`Install Armor agent on Mac OS X <armor_agent_macos>`
