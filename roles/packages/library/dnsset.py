#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys
def netconf():
  if os.stat("/etc/resolv.conf").st_size <= 1 :
    resconf = open("/etc/resolv.conf", "w")
    resconf.write('nameserver 8.8.8.8')
    resconf.close()
if __name__ == '__main__':
  module = AnsibleModule(argument_spec={})
  netconf()
  module.exit_json(msg="Succesfully configured DNS")
