.. _reference_ossec_scanpaths:

Scan paths configuration
=============================

Leaving this unconfigured will result in Armor using the module defaults.

By default, it will monitor ``/etc``, ``/usr/bin``, ``/usr/sbin``, ``/bin`` and ``/sbin`` on the Armor Server, with real time monitoring disabled and report_changes enabled.

To overwrite the defaults or add in new paths to scan, you can use here to overwrite the defaults.

To tell Armor to enable real time monitoring of the default paths:

armor::server::ossec_scanpaths:
-------------------------------

  path: /etc report_changes: 'no' realtime: 'no'

  path: /usr/bin report_changes: 'no' realtime: 'no'

  path: /usr/sbin report_changes: 'no' realtime: 'no'

  path: /bin report_changes: 'yes' realtime: 'yes'

  path: /sbin report_changes: 'yes' realtime: 'yes'

armor::server::ossec_ignorepaths:
----------------------------------

By default, it will empty.

To overwrite the defaults or add in new paths to scan, you can use here to overwrite the defaults.


More information in about syscheck configuration in the :ref:`File integrity monitoring <fim-examples>` section.

.. note::
  Configuring the ossec_scanpaths variable will overwrite the default paths. If you want to add a new directory to monitor, you must also add the above default paths to be monitored as well.
