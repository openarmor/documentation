.. _ansible-armor-agent:

Armor Agent
--------------

This role is designed to install and configure Armor Agent on different hosts, this agent is compatible with Linux and Windows machines. Also, has the ability to register the agent using the ``ossec-authd`` service on the Armor Manager, you can use several variables to customize the installation:

- **armor_manager_ip:** set Armor server to connect.
- **armor_agent_authd:** array with a set of options to register the Armor agent on the Armor server, will require the ``ossec-authd`` service started on the Armor server.

For example, create a YAML file ``armor-agent.yml`` to be used as an Ansible playbook:

.. code-block:: yaml

    - hosts: all:!armor-manager
      roles:
       - ansible-armor-agent

You can maintain different environments using a variable definition YAML file for each one:

a. For production environment ``vars-production.yml``:

.. code-block:: yaml

    armor_manager_ip: 10.1.1.12
    armor_agent_authd:
      enable: true
      port: 1515
      ssl_agent_ca: null
      ssl_agent_cert: null
      ssl_agent_key: null
      ssl_auto_negotiate: 'no'

b. For development environment ``vars-development.yml``:

.. code-block:: yaml

    armor_manager_ip: 192.168.0.10
    armor_agent_authd:
      enable: true
      port: 1515
      ssl_agent_ca: null
      ssl_agent_cert: null
      ssl_agent_key: null
      ssl_auto_negotiate: 'no'

Next, run the ansible playbook:

.. code-block:: bash

  $ ansible-playbook armor-agent.yml -e@vars-production.yml

The example above for production environment will install Armor agent in all host except ``armor-manager``. then it will register against ``armor-manager`` with ip ``10.1.1.12``.

Please review the :ref:`references <armor_ansible_reference_agent>` section to see all variables available for this role.
