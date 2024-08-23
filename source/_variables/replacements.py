###############################################################################
#
# Custom replacements
#
# This file contains the dictionary of custom replacements. Requires the 
# variables 'version', 'release' and 'is_latest_release' from 
# source/_variables/settings.py
#

import sys
import os
sys.path.append(os.path.abspath("_variables"))
from settings import version, is_latest_release, release


custom_replacements = {
    "|ARMOR_LATEST|" : "2.1.1",
    "|ARMOR_LATEST_MINOR|" : "2.1",
    "|ARMOR_LATEST_ANSIBLE|" : "2.1.1",
    "|ARMOR_LATEST_KUBERNETES|" : "2.1.1",
    "|ARMOR_LATEST_PUPPET|" : "2.1.1",
    "|ARMOR_LATEST_OVA|" : "2.1.1",
    "|ARMOR_LATEST_DOCKER|" : "2.1.1",
    "|ELASTICSEARCH_LATEST|" : "5.6.5",
    "|ELASTICSEARCH_LATEST_OVA|" : "5.6.3",
    "|ELASTICSEARCH_LATEST_ANSIBLE|" : "5.6.5",
    "|ELASTICSEARCH_LATEST_KUBERNETES|" : "5.6.5",
    "|ELASTICSEARCH_LATEST_PUPPET|" : "5.6.5",
    "|ELASTICSEARCH_LATEST_DOCKER|" : "5.6.5",
    "|ELASTIC_6_LATEST|" : "5.6.5",
    "|ARMOR_REVISION_AIX|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_I386|" : "1",
    "|ARMOR_REVISION_YUM_MANAGER_I386|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_X86|" : "1",
    "|ARMOR_REVISION_YUM_MANAGER_X86|" : "1",
    "|ARMOR_REVISION_YUM_API_X86|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_AARCH64|" : "1",
    "|ARMOR_REVISION_YUM_MANAGER_AARCH64|" : "1",
    "|ARMOR_REVISION_YUM_API_AARCH64|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_ARMHF|" : "1",
    "|ARMOR_REVISION_YUM_MANAGER_ARMHF|" : "1",
    "|ARMOR_REVISION_YUM_API_ARMHF|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_I386_EL5|" : "1",
    "|ARMOR_REVISION_YUM_AGENT_X86_EL5|" : "1",
    "|ARMOR_REVISION_DEB_AGENT_I386|" : "1",
    "|ARMOR_REVISION_DEB_MANAGER_I386|" : "1",
    "|ARMOR_REVISION_DEB_AGENT_X86|" : "1",
    "|ARMOR_REVISION_DEB_MANAGER_X86|" : "1",
    "|ARMOR_REVISION_DEB_API_X86|" : "1",
    "|ARMOR_REVISION_DEB_AGENT_AARCH64|" : "1",
    "|ARMOR_REVISION_DEB_MANAGER_AARCH64|" : "1",
    "|ARMOR_REVISION_DEB_API_AARCH64|" : "1",
    "|ARMOR_REVISION_DEB_AGENT_ARMHF|" : "1",
    "|ARMOR_REVISION_DEB_MANAGER_ARMHF|" : "1",
    "|ARMOR_REVISION_DEB_API_ARMHF|" : "1",
    "|ARMOR_REVISION_HPUX|" : "1",
    "|ARMOR_REVISION_OSX|" : "1",
    "|ARMOR_REVISION_WINDOWS|" : "2",
    "|CHECKSUMS_URL|" : "https://packages.armor.com/3.x/checksums/",
    "|RPM_AGENT|" : "https://packages.armor.com/3.x/yum/armor-agent",
    "|RPM_MANAGER|" : "https://packages.armor.com/3.x/yum/armor-manager",
    "|RPM_API|" : "https://packages.armor.com/3.x/yum/armor-api",
    "|DEB_AGENT|" : "https://packages.armor.com/3.x/apt/pool/main/w/armor-agent/armor-agent",
    "|DEB_MANAGER|" : "https://packages.armor.com/3.x/apt/pool/main/w/armor-manager/armor-manager",
    "|DEB_API|" : "https://packages.armor.com/3.x/apt/pool/main/w/armor-api/armor-api"
}
