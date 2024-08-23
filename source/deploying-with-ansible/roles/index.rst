.. _ansible_armor_roles:

Roles
======

You can use these roles to deploy Elastic Stack components, Armor API, Armor Manager and Armor Agents, first clone our `GitHub repository <https://github.com/armor/armor-ansible>`_ directly to your Ansible roles folder:

  .. code-block:: yaml

    $ cd /etc/ansible/roles
    $ git clone https://github.com/armor/armor-ansible.git .

Below we explain briefly how to use these roles, please check out `Ansible Playbooks <http://docs.ansible.com/ansible/playbooks.html>`_ for more information.

.. topic:: Contents

    .. toctree::
        :maxdepth: 2

        armor-manager
        armor-filebeat
        armor-elasticsearch
        armor-kibana
        armor-logstash
        armor-agent
