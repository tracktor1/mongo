#!/usr/bin/env python
import os
import argparse
import ansible
#from collections import namedtuple
#from ansible.parsing.dataloader import DataLoader
#from ansible.vars import VariableManager
#from ansible.inventory import Inventory
#from ansible.playbook.play import Play
#from ansible.executor.playbook_executor import PlaybookExecutor


playbook_path = './mongo1.yml'

if not os.path.exists(playbook_path):
    print '[INFO] The playbook does not exist'
    sys.exit()