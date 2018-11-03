#!/usr/bin/env python
import os
import sys
import subprocess
import argparse

#import ansible
#from collections import namedtuple
#from ansible.parsing.dataloader import DataLoader
#from ansible.vars import VariableManager
#from ansible.inventory import Inventory
#from ansible.playbook.play import Play
#from ansible.executor.playbook_executor import PlaybookExecutor


playbook_path = './mongo.yml'
if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist in path', playbook_path)
    sys.exit()

	
#subprocess.call("ansible-playbook -K ./mongo.yml")
subprocess.call(["ping", "-c 2", "8.8.8.8"])