.. _securing_api:

Securing the Armor API
======================

By default, the communications between the Armor Kibana App and the Armor API are not encrypted. You should take the following actions to secure the Armor API.

1. Change default credentials:

  By default you can access by typing user "foo" and password "bar". We recommend you to generate new credentials. This can be done very easily, with the following steps:

  .. code-block:: bash

    $ cd /var/ossec/api/configuration/auth
    $ sudo node htpasswd -c user myUserName

2. Enable HTTPS:

  In order to enable HTTPS you need to generate or provide a certificate. You can learn how to generate your own certificate or generate it automatically using the script ``/var/ossec/api/scripts/configure_api.sh``.

3. Bind to localhost:

  In case you do not need to access to the API externally, you should bind the API to ``localhost`` using the option ``config.host`` placed in the configuration file ``/var/ossec/api/configuration/config.js``.
