.. _armor_agent_solaris:

Install Armor agent on Solaris
===============================


Solaris agent can be downloaded from our :doc:`packages list<../packages-list/index>`. Current version has been tested on Solaris 11 version 5.11 and Solaris 10 version 5.10. The installation step is:

  a) For Solaris 11 i386::

	pkg install -d armor-agent_|ARMOR_LATEST|-sol11-i386.p5p armor-agent

  b) For Solaris 10 i386::

	pkgadd -d armor-agent_|ARMOR_LATEST|-sol10-i386.pkg

  c) For Solaris 11 sparc::

	pkg install -d armor-agent_|ARMOR_LATEST|-sol11-sparc.p5p armor-agent

  d) For Solaris 10 sparc::

	pkgadd -d armor-agent_|ARMOR_LATEST|-sol10-sparc.pkg


.. note:: At this point your agent is installed and you just need to register and configure it to talk to your manager. For more information about this process please visit our user manual.
