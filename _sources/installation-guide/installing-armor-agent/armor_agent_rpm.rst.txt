.. _armor_agent_rpm:

Install Armor agent with RPM packages
=====================================

The RPM package is suitable for installation on Red Hat, CentOS and other RPM-based systems.

.. note:: Many of the commands described below need to be executed with root user privileges.

Adding the Armor repository
---------------------------

The first thing you need is to add the Armor repository to your server. Alternatively, if you prefer to download the armor-agent package directly, you can find it :ref:`here <packages>`.

Run the following command that corresponds to your specific Linux distribution:

  a) For CentOS:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/GPG-KEY-ARMOR
      enabled=1
      name=CentOS-$releasever - Armor
      baseurl=https://packages.armor.com/yum/el/$releasever/$basearch
      protect=1
      EOF

  a.1) For CentOS-5:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/RPM-GPG-KEY-OSSEC-RHEL5
      enabled=1
      name=CentOS-$releasever - Armor
      baseurl=https://packages.armor.com/yum/el/$releasever/$basearch
      protect=1
      EOF

  b) For RHEL:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/GPG-KEY-ARMOR
      enabled=1
      name=RHEL-$releasever - Armor
      baseurl=https://packages.armor.com/yum/rhel/$releasever/$basearch
      protect=1
      EOF

  b.1) For RHEL-5:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/RPM-GPG-KEY-OSSEC-RHEL5
      enabled=1
      name=RHEL-$releasever - Armor
      baseurl=https://packages.armor.com/yum/rhel/$releasever/$basearch
      protect=1
      EOF

  c) For Fedora:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/GPG-KEY-ARMOR
      name=Fedora-$releasever - Armor
      enabled=1
      baseurl=https://packages.armor.com/yum/fc/$releasever/$basearch
      protect=1
      EOF

  d) For Amazon Linux:

    .. code-block:: bash

      $ cat > /etc/yum.repos.d/armor.repo <<\EOF
      [armor_repo]
      gpgcheck=1
      gpgkey=https://packages.armor.com/key/GPG-KEY-ARMOR
      name=Amazon Linux - Armor
      enabled=1
      baseurl=https://packages.armor.com/yum/el/7/$basearch
      protect=1
      EOF

Installing Armor agent
----------------------

On your terminal, install the Armor agent:

  .. code-block:: bash

	 $ yum install armor-agent-|ARMOR_LATEST|-|ARMOR_REVISION_YUM_AGENT_X86|

.. note:: At this point your agent is installed and you just need to register and configure it to talk to your manager. For more information about this process please visit our user manual.
