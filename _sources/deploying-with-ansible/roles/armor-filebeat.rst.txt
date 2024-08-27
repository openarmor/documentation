.. _ansible-armor-filebeat:

Filebeat
--------------

Filebeat can be used in conjunction with Armor Manager to send events and alerts to Logstash node, this role will install Filebeat, you can customize the installation with these variables:

- **filebeat_output_logstash_hosts:** define logstash node(s) to be use (default: ``127.0.0.1:5000``).

Please review the :ref:`references <armor_ansible_reference_filebeat>` section to see all variables available for this role.
