.. _command-line-register:

Register Agent
----------------------------

1. On the **manager**, run `manage_agents`::

	$ /var/ossec/bin/manage_agents

	****************************************
	* Armor v2.0 Agent manager.            *
	* The following options are available: *
	****************************************
	   (A)dd an agent (A).
	   (E)xtract key for an agent (E).
	   (L)ist already added agents (L).
	   (R)emove an agent (R).
	   (Q)uit.
	Choose your action: A,E,L,R or Q:

2. Press `A` and `Enter` to add an agent. You'll be asked for the agent's name (use the agent hostname or another arbitrary name), its IP and the agent ID (you can leave this field empty to auto-assign an ID).

In this example, we'll add an agent with name "Example", dynamic IP (`any`) and automatic ID::

	Choose your action: A,E,L,R or Q: A

	- Adding a new agent (use '\q' to return to the main menu).
	  Please provide the following:
	   * A name for the new agent: Example
	   * The IP Address of the new agent: any
	   * An ID for the new agent[001]:
	Agent information:
	   ID:001
	   Name:Example
	   IP Address:any

	Confirm adding it?(y/n): y
	Agent added with ID 001.

3. Extract the new agent's key. You will need it for the agent::

	Choose your action: A,E,L,R or Q: E

	Available agents:
	   ID: 001, Name: Example, IP: any
	Provide the ID of the agent to extract the key (or '\q' to quit): 001

	Agent key information for '001' is:
	MDAxIDE4NWVlNjE1Y2YzYiBhbnkgMGNmMDFiYTM3NmMxY2JjNjU0NDAwYmFhZDY1ZWU1YjcyMGI2NDY3ODhkNGQzMjM5ZTdlNGVmNzQzMGFjMDA4Nw==

4. Exit from `manage_agents` by pressing `Q` and `Enter`.

5. Now on the **agent** run `manage_agents`::

	$ /var/ossec/bin/manage_agents

	****************************************
	* Armor v2.0 Agent manager.            *
	* The following options are available: *
	****************************************
	   (I)mport key from the server (I).
	   (Q)uit.
	Choose your action: I or Q:

6. Press `I` and `Enter` to import a key. Then paste the key that you extracted on the manager::

	Choose your action: I or Q: I

	* Provide the Key generated by the server.
	* The best approach is to cut and paste it.
	*** OBS: Do not include spaces or new lines.

	Paste it here (or '\q' to quit): MDAxIDE4NWVlNjE1Y2YzYiBhbnkgMGNmMDFiYTM3NmMxY2JjNjU0NDAwYmFhZDY1ZWU1YjcyMGI2NDY3ODhkNGQzMjM5ZTdlNGVmNzQzMGFjMDA4Nw=

	Agent information:
	   ID:013
	   Name:Example
	   IP Address:any

	Confirm adding it?(y/n): y
	Added.

7. Press `Q` and `Enter` to exit from `manage_agents`.

8. Edit the armor-agent configuration in ``/var/ossec/etc/ossec.conf`` to add the armor-manager IP address. In ``<client>`` section change the ``MANAGE_IP`` value to the armor-manager address::

         <client> 
               <server-ip>MANAGE_IP</server-ip> 
         </client>

9. Restart the agent::

	/var/ossec/bin/ossec-control restart

Forcing insertion
^^^^^^^^^^^^^^^^^^^

If you try to add an agent with an IP that another agent is already registered with, ``manage_agents`` will generate an error. You can use the argument *-d* in order to force the insertion.

Example
~~~~~~~~~~~~~~~~~~

We have installed the agent *Server1* with IP 10.0.0.10 and ID 005. For some reason, we had to reinstall the server, so now we must install a new agent and we need to connect it to the manager. In this case, we can use the argument *-d 0* meaning that the previous agent (005) will be removed (with a backup) and a new agent will be created re-using the IP. The new agent will have a new ID::

    /var/ossec/bin/manage_agents -n Server1 -a 10.10.10.10 -d 0
